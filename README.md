# Sneak Score - Machine Learning Experience 


## Overview of the Machine Motivation:

##### Have you ever wondered what totally unrelated data might do when you run your machine learning program?  Well, that was what I wanted to try.
I wanted to see what car you are driving indicate what kind financial freedom you have. Especially by Gender, it would be interesting to see since guys 
love what they are driving more than women.  so here we go.  I am about to predict the your credit score!

##### Data
-	Drivers data - Data from a Car insurance company randomly selected from year 2020 to 2011 insured or attempted to insure
	- Features: Gender, DOB, Credit Score, Owned Vehicle ID (which maps to Vehicles data)
-	Vehicles data - From HLDI vehicle service (Third party provides vehicle details) - selected vhicles between 2010 through 2022
	- Features: Year, Make, Model
	
- 	Extracted data from DB2
	
-	I am hoping that the data is somewhat releated and tells me something meaningful.

### Preprocessing the Data  

		![raw drivers table](readme_raw_tables.PNG.PNG)	<br>
		
		![raw drivers table](population_diagram.PNG )	<br>

-	Sample data of xsls files generated from DB2 instances (500 rows) in the begining of project
- 	Created ETL programs such as with Samples :
	- DOB is converted to age
	![vine review is empty](vine_empty.png)	
	- Null, NA, blank data is dropped
	- Gender is dummified
	- Question was what to do with vehicle
	- Ran a simple model, and gained some score, however the number wasn't feasable
-	Sample data of xls files generated from DB2 instances (500 rows) in the begining of project
	- Later adopted real data set I wanted to run against
	- It was total 2 milion data. Ran it against sample code and it wasn't capable running (Random Forest)
	- Reduced to 1/2 and dropped data group < 100
	- Converted the categorical values to Predictable values using dummy  function (Independent data)
	- Ran K-Means to determine the Bin size and it was similar to standard credit score evaluation, so decided go for it, since it can be very well used when it is interacting web application.


### Clustering Cryptocurrencies Using K-means - 
KMeans – using centroid relocate each centroid to the mean of its assigned ovservations until the clusters no longer change
Note : Also we can use  the WWS (within-cluster sum of Squares)
![Centroids Explained](Images/centroid_explained.PNG)	

### visualizing 
This estimator scales and translates each feature individually such that it is in the given range on the training set, 
e.g. between zero and one.


## Analysis Results:


#### Viweing - There are two primary methodologies for feature scaling in Machine Learning:  Normalization (scaled values are re-arranged to range between 0 to 1) and Standardization. 
Not all feature scaling (values are re-arranged to around means) works for all data, one can improve the performance significantly than the other depending on the data. Machine learning algorithms use
gradient descent as an optimization technique that requires data to be scaled. In this step, we cleaned the data, by droping missing values and numericalize values using get_dummies.
Then we chose Standardization to transform the data for the DecisionTree.  







#### Clustering Cryptocurrencies Using K-means: Machine Learning also uses distance algotithms 


#### visualizing the Results:  In this step using all prepared data from the previous steps, We created 3D to visualized data so far. 

## Analysis Summary:

As you can see in our visualization, there are outliers (class 1, class 3).  However, using Standardization, 
which is following the Gaussian distribution, those outliers won't be affected by standardization (3D), and the clusters range from close to their mean, to compressed.

