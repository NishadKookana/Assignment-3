#Question 7

#fibonacci sequence
first_term=int(input("Give a number= "))
second_term=int(input("Give a number= "))
#Now it will keep on going if the user type y and stop if he types n

sum=first_term+second_term
series=[first_term,second_term]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to continue and n to stop going further-")
print("Now we got a list having a fibonacci series= ",series)

#now lets find average of the resultant fibonacci series
sum=0
for i in series:
    sum=sum+i
print("Average of the sequence= ",sum/len(series))
print("Done!")
