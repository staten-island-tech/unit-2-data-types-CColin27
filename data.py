""" #Data Types
#numbers 1,2,3
def add(x,y):
    print(x + y)
add(1,2)

#strings "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)

#1 and "1" are not the same
#undefined/null

#booleans
tenure = True
def is_tenured(status):
    if(status == True):
        print("They have tenure")
    else:
        print("They are not tenured") """




""" animals = ["zebra", "camel", "Ape"]
#Start count at 0, reference eache element with []
print(animals[0])
for animal in animals:
    print(animal) """

""" for animal in animals:
    if (animal == "camel"):
        print("we're in the desert") """

#Strings operate like lists
x = "Hello Freshman, you all smell"
#print(x[0])
#y = x.upper()
#print(y)
words_list = x.split( )
print(len(words_list))




#Floats
""" x = 3
y = float(3)
print(x,y)  """



#Lists
""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])  



""" #String Methods
""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)  """



""" Question = "Input a Sentence"
def answer(response):
    print(response)
answer(Question)  """ 



""" #Booleans
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """



#F Strings
""" x = "test"
print(f"hello {x}") """


""" temp = 75 
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """



#Challenge 1
""" number = int(input("Enter a number: "))
if number%2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.") """


#Challenge 2
""" x = "0%,15%,20%,25%"
x = "0%,15%,20%,25%"
print(f" {x}")
Tip = input("Choose a Tip Amount")
if Tip == "0%":
    print("bad")
if Tip == "15%":
    print("okay")
if Tip == "20%":
    print("good")
else:
    print("great")
 """


#Challenge 3
""" number = int(input("enter a number and I will tell all the factors of the number up to 12: "))
print(f"{number}")
print("1")
if number%2 == 0:
    print("2")
if number%3 == 0:
    print("3")
if number%4 == 0:
    print("4")
if number%5 == 0:
    print("5")
if number%6 == 0:
    print("6")
if number%7 == 0:
    print("7")
if number%8 == 0:
    print("8")
if number%9 == 0:
    print("9")
if number%10 == 0:
    print("10")
if number%11 == 0:
    print("11")
if number%12 == 0:
    print("12") """


#Challenge 4
""" number = int(input("enter a number: "))
print(f"{number}")
number2 = int(input("Now enter another number: "))
print(f"{number2}")
print(f"the GCF of {number} and {number2} is.. ")
 """