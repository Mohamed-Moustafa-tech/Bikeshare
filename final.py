import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        CITY=input("Would you like to see data for Chicago, New York, or Washington? ")
        city=CITY.lower()
        if city in ["washington","chicago","new york"]:
            break
        else:
            print("Please enter correct spelling, Avoid using spaces before or after the entry")


    while True:
        Time_Filter= input("Would you like to filter the data by month, day, or not at all?")
        time_filter=Time_Filter.lower()
        if time_filter == "month":
            while True:
                month = input("Which month - January, February, March, April, May, or June or 'all'?")
                month = month.lower()
                if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                    day = None
                    break
                else:
                    print("please enter correct spelling, Avoid using spaces before or after the entry")
            break
        elif time_filter == "day":
            while True:
                day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday or 'all'?")
                day = day.lower()
                if day in ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']:
                    month = None
                    break
                else:
                    print("please enter correct spelling, Avoid using spaces before or after the entry")
            break
        elif time_filter == "not at all":
            month = None
            day = None
            break
        else:
            print("Please enter correct spelling, Avoid using spaces before or after the entry")

    print('-'*40)
    return city, month, day
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')





def load_data(city, month, day):
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month !=None:
        if month != 'all':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month1 = months.index(month)+1
            df = df[df['month']==month1]
    elif day != None :
        if day != 'all':
            # filter by day of week to create the new dataframe
            #days= ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
            df =df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most Frequent month:",popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent day of week:',popular_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_com_sta= df['Start Station'].mode()[0]
    print('Most common Start Station:', most_com_sta)


    # TO DO: display most commonly used end station
    most_com_end= df['End Station'].mode()[0]
    print('Most Common End Station:', most_com_end)


    # TO DO: display most frequent combination of start station and end station trip
    most_com_sta_end = (df['Start Station'] + " " + df['End Station']).mode()[0]
    print("Most common combination of Start and end stations:", most_com_sta_end.split(" "))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print(df.groupby(['month'])['Trip Duration'].sum())
    print(df.groupby(['day_of_week'])['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df.groupby(['month'])['Trip Duration'].mean())
    print(df.groupby(['day_of_week'])['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types =df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    Gender =df['Gender'].value_counts()
    print(Gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    print('Earliest year of birth:\n', df['Birth Year'].min())
    print('Most recent year of birth:\n', df['Birth Year'].max())
    print('Most common year of birth:\n', df['Birth Year'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
