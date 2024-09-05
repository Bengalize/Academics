# Logical Operators
# Checking if 2+2 equals 5
2 + 2 == 5

# Check if 8^13 is less than 15^9
8^13 < 15^9

# Variables
# Assigning the value 79 to the variable 'potato'
potato <- 79
# Printing 'potato'
print(potato)

# Calculating the square root of 'potato' and printing
sqrt(potato)
print(potato)

# Reassigning 'potato' to 'potato * 2' and printing the new value
potato <- potato * 2
print(potato)

# Creating variables: string, logical, and missing value (NA)
my_string <- "Hello, world"
my_logic <- TRUE
my_missing <- NA

# Checking the type of each variable
class(my_string)
class(my_logic)
class(my_missing)

# Vectors
# Creating a numeric vector
c(1, 2, 3)

# Creating a character vector
c("Hello", "Beautiful", "World")

# Creating a named numeric vector 'age'
age <- c(20, 21, 13)
names(age) <- c("Malik", "Mohamed", "Papito")
print(age)

# Indexing by number to get the first element of 'age'
first_element <- age[1]
print(first_element)

# Logical indexing to return ages greater than 20
ages_greater_than_20 <- age[age > 20]
print(ages_greater_than_20)

# Indexing by name to get Malik's age
print(age["Malik"])

# Matrices and Dataframes
# Loading the airquality dataset and printing 'Wind' variable
data(airquality)
print(airquality$Wind)

# Printing the third element of 'Wind'
print(airquality$Wind[3])

# Creating a dataframe 'aq' with the first 10 cases of airquality
aq <- airquality[1:10, ]

# Logical indexing to print Ozone levels greater than 20
print(aq[aq$Ozone > 20, ])  # NA values appear as NA

# Using subset() to print Ozone levels greater than 20
print(subset(aq, Ozone > 20))  # NA values are omitted

# Adding a logical column 'TooWindy' where Wind > 10
aq$TooWindy <- aq$Wind > 10
print(aq)

# Using length() to find the number of observations in airquality
length(airquality)

# Calculating mean and standard deviation of the 'Temp' variable
mean(airquality$Temp)
sd(airquality$Temp)

# Creating a table of 'Temp' values
temp_table <- table(airquality$Temp)
print(temp_table)

# Creating a histogram of the 'Ozone' variable
hist(airquality$Ozone)
# The Ozone distribution is skewed, not a normal distribution.

# Functions
# Defining a simple function that adds 6 to x
simp_func <- function(x) {
  print(x + 6)
}

# Applying simp_func to the 'Temp' column
simp_func(airquality$Temp)

# Packages
# Installing and loading required packages
install.packages("ggplot2")
install.packages("car")
install.packages("ez")
library(car)

# Importing a CSV file
install.packages("rio")
library(rio)
my_csv <- import("/Users/bengalycisse/Downloads/lab_R_learning.csv")
head(my_csv)
