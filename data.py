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
""" Question = input("Type a number between 1-10")
if Question == "1":
    print('odd')
elif Question == "2":
    print('even')
elif Question == "3":
    print('odd')
elif Question == "4":
    print('even')
elif Question == "5":
    print('odd')
elif Question == "6":
    print('even')
elif Question == "7":
    print('odd')
elif Question == "8":
    print('even')
elif Question == "9":
    print('odd')
elif Question == "10":
    print('even')
 """

""" Question = input("Type a number and I will tell you if it is odd or even")
if Question % 2 == 0:
    print('even')
else:
    print('odd') """


number = int(input("Enter a number: "))
if number%2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


#Challenge 2
""" x = "0%,15%,20%,25%"
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
""" factors = input("Type a number between 1-10") """



