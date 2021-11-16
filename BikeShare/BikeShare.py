import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthes=['jan','feb','mar','apr','may','jun','all']
days={'sun':'Sunday',
      'mon':'Monday',
      'tues':'Tuesday',
      'wed':'Wednesday',
      'thur':'Thursday',
      'fri':'Friday',
      'sat':'Saturday',
      'all':'all'}



def get_filters():
    
    month,day='all','all'
  
    print('Hello! Let\'s explore some US bikeshare data!')
    city=input('Would you like to see data about chicago, new york city or washington ?\n')
    
    city=city.lower()
    while (city not in CITY_DATA):
         city=input('Sorry, Invalid city name, enter again\n')
         city=city.lower()
                         
    bool_filter=True
    
    while(bool_filter):
         
        data_filter=input('would you like to filter data by month, day, both, or not at all? type none for no time filter')
        data_filter=data_filter.lower()
        
        if data_filter=='month':
            month=input('Which month? all, jan, feb, mar, apr, may, or jun\n')
            month=month.lower()
            
            while (month not in monthes ):
                month=input('Invalid month! enter all, jan, feb, mar, apr, may, or jun\n')
                month=month.lower()
                
            bool_filter=False
        
        elif data_filter=='day':
            day=input('all, sun, mon, tues, wed, thur, fri, sat\n')
            day=day.lower()
            day=days[day]
            
            
            while (day not in days.values()):
                day=days[input('Invalid day! all, sun, mon, tues, wed, thur, fri, sat\n')]
                day=day.lower()
            bool_filter=False
            
            
        elif data_filter=='both':
            month=input('Which month? all, jan, feb, mar, apr, may, or jun\n')
            month=month.lower()
            
            while (month not in monthes):
                month=input('Invalid month! enter all, jan, feb, mar, apr, may, or jun\n')
                month=month.lower()
            day=days[input('Which day? all, sun, mon, tues, wed, thur, fri, sat\n')]
            day=day.lower()
            
            while (day not in days.values()):
                day=days[input('Invalid day! all, sun, mon, tues, wed, thur, fri, sat\n')]
                day=day.lower()
            bool_filter=False
            
            
        elif data_filter=='none':
            month,day='all','all'
            bool_filter=False
            
        else:
            print('Invalid filter input!!')
            
        print('-'*40)     
        return city,month,day
    
    
    
def load_data(city,month,day):
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    
    if month!= 'all':
        month=monthes.index(month) + 1
        df = df[df['month'] == month]
        
    if day!='all':
        df=df[df['day_of_week']==day.title()]
        
    return df  



def time_stats(df,month,day):
    print('Calculating time statistics....')

    df['Start Time']=pd.to_datetime(df['Start Time'])  
    df['hour']=df['Start Time'].dt.hour
    
    if month=='all':
        popular_month=df['month'].mode()[0]
        print('Most common month: ',popular_month,'count: ',df['month'].value_counts().max())
    if day=='all':
        popular_day=df['day_of_week'].mode()[0]
        print('Most common day: ',popular_day,'count: ',df['day_of_week'].value_counts().max())
        
    popular_hour=df['hour'].mode()[0]
    print('Most common hour:',popular_hour,'count: ',df['hour'].value_counts().max())
    print('-'*40)
    
    
    
    
def station_sats(df):
    print('Calculating station statistics....')
    
    popular_start_station=df['Start Station'].mode([0])
    popular_end_station=df['End Station'].mode([0])
    print('Start Station:',popular_start_station,'Count: ',df['Start Station'].value_counts().max())
    print('End Station:',popular_end_station,'Count: ',df['End Station'].value_counts().max())
    
    
    df['combiation_station']=df['Start Station']+','+df['End Station']
    popular_combination_station=df['combiation_station'].mode()[0]
    print('combination station:',popular_combination_station,'Count: ',df['combiation_station'].value_counts().max())
    print('-'*40)
   

    
    
def trip_duration_stats(df):
    
    print('Calculating trip duration statistics....')
    total_travel_time=df['Trip Duration'].sum()
    df['Trip Duration'].value_counts()
    avg_travel_time=df['Trip Duration'].mean()
    print('Total travel time: ',total_travel_time)
    print('Average Travel time: ',avg_travel_time)
    print('-'*40)
    
    
    
def user_stats(df,city):
    print('Calculating user statistics....')
    print(df['User Type'].value_counts())
    
    if city!='washington':
        
        print(df['Gender'].value_counts())
        print('Smallest user: ',df['Birth Year'].max())#smallesr
        print('Oldest user: ',df['Birth Year'].min())
        print('Most common Birth year: ',df['Birth Year'].mode(),'count: ',df['Birth Year'].value_counts().max())
    print('-'*40)



def display_data(df):
    flag=False
    start_loc=0
    answer=input('Do you want to see the first 5 rows of data?')
    answer=answer.lower()
    if answer=='yes':
        flag=True
        while(flag):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display!='yes':
                break
                
        





def main():
    while True:
        city,month,day=get_filters()
        df=load_data(city,month,day)

        time_stats(df,month,day)
        station_sats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()




