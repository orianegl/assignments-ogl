#the first thing a program does = setting the variables; then going line by line

def pig_latin(word):
    first_letter = word[0]
    rest_word = word[1:]
    platin = rest_word + first_letter + "ay"
    return platin 

x = 5
if x == 0:
    print("Zero")
    print ("Positive")
elif x<0:
    print("Negative")
else:
    print("Positive")

print("done")

x = 5
if not(x>0 or x<0):
  print("ZERO")

  def sum(number_list):
    x = 0
    sum = 0
    while x<len(number_list):
        sum = sum + number_list[x]
        x = x+1
    return sum

 # Assignment 3
def filter_evens(numbers):
   evens = []
   for number in numbers:
      if number % 2 == 0
      evens.append(number)
  

nums = [0,-2,3,14]
print(filter_evens(nums))

