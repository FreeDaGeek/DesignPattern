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
#declaring variable
print "Chorus-----------------------"#put these as makers to make them easy to read
#for statement w/ math operations
chorus = 5
if chorus > 3:
    for i in range(0, 4):
        print "Oh it's what you do to me"
        i = i + 1
else:
    print "You not ready?? WHY NOT!"
    pass
print "What you do to me"




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

print "Hey there " + delilah
print "I've got so much left to say"
print "If every simple song I wrote to you"
print "Would take your breath away"
print "I'd write it all"
print "Even more in love with me you'd fall"
print "We'd have it all"

print"***************************************"
#fuctions to state how repetative the chorus is
def count(l, c):
    total = l / c
    #print total
    return total
a = count(8, 2)
print "This chorus says one line 8 time in the whole song!"
print "With two chorus sections, they sang it " + str(a) + " times each chorus!"
print "Look for you self!"

print "Chorus-----------------------"
#for statement w/ math operations
chorus = 5
if chorus > 3:
    for i in range(0, 4):
        print "Oh it's what you do to me"
        i = i + 1
else:
    print "You not ready?? WHY NOT!"
    pass
print "What you do to me"

print "********************************************"
final_lines = 10
if final_lines < 20:
    print "A thousand miles seems pretty far"
    print "But they've got planes and trains and cars"
    print "I'd walk to you if I had no other way"
    print "Our friends would all make fun of us"
    print "And we'll just laugh along because we know"
    print "That none of them have felt this way"
    print "Delilah I can promise you"
    print "That by the time we get through"
    print "The world will never ever be the same"
    print "And you're to blame"
else:
    pass
print"----------------------------------------------"


#variable deceleration
first_line = "A thousand miles seems pretty far"
second_line = "But they've got planes and trains and cars"
third_line ="I'd walk to you if I had no other way"
fourth_line ="Our friends would all make fun of us"
fifth_line ="And we'll just laugh along because we know"
sixth_line = "That none of them have felt this way"
seventh_line = "Delilah I can promise you"
eighth_line = "That by the time we get through"
ninth_line = "The world will never ever be the same"
tenth_line = "And you're to blame"



