import time
import calendar
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Added a list to capture the timing for each section and refer in end to get the performance stats for each section.
performance_stats = []

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city_list= ['chicago','new york city', 'washington']
    city = input("For today's analysis, which city are you curious to explore? Chicago, New York City, or Washington? \n"
                "Input City(Chicago, New York City or Washington):" ).lower()
    # implement while loop to check for user input and pop up a message if values are outside the intended values.
    while city not in ['chicago','new york city', 'washington']:
        city= input("Whoops! Look's like the city you entered is not in the database. \n"
                    "Let's start again,For today's analysis, which city are your curious to explore? Chicago, New York City, or Washington? \n"
                    "Input City(Chicago, New York City or Washington):" ).lower()
    # If the input is accepted, display message and proceed with the month selection
    print('-'*40)
    print ("Great! We will proceed with analysis of {}, if this is not desired city, restart the program \n".format(city.title()))
    print ("Here is a fun fact about {}!\n".format(city.title()))
    if city == 'chicago':
        print ("Spray paint was invented in Chicago in 1949 \n")
    elif city == 'washington':
        print ("Washington has five major volcanoes as part of the Cascade Range: Mount Baker, Glacier Peak, Mount Rainier, Mount Adams and Mount St. Helens. \n")
    else:
        print ("The first American chess tournament was held in New York in 1843. \n")
    print('-'*40)

    # get user input for month (all, january, february, ... , june)
    #month_list= ['january','february','march','april','may','june','all']
    print ("Next up is time range selection \n")
    month = input ("Data is available for range of January to June. \n"
                    "Will you like to explore any specific month available in data set or all the data? \n"
                    "Input Month(specifc month or all):").lower()

    while month not in ['january','february','march','april','may','june','all']:
        month= input("Whoops! Look's like the option you entered is not valid for this database. \n"
                    "Data is available for ranage of January to June. \n"
                    "Will you like to explore any specific month available in data set or all the data? \n"
                    "Input Month(specifc month or all): \n").lower()
    # If the input is accepted, display message and proceed with the day selection
    print('-'*40)
    print("Alright, you are set to explore data for City: {} and selected Time (range or month): {}. If these are not the desired inputs, restart the program \n".format(city.title(),month.title()))
    print('-'*40)
    day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day = input ("Data is available for days Monday to Sunday. \n"
                    "Will you like to explore any specific day available in data set or whole week (all)? \n"
                    "Input Day (specific day or all):").lower()
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        day= input("Whoops! Look's like the option you entered is not valid for this database. \n"
                    "Data is available for range of Monday to Sunday. \n"
                    "Will you like to explore any specific day available in data set or whole week (all)? \n"
                    "Input Day (specific day or all): \n").lower()
    print('-'*40)
    print ("Ok we are set with the inputs. For City: {}, selected Time (range or month) {} and day(s) {}. If these are not the desired inputs, restart the program".format(city.title(),month.title(),day.title()))
    print('-'*40)

    """
    print("While your data is being prepared, here are some fun facts about the city you selected. \n")
    if city == 'chicago':
        print ("Spray paint was invented in Chicago in 1949 \n")
    elif city == 'washington':
        print ("Washington has five major volcanoes as part of the Cascade Range: Mount Baker, Glacier Peak, Mount Rainier, Mount Adams and Mount St. Helens. \n")
    else:
        print ("The first American chess tournament was held in New York in 1843. \n")
    print('-'*40)
    """
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # based on city input by user, import the csv into dataframe using pandas read_csv
    df= pd.read_csv(CITY_DATA[city])

    #Re-using the code from practice problem 3 to make the required columns and filter by month/day.

    # convert the Start Time column to datetime and use the dt.hour function to convert the time into hour number.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start_hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns. Create the number and name for each.
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['month'].apply(lambda x:calendar.month_abbr[x])
    df['day_of_week'] = df['Start Time'].dt.weekday_name



    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df,city,month,day):
    """Displays statistics on the most frequent times of travel.
Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    df - Pandas DataFrame containing city data filtered by month and day
Returns:
    Prints out different statistics computed from data set with a sentence
    (list) performance_stats

    """
    print('Calculating The Most Frequent Times of Travel...\n')
    start_time_month = time.time()

    # display the most common month(mcom_month) and counts (mcom_month_count)
    mcom_month= df['month_name'].mode().loc[0]
    mcom_month_count = df['month_name'].value_counts().loc[mcom_month]
    print ('Most common month is:',mcom_month)
    print ('Number of users for the month are:', mcom_month_count)
    print('-'*40)
    performance_stats.append("Processing time for most common month was %s seconds" % float (time.time()-start_time_month,))

    # display the most common day (mcom_day) of week and user count (mcom_day_count)
    start_time_day = time.time()
    mcom_day = df['day_of_week'].mode().loc[0]
    mcom_day_count = df['day_of_week'].value_counts().loc[mcom_day]
    print('Most common day of the week is:', mcom_day)
    print('Number of users for the day(s) are:', mcom_day_count)
    print('-'*40)

    performance_stats.append("Processing time for most common day was %s seconds" % float (time.time()-start_time_day,))

    # display the most common start hour(mcom_hour) and user count(mcom_hour_count)
    start_time_hour = time.time()
    mcom_hour = df['Start_hour'].mode().loc[0]
    mcom_hour_count = df['Start_hour'].value_counts().loc[mcom_hour]
    print('Most common hour of the day is:',mcom_hour)
    print('Number of users for the busiest hour are:', mcom_hour_count)
    print('-'*40)

    performance_stats.append("Processing time for most common hour was %s seconds" % float(time.time()-start_time_hour,))

    return performance_stats

    print('-'*40)

