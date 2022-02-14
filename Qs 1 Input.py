#Question 1

text=input("Give a string= ")
list1=[]
list2=text.split()
a=len(list2)
b=dict()
c=dict()
if len(list2)==1:           #It s for 1 word
    for i in text:          #Here i created list with characteres
        list1.append(i)
    for j in list1:         #Here i created a condition where all unique key get
        if j in b:          #value 1 ad when a key is repeated it increases by 1
            b[j]=b[j]+1
        else:
            b[j]=1
    print(b)
    print("Completed")

else:
    for i in list2:         #This is for multiple words
        if i in c:
            c[i]=c[i]+1
        else:
            c[i]=1
    print(c)
    print("Completed")
