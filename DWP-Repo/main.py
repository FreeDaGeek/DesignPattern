"""
Name: Free Rosas
Date: 7/11/2014
Assignment: MadLib
"""

print "***************************************" #put these as makers to make them easy to read
#function created for title
band = "Plain White T's"
song = "Hey There Delilah"
message = """Help me rewrite the lyrics to {song} by {band}"""
message = message.format(**locals())
print message
print "Just follow along and do as directed."
print "***************************************"#put these as makers to make them easy to read
#raw input
#this name will print ever time "delilah" is written
delilah = raw_input("Enter your FIRST name?")
nyc = raw_input("Enter a CITY name?")
yes_no = raw_input("Yes or No: Are TURTLES cute?")
print "---------------------------------------"#put these as makers to make them easy to read
print "Hey there " + delilah
print "What's it like in " + nyc
print "But babe, tonight you look so pretty"
#conditional statement / if yes: "delilah" is pretty, if no: delilah isn't
if yes_no == "Yes":
    print "Yes you do!"
    print "Times Square can't shine as bright as you"
    print "I swear it's true"
elif yes_no == "No":
    print "just kidding you really don't"
    print "Times Square can't shine as bright as you"
    print "Oh no that wasn't for you"
    print "Don't get confused"
else:
    print "Maybe you have the flu!"
    pass
#second verse
print "Second Verse-----------------------"#put these as makers to make them easy to read
print "Hey there " + delilah
'''
l1 = raw_input("Enter a noun.")
l2 = raw_input("Enter an adjective.")
print "Hey there " + delilah
print "Don't you worry about the" + l1
print "I'm right there if you get" + l2
'''
verse_two = dict()
verse_two = [
    "Don't you worry about the distance",
     "I'm right there if you get lonely",
    "Give this song another listen",
     "Close your eyes",
    "Listen to my voice, it's my disguise",
     "I'm by your side"
]

for v in verse_two:
    print v
    pass
#chorus
print "Chorus-----------------------"#put these as makers to make them easy to read
i= 0
while i<4:
    print "Oh it's what you do to me"
    i= i+1
print "What you do to me"

