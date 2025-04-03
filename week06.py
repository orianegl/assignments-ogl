#below is same prompt but phrased differently

def pig_latin(word):
  prefix = word[1:]
  suffix = word[0]
  return prefix + suffix + "ay"

print("Hazel"[1:]+"Hazel"[0]+"ay")
print("is"[1:]+"is"[0]+"ay")
print("a"[1:]+"a"[0]+"ay")
print("good"[1:]+"good"[0]+"ay")
print("dog"[1:]+"dog"[0]+"ay")

def pig_latin(word):
  return word[1:]+word[0].lower()+"ay"

def repeat (word, number):
  return (word+" ")*number

input = "praxis codelab code lab"
l = input.split(" ")    
print(repeat(pig_latin(l[0]),10) + " ".join(l[1:]))


infile = open('week06/shakespeare.txt', "r")