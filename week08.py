while 1:
    word = input("What do you say? ")
    if word.upper() == "DUCK":
        continue
    elif word.upper() == "GOOSE":
        break
    print("Maybe I should explain the rules again...")


    x = [3,5,2,7,5]
    i = 0
    while i < len(x)-1:
    j = i+1
    while j < len(x):
    if x[i] == x[j]:
    print ("Duplicate")
    j+= 1
    i+=1

    def got_dupes(numbers):
    i = 0 # i is the first counter, for the outer loop
    while i < len(numbers)-1: #we don't need to loop at the very last number on the outside loop because there's nothing to compare it to
        j = 0 # j is the second counter, for the inner loop
        while j < len(numbers):
            if numbers[i] == numbers[j]:
                return True #duplicate found! Returning True.
            j+=1
        i+=1
    return False #if we complete all the looping without returning, there must not have been any duplicates

#print nested lists elements
x=[[0 ,1 ,2 ,3 ,4 ,5],
   [10,11,12,13,14,15],
   [20,21,22,23,24,25]]
for i in x:
    for j in i:
        print(j)

#return change homework week 8
        DENOMINATIONS = [100,20,10,5,1,0.25,0.1,0.5,0.01]

def change(cost, payment):
    if cost - payment > 0:
        return None
    change = []
    remainder = payment - cost 
    for denomination in DENOMINATIONS:
        while (remaining_change >= denomination):
            ##your code here
    return change

# Test cases
print(change(5,2.55))
print(change(2.55,5))
print(change(5,5))
print(change(0,5))