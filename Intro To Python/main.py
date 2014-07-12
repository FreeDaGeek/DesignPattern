#one lined comments
"""
Multi line Doc strings comments
"""

#Declare Variable
first_name = "Kermit"
last_name = "Da Frog"
#print first_name

#Raw input Method
#response = raw_input("Enter your name?")
#print "Hello There, ",response

birth_year = 1988
current_year = 2014
age = current_year - birth_year
#print age
#print "You are " + str(age) + " years old"

#Conditonal Statements
budget =90

if budget > 100:
    brand = "Nike"
    print "Yay! We can buy cool" + brand + " shoes!"
elif budget > 75:
    print "We can at least get the bootlegs"
else:
    print "No cool shoes for me."

# Incl Pass if the condtions is empty
budget =90
"""
if budget > 100:
    brand = "Nike"
    print "Yay! We can buy cool" + brand + " shoes!"
elif budget > 75:
    print "We can at least get the bootlegs"
else:
    pass

    print "No cool shoes for me."
 """

#Array

characters = ["leia","luke","chewy","lando"]
characters.append("obi won")
#print characters
#print characters[0]

#Dictionary

movies = dict() #create dictionary object
movies = {"Star Wars": "Darth Vader",
          "Silence of the Lambs":"Hannibal Lecter"}
print movies["Star Wars"]

#While Loops

i= 0
while i<9:
    #print "The While count is ", i
    i= i+1

#for loop

for i in range (0,10):
    #print "The For count is ", i
    i= i+1

#For Each loop

rappers = ["Tupac","Nas", "Biggie Smalls"]
for r in rappers:
    #print "The best rapper alive " + r
    pass

#functions


def calcArea(h,w):
    area = h * w
    print area
    return area

a = calcArea(20, 40);
#print "My area is " + str(a)

#variables into larger strings

weight = 200
height = 56
message = """
Your height is {height} and your weight is {weight}
"""
message = message.format(**locals())
print message







