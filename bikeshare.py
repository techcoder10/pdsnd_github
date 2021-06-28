import time
import pandas as pd
import numpy as np

# declare global variables
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june']


weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']

city = None
month = None
day = None
show_raw_data = None

# helper functions

def show_data(df):
    """
    Prints raw data after the user respondes yes and does not print raw data if the user responds no
  
       
    """
     print("_____________Printing Top 5 Rows__________________________")
     print(df.head(5))
     print("__________________________________________________________")
        
def ask_for_data():
    """
    Asks user if they want to receive the raw data by asking yes or no
  
       
    """
    global show_raw_data
    response_list = ["yes", "no"]
    response = ''
    while response.lower() not in response_list:
        response = input("Please enter yes or no if you want to view the data: ")
    show_raw_data = response.lower()        
        

def ask_city():
    """
    Ask user to type in what city they want from the three options: Chicago, New York City, and Washington
  
       
    """
    global city
    response = ''
    while response.lower() not in cities:
        response = input("Please enter correct city: chicago, new york city, washington: ")
    city = response
    
def ask_month():
    """
    Ask user to type in what month they want from the data 
  
       
    """
    global month
    response = ''
    while response.lower() not in months:
        response = input("Please enter correct month: 'january', 'february', 'march', 'april', 'may', 'june': ")
    month = response
    
def ask_day():
    """
    Ask user to type in what day they want from the data 
  
       
    """
    global day
    response = ''
    while response.lower() not in weekdays:
        response = input("Please enter correct day of week: 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday': ")
    day = response
   
  
    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    global city
    global month
    global day
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    ask_city()

    # TO DO: get user input for month (all, january, february, ... , june)
    ask_month()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    ask_day()
    
    # TO DO: ask user if they want to see data
    ask_for_data()

    print('-'*40)
    #print(city, month, day)
    city = city.lower()
    month = month.lower()
    day = day.lower()
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city],index_col=0)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    print('Most Common Month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_ofweek = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', most_common_day_ofweek)

    # TO DO: display the most common start hour
    
    most_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:',  most_common_start_station )


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most End Station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
     # TO DO: Display counts of gender
     print('Gender Stats:')
     print(df['Gender'].value_counts())

     # TO DO: Display earliest, most recent, and most common year of birth
     earliest_year = df['Birth Year'].min()
     print('Earliest Year:',earliest_year)
     most_recent_year = df['Birth Year'].max()
     print('Most Recent Year:',most_recent_year)
     most_common_year = df['Birth Year'].mode()[0]
     print('Most Common Year:',most_common_year)
        
               
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # if user wants then print raw data then this code will run
        if (show_raw_data == "yes"):
            show_data(df)
         
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
