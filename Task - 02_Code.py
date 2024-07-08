#1.DATA CLEANING:
##Installing necessary libraries
import pandas as pd
import numpy as np
##Importing csv file
df=pd.read_csv(r"C:\Users\snmur\OneDrive\Desktop\Internship_Prodigy\Task - 02_Raw_Data.csv")
##Analysing and cleaning the csv file
###Analysing the csv file
print(df.shape) #The (df.shape) method prints the dimensions of the dataframe (number of rows, number of columns).
print(df.columns) #The (df.columns) method prints the column names of the dataframe.
###Cleaning the csv file
#Step:01 Dropping unnecessary columns
df=df.drop(["url","address","reviews_list","dish_liked","menu_item","phone","listed_in(type)","listed_in(city)"],axis=1) #The (df.drop(["",""])) method removes the specified columns from the dataframe.
print(df.shape)
print(df.columns)
#Step:02 Dropping duplicate rows
df=df.drop_duplicates() # The df.drop_duplicates() method removes duplicate rows.
print(df.shape)
#Step:03 Renaming column names
df.columns=["RESTAURANT NAME","ONLINE ORDER","TABLE BOOKING","RATING","NO OF VOTES","RESTAURANT LOCATION","RESTAURANT TYPE",
           "CUISINES AVAILABLE","APPROXIMATE COST FOR 2 PEOPLE"] 
