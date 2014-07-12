"""
Name: Free Rosas
Date: 7/11/2014
Assignment: MadLib
"""
'''
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
#conditional statement(non-logical operator) / if yes: "delilah" is pretty, if no: delilah isn't
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
#array
verse_two = [
    "Don't you worry about the distance",
     "I'm right there if you get lonely",
    "Give this song another listen",
     "Close your eyes",
    "Listen to my voice, it's my disguise",
     "I'm by your side"
]
#for loop
for v in verse_two:
    print v
    pass
#chorus
chorus = 3 #declaring variable
print "Chorus-----------------------"#put these as makers to make them easy to read
#if statement w/ math operations
if chorus < 3:
    #while loop to create chorus
    i= 0
    while i<4:
        print "Oh it's what you do to me"
    i= i+1
    print "What you do to me"
else:
    print "You not ready?? WHY NOT!"


print "Third Verse------------------------"
#dictionary
hard = raw_input("Enter a texture?")
honey = raw_input("Enter a word that rhymes with funny?")
someday = raw_input("Enter a word that rhymes with sunday?")
guitar = raw_input("Enter any instrument.")
verse_three = dict()
verse_three = {"0": "I know times are getting ",
               "1": "But just believe me, ",
               "2": " I'll pay the bills with this ",
               "3": "We'll have it good",
               "4": "We'll have the life we knew we would",
               "5": "My word is good"}
print"***************************************"
print "Hey there " + delilah
print verse_three[str(0)] + hard
print verse_three[str(1)] + honey
print someday + verse_three[str(2)] + guitar
print verse_three[str(3)]
print verse_three[str(4)]
print verse_three[str(5)]

print"***************************************"
'''

#print "Hey there " + delilah
l1 ="I've got so much left to say"
print len(l1)
l2 = "If every simple song I wrote to you"
print len(l2)
l3 = "Would take your breath away"
print len(l3)
l4 = "I'd write it all"
print len(l4)
l5 = "Even more in love with me you'd fall"
print len(l5)
l6 = "We'd have it all"
print len(l6)
l_total = len(l5) + len(l4) +len(l3)+ len(l2)+ len(l1)
print l_total
