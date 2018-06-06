Project Introduction: Dataset consists of bike sharing statistics for 3 different cities: Washington DC, Chicago and New York. Ridership details such as Starting point, End point, Age, Sex, Usage day etc. are provided in raw data (csv format).

Analysis Details: I utilized python framework to perform analysis on all this data. The program is made interactive for user inputs and a fail safe is built in case user inputs values that are non-relevant to this data. Functions were created to explore dataset by Day, Month or all for a given city. Upon selecting parameters, program reverts back with Most common starting point, Most common end point, Most common trip, Busiest day of the week, Most active user Age group and Sex (if available in dataset).
In the end it also offers to display the raw data (10 lines) to users and then present user with option to either restart the analysis or end the program.

Library versions:
python
pandas
numpy
time
calendar


Reference Articles/documentation:

(website)https://pandas.pydata.org/pandas-docs/stable/timeseries.html -  for panda time functions
(website)stackoverflow : python/pandas: convert month int to month name
(website)stackoverflow: For finding the way to append the list and get it printed in end as code statistics
(website)slack channel: For finding the most common trip
(book) McKinney, Wes. Python for Data Analysis : Data Wrangling with Pandas, NumPy, and IPython, O'Reilly Media : For syntax of code and referring to statistical methods.


