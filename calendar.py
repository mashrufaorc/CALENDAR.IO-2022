#function returns the number of days in a month  (function)
def month(month):
    #(conditional statements)
    if month == 1:            #January -> 31
        return 31
    elif month == 2:          #February -> 28
        return 28
    elif month == 3:          #March -> 31
        return 31
    elif month == 4:          #April -> 30
        return 30
    elif month == 5:          #May -> 31
        return 31
    elif month == 6:          #June -> 30
        return 30
    elif month == 7:          #July -> 31
        return 31
    elif month == 8:          #August -> 31
        return 31
    elif month == 9:          #September -> 30
        return 30
    elif month == 10:         #October -> 31
        return 31
    elif month == 11:         #November -> 30
        return 30
    elif month == 12:         #December -> 31
        return 31
    else:
        pass

#function returns the remaining days till due date    (function)
def days_left(from_day, from_month, to_day, to_month):
    #initializing variable
    days = 0
    
    #process
    #(conditional statements)
    if to_month != from_month:   #if the final month does not equal to the current month
        days = days + to_day     #add the days of the final month
        #(for loop)
        for i in range(to_month):  #for loop iterating up to the final month
            if i > from_month and i < to_month:   #for all months that are between the current month and the final month
                days = days + month(i)         #add the days of these months to the variable "days"
                i+=1           #iterate up to the next month
            elif i == from_month:  #if the iterated month is equal to the current month
                days = days + (month(from_month) - from_day)  #add the number of days left in the month after today
                i+=1        #iterate up to the next month
            else:
                i+=1        #iterate up to the next month
    else:    #if the final month is equal to the current month
        days = to_day - from_day    #subtracts current day from final day
    
    due_in = "📅 " + str(days) + " day(s) left"       #print statement
    
    return due_in        #returning the days left till due date
    

if __name__ == "__main__":
    
    #intro    
    print("*********************************************************************************")
    print("************************** WELCOME TO CALENDAR.IO 2022 **************************")
    print("*********************************************************************************")
    print("Enter the required information below to find the remaining days.")
    print("*********************************************************************************")
    #variable initialzation
    user_choice = True   #(boolean primitive data type)
    
    #process
    #(while loop)
    while user_choice:  #enters the loop of user_choice is True
        print("Please enter a title: ")      
        title = input("Title: ")            #user inputs title
        print("")
        print("Please enter today's date (numbers only): ")    #user input: current date
        this_day = int(input("Day: "))                                   # day
        this_month= int(input("Month: "))                                # month
        this_year = input("Year: ")                                      # year
        print("")
        print("Please enter the due date (numbers only): ")    #user input: due date
        due_day = int(input("Day: "))                                    # day
        due_month = int(input("Month: "))                                # month
        due_year = input("Year: ")                                       # year
        print("*********************************************************************************")
        print("")
        
        #(conditional statements)
        if due_year == this_year and this_year == "2022": #checks if the years are both 2022 (string comparison)
            print(title + ":" + days_left(this_day, this_month, due_day, due_month))  #calls the function days_left to print the remaining days
        else:    #if one of the year is not 2022, prints an "invalid" statementvv
            print("Invalid! The CALENDAR.IO 2022 works with the year 2022. Please try again.")  
        
        print("")
        print("*********************************************************************************")
        #asks the user if they want to check another task's remaining days
        reply = input("Please enter 'yes' to check another due date or enter any key to conclude: ")
        print("*********************************************************************************")
        
        #(conditional statements) (string comparison)
        if reply.casefold() == "yes":     #if user wants to check another task, the code allows them to do so
            #(boolean primitive data type)
            user_choice = True            
        else:                             #if user wants to exit the program, prints a conclusion statement
            #(boolean primitive data type)
            user_choice = False
            print("Thank you! The session has concluded.")
            print("")
        