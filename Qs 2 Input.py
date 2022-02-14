#Question 2

month=int(input("Enter month= "))

if (month in [1,3,5,7,8,10,12]):
          date=int(input("Enter a date= "))
          if (1<=date<=31):
                  year=int(input("Enter a year= "))
                  if (1800<=year<=2025):
                      print("Date=",date,"/",month,"/",year)
                      if(month==12 and date==31):
                          print("Next date is=1/1/",year+1)
                      elif(date==31):
                          print("Next date is= 1/",month+1,"/",year)
                      else:
                          print("Next date is=",date+1,"/",month,"/",year)
                  else:
                      print("Invalid year")
          else:
              print("Invalid date")

elif (month in [4,6,9,11]):
    date=int(input("Enter a date= "))
    if (1<=date<=30):
        year=int(input("Enter a year= "))
        if (1800<=year<=2025):
            print("Date is= ",date,"/",month,"/",year)
            if (date==30):
                 print("Next date is= 1/",month+1,"/",year)
            else:
                print("Next date is= ",date+1,"/",month,"/",year)
        else:
            print("Invalid year")
    else:
        print("Invalid Date")


elif (month==2):
    year=int(input("Enter a year= "))
    if (1800<=year<=2025):
        date=int(input("Enter a date= "))
        if(year%4==0):
            if (1<=date<=29):
                print("Date=",date,"/",month,"/",year)
                if (date==29):
                    print("Next date is= 1/3/",year)
                else:
                    print("Next date is= ",date+1,"/",month,"/",year)
            else:
                print("Invalid Date")
        else:
            if (1<=date<=28):
                print("Date= ",date,"/",month,"/",year)
                if (date==28):
                    print("Next date is= 1/3/",year)
                else:
                    print("Next date is= ",date+1,"/",month,"/",year)
            else:
                print("Invalid Date")
    else:
        print("Invalid year")
else:
    print("Invalid month")
print("Completed")
                 
    
             
            
                  
                
                  
                  
                  