#Step:04 Displaying a concise summary of the dataframe, including the number of non-null entries, column names, data types, and memory usage.
df.info() #The df.info() method provides summary of dataframe.
#from the output of the Step:04 it is clear that the columns "RATING,RESTAURANT LOCATION,RESTAURANT TYPE,CUISINES AVAILABLE,APPROXIMATE COST FOR 2 PEOPLE" has some null values that need to changed which is done in the further steps
#Step:05 Cleaning "RATING" column
print(df["RATING"].unique()) #The df[" "].unique() method removes all duplicate values on a column and returns a single value for multiple same values.
print(df["RATING"].isnull().sum()) #The df[column name].isnull().sum() method gives the sum of null values in the specified column.
df["RATING"] = df["RATING"].replace(['NEW', '-'], np.nan) #The df.["column name"].replace(["specified value"], np.nan) method replaces specified values with NaN values in a specified column.
df["RATING"]=df["RATING"].str.split("/").str[0]
df["RATING"] = df["RATING"].fillna(df["RATING"].mode()[0]) #The df["column name"].fillna(specified value) method fills the null values of a column with a specified value, here mode of the column.
df["RATING"] = df["RATING"].astype(float) #The df["column name"].astype(specified data type) method changes data type of a specified column.
print(df["RATING"].isnull().sum())
print(df["RATING"].unique())
print(df.info())
#Step:06 Cleaning "RESTAURANT LOCATION" column
print(df["RESTAURANT LOCATION"].isnull().sum())
print(df["RESTAURANT LOCATION"].unique())
print(df["RESTAURANT LOCATION"].value_counts()) #The df["column name"].value_counts() method counts the number of occurrences of each unique value in a dataframe column.  
RESTAURANT_LOCATION_COUNTS=df["RESTAURANT LOCATION"].value_counts()
RESTAURANT_LOCATIONS_TO_REPLACE = RESTAURANT_LOCATION_COUNTS[RESTAURANT_LOCATION_COUNTS < 100].index #
df["RESTAURANT LOCATION"] = df["RESTAURANT LOCATION"].replace(RESTAURANT_LOCATIONS_TO_REPLACE, "Others")
df["RESTAURANT LOCATION"] = df["RESTAURANT LOCATION"].fillna("Unknown")
print(df["RESTAURANT LOCATION"].isnull().sum())
print(df["RESTAURANT LOCATION"].unique())
print(df["RESTAURANT LOCATION"].value_counts())
#Step:07 Cleaning "RESTAURANT TYPE" column
print(df["RESTAURANT TYPE"].isnull().sum())
print(df["RESTAURANT TYPE"].unique())
print(df["RESTAURANT TYPE"].value_counts())
RESTAURANT_TYPE_COUNTS=df["RESTAURANT TYPE"].value_counts()
RESTAURANT_TYPES_TO_REPLACE = RESTAURANT_TYPE_COUNTS[RESTAURANT_TYPE_COUNTS < 100].index
df["RESTAURANT TYPE"] = df["RESTAURANT TYPE"].replace(RESTAURANT_TYPES_TO_REPLACE, "Others")
df["RESTAURANT TYPE"] = df["RESTAURANT TYPE"].fillna("Unknown")
print(df["RESTAURANT TYPE"].isnull().sum())
print(df["RESTAURANT TYPE"].unique())
print(df["RESTAURANT TYPE"].value_counts())
#Step:08 Cleaning "CUISINES AVAILABLE" column
print(df["CUISINES AVAILABLE"].isnull().sum())
print(df["CUISINES AVAILABLE"].unique())
print(df["CUISINES AVAILABLE"].value_counts())
CUISINES_AVAILABLE_COUNTS=df["CUISINES AVAILABLE"].value_counts()
CUISINES_AVAILABLE_TO_REPLACE = CUISINES_AVAILABLE_COUNTS[CUISINES_AVAILABLE_COUNTS < 100].index
df["CUISINES AVAILABLE"] = df["CUISINES AVAILABLE"].replace(CUISINES_AVAILABLE_TO_REPLACE, "Others")
df["CUISINES AVAILABLE"] = df["CUISINES AVAILABLE"].fillna("Unknown")
print(df["CUISINES AVAILABLE"].isnull().sum())
print(df["CUISINES AVAILABLE"].unique())
print(df["CUISINES AVAILABLE"].value_counts())
#Step:09 Cleaning "APPROXIMATE COST FOR 2 PEOPLE" column
print(df["APPROXIMATE COST FOR 2 PEOPLE"].unique())
print(df["APPROXIMATE COST FOR 2 PEOPLE"].isnull().sum())
df["APPROXIMATE COST FOR 2 PEOPLE"] = df["APPROXIMATE COST FOR 2 PEOPLE"].str.replace(',', '')
df["APPROXIMATE COST FOR 2 PEOPLE"] = df["APPROXIMATE COST FOR 2 PEOPLE"].fillna(df["APPROXIMATE COST FOR 2 PEOPLE"].mode()[0]) #inplace=True
df["APPROXIMATE COST FOR 2 PEOPLE"] = df["APPROXIMATE COST FOR 2 PEOPLE"].astype(int)
print(df["APPROXIMATE COST FOR 2 PEOPLE"].isnull().sum())
print(df["APPROXIMATE COST FOR 2 PEOPLE"].unique())
print(df.info())
print(df.tail(50))
#2.Exploratory Data Analysis (EDA):
##Identifying patterns, trends, and relationships between variables:
###Descriptive statistics: (mean,median,mode, etc.)
print(df.describe()) #The (df.describe()) method returns description of the data in the dataframe. 
###Data visualization: (bar graphs,box plots,pie charts e.t.c)
#Bar graph describing number of restaurants location wise
#Installing necessary libraries
import matplotlib.pyplot as plt
#Extracting data for plotting
location_counts = df["RESTAURANT LOCATION"].value_counts()
x=location_counts.index
y=location_counts.values
#Bar graph customization
#Step:01 Plot the bar graph
plt.bar(x,y,color=("#E9967A","#8FBC8F","#483D8B","#696969","#CD5C5C","#20B2AA","#D2B48C","#ADD8E6","#DB7093","#9370DB"))
#Step:02 Define font properties
font1={"family":"serif","color":"#2F4F4F","weight":"bold","size":"20"}
font2={"family":"serif","color":"#2F4F4F","weight":"semibold","size":"15"}
#Step:03 Setting titles and labels
plt.title("Distribution of Restaurants by Location",fontdict=font1,loc="center")
plt.xlabel("Location",fontdict=font2,loc="center")
plt.ylabel("Number of Restaurants",fontdict=font2,loc="center")
#Step:04 Setting up grid properties
plt.grid(axis="both",color="#000000",linestyle="solid",linewidth=0.5)
#Step:05 Setting up xticks
plt.xticks(rotation=90)
#Step:06 Displaying the graph
plt.tight_layout()
plt.show()
#Box plot describing the rating of a restaurant based on the approximate cost of food for two people
#Installing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
#Extracting data for plotting
x=df['APPROXIMATE COST FOR 2 PEOPLE']
y=df['RATING']
#Box plot customization
#Step:01 Plot the box plot
sns.boxplot(x=df['APPROXIMATE COST FOR 2 PEOPLE'],y=df['RATING'],palette="Set1")
#Step:02 Define font properties
font1={"family":"serif","color":"#2F4F4F","weight":"bold","size":"20"}
font2={"family":"serif","color":"#2F4F4F","weight":"semibold","size":"15"}
#Step:03 Setting titles and labels
plt.title("Restaurant rating based on approximate food cost for two people",fontdict=font1,loc="center")
plt.xlabel("Approximate Cost for 2 People",fontdict=font2,loc="center")
plt.ylabel("Rating",fontdict=font2,loc="center")
#Step:04 Setting up grid properties
plt.grid(axis='both',color="#000000",linestyle="solid",linewidth=0.5)
#Step:05 Setting up xticks
plt.xticks(rotation=90)
#Step:06 Displaying the plot
plt.tight_layout()
plt.show()
#Pie chart representing availability of table booking of different restaurants
#Installing necessary libraries
import matplotlib.pyplot as plt
#Extracting data for plotting
x=df["TABLE BOOKING"].value_counts()
#Pie chart customization
#Step:01 Setting up mycolors and myexplode
mycolors=["r","b"]
myexplode=[0.5,0]
#Step:02 Plot the pie chart
plt.pie(x,startangle=180,explode=myexplode,shadow=True,colors=mycolors)
#Step:03 Define font properties
font1={"family":"serif","color":"#2F4F4F","weight":"bold","size":"20"}
#Step:04 Setting up title
plt.title("Availability of table booking at different restaurants",fontdict=font1,loc="center")
#Step:05 Setting up legend
plt.legend(title="Table Booking",labels=x.index,loc="best")
#Step:06 Displaying the plot
plt.show()

