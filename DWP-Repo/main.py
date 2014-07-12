"""
Name: Free Rosas
Date: 7/11/2014
Assignment: MadLib
"""

#function created for title
band = "Plain White T's"
song = "Hey There Delilah"
message = """Help me rewrite the lyrics to {song} by {band}"""
message = message.format(**locals())
print message
print "Just follow along and do as directed."

#raw input
#this name will print ever time "delilah" is written
delilah = raw_input("Enter your FIRST name?")
nyc = raw_input("Enter a CITY name?")
yes_no = raw_input("Yes or No: Are TURTLES cute?")
print "---------------------------------------"
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
print "Hey there " + delilah