def station_stats(df,city):
    """ Displays statistics on most popular stations and trips taken.

    Args:
        (str) city - name of the city to analyze
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        Prints out different statistics computed from data set with a sentence
        (list) performance_stats
    """

    start_time = time.time()

    print('\nCalculating The Most Popular Start Stations...\n')
    # display most commonly used start station (mcom_start_station) and users count(mcom_start_station_count)
    start_time_start_station = time.time()
    mcom_start_station = df['Start Station'].mode().loc[0]
    mcom_start_station_count = df['Start Station'].value_counts().loc[mcom_start_station]
    print ('Most popular starting station for selected parameters is:',mcom_start_station)
    print ('Number of users:', mcom_start_station_count)
    print('-'*40)
    performance_stats.append("Processing time for most common start station was %s seconds" % float (time.time()-start_time_start_station),)

    # display most commonly used end station(mcom_end_station) and users count (mcom_end_station_count)
    print('\nCalculating The Most Popular End Stations...\n')
    start_time_end_station = time.time()
    mcom_end_station = df['End Station'].mode().loc[0]
    mcom_end_station_count = df['End Station'].value_counts().loc[mcom_end_station]
    print ('Most popular ending station for selected parameters is:', mcom_end_station)
    print ('Number of users:', mcom_end_station_count)
    print('-'*40)
    performance_stats.append("Processing time for most common end station was %s seconds" % float (time.time()-start_time_end_station),)

    # display most frequent combination of start station and end station trip(mcom_trip) and users count (mcom_trip_count)
    """ To find the most common trip, combination of start and end station is used. After combining the data, statistics
        were computed on top of it."""

    print('\nCalculating The Most Popular Trip between stations...\n')
    start_time_mcom_trip = time.time()
    df['trip'] = df['Start Station']+ df['End Station']
    mcom_trip = df['trip'].mode().loc[0]
    mcom_trip_count = df['trip'].value_counts().loc[mcom_trip]
    print ('Most common trip taken between stations is:',mcom_trip)
    print('Number of users taken this trip are:', mcom_trip_count)
    print('-'*40)
    performance_stats.append("Processing time for most common trip was %s seconds" % float (time.time()-start_time_mcom_trip),)

    return performance_stats
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration along with number of trips taken.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        Prints out different statistics computed from data set with a sentence
        (list) performance_stats
    """

    print('\nCalculating Trip statistics...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    trip_count = df['Trip Duration'].count()
    print ('Total travel time is %s hours'% (total_travel_time//3600),)
    print ('Total number of trips taken are: ', trip_count)
    performance_stats.append("Processing time for calculating total travel time was %s seconds" % float(time.time()-start_time,))

    # display mean travel time
    start_time_travel_mean = time.time()
    travel_time_mean = df['Trip Duration'].mean()
    print ('Average time for each trip is %s minutes' %(travel_time_mean//60),)
    performance_stats.append("Processing time for calculating total travel time was %s seconds" % float(time.time()-start_time_travel_mean,))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users.

    Args:
        (str) city - name of the city to analyze
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        Prints out different statistics computed from data set with a sentence
        (list) performance_stats
    """

    print('Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print ('Total number of users in this analysis are:\n', user_types)
    print('-'*40)
    performance_stats.append("Processing time for calculating total travel time was %s seconds" % float(time.time()-start_time,))

    # Display counts of gender in case of chicago and new york city, for washington data it goes to else statement.
    if city in ['chicago','new york city']:
        start_time_gender = time.time()
        gender_count = df['Gender'].value_counts()
        print ("User split by gender is:\n")
        print(gender_count)
        performance_stats.append("Processing time for calculating total travel time was %s seconds" % float(time.time()-start_time_gender,))

    else:
        print ('No gender data available for Washington state!')


    # Display earliest, most recent, and most common year of birth in case of chicago and new york city, for washington data it goes to else statement.
    if city in ['chicago','new york city']:
        start_time_dob = time.time()
        print('-'*40)
        print('Calculating User profile by Birth Year...\n')
        earliest_dob = df['Birth Year'].min().astype(int)
        recent_dob = df['Birth Year'].max().astype(int)
        mcom_dob = df['Birth Year'].mode().loc[0].astype(int)
        mcom_dob_value= df['Birth Year'].value_counts().loc[mcom_dob]

        print('The oldest users date of birth is:', earliest_dob)
        print('The youngest users date of birth is:', recent_dob)
        print ('Maximum users are from date of birth :' , mcom_dob)
        print('-'*40)
        performance_stats.append("Processing time for calculating total travel time was %s seconds" % float(time.time()-start_time_dob,))
    else:
        print ('No birth data available for Washington state!')
        print('-'*40)

def raw_data(df):
    """
    Displays raw data and uses while to iterate through raw data.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        Keep returing 10 lines of raw data, till user inputs no.
    """
    i = 0
    show_data = input("\n Will you like to see 10 lines of raw data?"
                    "Input (Yes or No): \n")
    while show_data.lower() == 'yes':
        print(df.iloc[i:i + 10])
        i += 10
        show_data = input("Will you like to see 10 more lines of raw data?"
                    "Input (Yes or No): \n")
        print('-'*40)

def summary (performance_stats):
    """Displays time taken by each module in terms of code performance_stats.

    Args:
        (list) performance_stats
    Returns:
        Prints out each item of list in separate line.
    """
    print('-'*40)
    print('-'*40)
    print ("Code performance summary")
    print('-'*40)
    print('-'*40)
    for info in performance_stats:
        print(info)


def main():
    """
    Takes into account all the functions and run them in orderself.
    Restart gives user to go to top of the program and change the parameters again to run the analysis.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,city,month,day)
        station_stats(df,city)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        summary(performance_stats)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
