#Gene Gittings
#Group 7

import csv, datetime
#import csv and datetime to use each modules function

##1.------------------------------------------------------------------------------------------------------
def storm_by_event(event):
    data = csv.DictReader(open("Indiana_Storms.csv", "r"))
    ## It opens the csv file in a dictionary format.
    for each_data in data:
        ## This forloop goes through each and all of the enries in the file.
        if event in each_data["EVENT_TYPE"]:
            ## The if statement will try to find an entry that matches the argument.
            clean_date = each_data["BEGIN_DATE_TIME"].split("/")
            sorted_date = [str(clean_date[0]),str(clean_date[1]), str(clean_date[2][0:4])]
            organized = "/".join(sorted_date)
            #clearfy to use the date in the print section.
            layout = "A {0} happended on {1} in {2} County"
            #layout for what are we going to print
            print(layout.format(each_data["EVENT_TYPE"], organized, each_data["CZ_NAME"]))
            #print with formate method

event = "Dense Fog"
storm_by_event(event)


##2.------------------------------------------------------------------------------------------------------
#this function works properly in MAC OS, but it won't work on Windows...we do not know why.
            
def storm_by_date(year,month,day):
    date = datetime.date(year,month,day)
    storm_csv = csv.DictReader(open('Indiana_Storms.csv','r'))
    #open the file with csv function with dictionary form
    date_fixed = date.strftime('%-m/%-d/%Y')
##    print(date_fixed)
    for event in storm_csv:
        #print(event)
        clean_date = event["BEGIN_DATE_TIME"].split('/')
        sorted_date = str(clean_date[0]),str(clean_date[1]),str(clean_date[2][0:4])
        organized = '/'.join(sorted_date)
        #clearfy to use the date in the print section.
        if organized == date_fixed:
        #give condition that if orgainized equal to date_fixed
            layout = "A {0} happended on {1} in {2} county."
            #layout for what are we going to print
            print(layout.format(event['EVENT_TYPE'], date_fixed, event['CZ_NAME']))
            #print with formate method
    
    
    
    
    

storm_by_date(2017,5,15)


##3.------------------------------------------------------------------------------------------------------

while True:
    data = csv.DictReader(open("Indiana_Storms.csv", "r"))
    #open the file by using csv function as dictionary form
    search_method = input("Would you like to search by date or by event? ")
    #get input from user that what the user want to search with

    if search_method.lower() == "event":
        #condition for when we get "event" from search_method
        enter_event = input("Please enter the type of weather you are searching for: ")
        #get another input from user that what kind of weather user is looking for
        for event in data:
            if enter_event in event["EVENT_TYPE"]:
                #if enter_event is in event["EVENT_TYPE"], then following the below statement
                clean_date = event["BEGIN_DATE_TIME"].split("/")
                sorted_date = [str(clean_date[0]),str(clean_date[1]), str(clean_date[2][0:4])]
                organized = "/".join(sorted_date)
                #we need to reagrrange to use in the print section
                layout = "A {0} happended on {1} in {2} County"
                #layout for what python will print
                print(layout.format(event["EVENT_TYPE"], organized, event["CZ_NAME"]))
                #print with formate method
        break
        #break for stop this program when all the progress is done.

        
    elif search_method.lower()== "date":
    #another condition for when we get "event" from search_method
        enter_date = input("Please enter your date in YYYY/MM/DD format: ")
        clean_enter = enter_date.split("/")
        sorted_date = "/".join([str(int(clean_enter[1])),str(int(clean_enter[2])), str(int(clean_enter[0]))])
        #we need to reagrrange to use datetime functions as year, month and day
        for each_data in data:
        #using for loop to check each data from data
            if sorted_date in each_data["BEGIN_DATE_TIME"]:
                #condition that if sorted_date in each_data["BEGIN_DATE_TIME"], then folling the below statement
                layout = "A {0} happened on {1} in {2} county"
                #layout for what python will print
                print(layout.format(each_data["EVENT_TYPE"], sorted_date, each_data["CZ_NAME"]))
                #print with formate method
        break
        #break for stop this program when all the progress is done.
            

    else:
    #else for if we get somthing from enter_event but it is not suit for the previous conditions then following the below statement.
        print("That is not a valid selection. Please try again")
        #print that it is not a valid

#bonus--------------------------------------------------------------------------------------------------------
        
while True:
    data = csv.DictReader(open("Indiana_Storms.csv", "r"))
    #open the file by using csv function as dictionary form
    search_method = input("Would you like to search by date or by event? ")
    print()
    #get input from user that what the user want to search with

    if search_method.lower() == "event":
        #condition for when we get "event" from search_method
        enter_event = input("Please enter the type of weather you are searching for: ")
        #get another input from user that what kind of weather user is looking for
        for event in data:
            if enter_event in event["EVENT_TYPE"]:
                #if enter_event is in event["EVENT_TYPE"], then following the below statement
                clean_date = event["BEGIN_DATE_TIME"].split("/")
                sorted_date = [str(clean_date[0]),str(clean_date[1]), str(clean_date[2][0:4])]
                organized = "/".join(sorted_date)
                #we need to reagrrange to use datetime functions as year, month and day
                layout = "On {0} the {1} of {2} {3}. This was reported in {4} county. {5}"
                #layout for what python will print
                print(layout.format(date.strftime("%A"), date.strftime("%d"), date.strftime("%B"), each_data["EPISODE_NARRATIVE"], each_data["CZ_NAME"], each_data["EVENT_NARRATIVE"] ))
                #print with formate method
                print()
                print()
        break
        #break for stop this program when all the progress is done.

        
    elif search_method.lower()== "date":
    #another condition for when we get "event" from search_method
        enter_date = input("Please enter your date in YYYY/MM/DD format: ")
        clean_enter = enter_date.split("/")
        sorted_date = "/".join([str(int(clean_enter[1])),str(int(clean_enter[2])), str(int(clean_enter[0]))])
        #rearrange the date to print out correct form
        date = datetime.date(int(clean_enter[0]),int(clean_enter[1]), int(clean_enter[2]))
        #to use datetime function make a right format
        
        for each_data in data:
        #using for loop to check each data from data
            if sorted_date in each_data["BEGIN_DATE_TIME"]:
                #condition that if sorted_date in each_data["BEGIN_DATE_TIME"], then folling the below statement
                layout = "On {0} the {1} of {2} {3}. This was reported in {4} county. {5}"
                #layout for what python will print
                print(layout.format(date.strftime("%A"), date.strftime("%d"), date.strftime("%B"), each_data["EPISODE_NARRATIVE"], each_data["CZ_NAME"], each_data["EVENT_NARRATIVE"] ))
                #print with formate method
                print()
                print()
        break
        #break for stop this program when all the progress is done.
            

    else:
    #else for if we get somthing from enter_event but it is not suit for the previous conditions then following the below statement.
        print("That is not a valid selection. Please try again")
        #print that it is not a valid
