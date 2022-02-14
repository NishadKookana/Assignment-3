#Question 5

word=("ABCDEFGHIJK")
'''We first identify the pattern which says that we need to first leave gaps
equal to count-1 where count tells the row number and the alphabets that
should be decreased after every row'''

count=1
while (count<7):
    print(" "*(count-1),word[0:11-((count-1)*2)])
    count=count+1
print("Completed!")
