#Question 6

student_info=dict()
n="y"
listsid1=[]
listsid=[]

#a
'''Here i kept an infinity while loop so that we may enter as many name as we like.
and that will be entered in the dictionary.
I have also used if statement so that i can exit the loop whenevr i want
Finally i have made a list which will be used in further parts.'''

print("                (a)              ")
while (n=="y"):
    sid=int(input("Enter your SID= "))
    if sid in listsid:
        print("Error! run the code again and enter a different SID")
        break
    listsid.append(sid)
    name=input("Enter your name= ")
    student_info[sid]=name
    n=input('To continue type "y" else type "n" ')
    listsid1.append((sid,name))
print("The required dicionary= ",student_info)
print("The required list= ",listsid1)
print("Part (a) completed!")


#b
'''To sort our dictionary based on names we will iterate dict.items() twice each
time inversing the key value pair and we will form a list which can be sorted
and converted back to dictionary hence we get the required dictionary'''

print("                (b)        ")
#Now we exhange the key value pair

newdict=dict()
listname=[]
#Now we iterate

for (k,v) in student_info.items():
    newdict[v]=k
    listname.append((v,k))
print("Unsorted Dictionary= ",newdict)
#Now we will sort our list and use it to make sorted dictionary

listname.sort()
sorted_dict=dict(listname)
#Now we just need to exchange the key value pair to get desired dictionary

req_dict=dict()
for (k,v) in sorted_dict.items():
    req_dict[v]=k
print("Dictionary sorted on the basis of name= ",req_dict)
print("Part (b) completed")


#c
'''To sort the dictionary on the basis of SID list we made will be used
we first sort list then convert it to dictionary'''

print("                (c)                ")
#sorting the list

listsid1.sort()
#Now it is sorted and converting it to dictionary

sorted_student_info=dict(listsid1)
print("Sorted dictionary on the basis of SID is= ",sorted_student_info)
print("Part (c) completed")


#d
'''Here i will search the name of the student with the key value or sid'''

print("                (d)                ")
entered_sid=int(input("Enter the SID you want to search= "))
print("The name of the student is= ",student_info[entered_sid])
print("Part (d) completed")
