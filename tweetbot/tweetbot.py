#Author: Joshua Williams
#Project Description:   This program searches two links on the internet for lists of adjectives and nouns.
#                       It then takes a random adjective and noun, and tweets (using th twitter API) them.

import tweepy
import string
import urllib
import random
#import Tkinter

#consumer_key = 'VlAA45N9wod2KgmOykGOuTM2R'
#consumer_secret = 'smb89axGD1zRjR5rempoAiDJOJKwvOegDZHhS7n1AYyEuPKPCT'
#access_token = '1129125415014952960-8ZSojFyFMcNo9FveP1VcQG7QbcOExt'
#access_token_secret = '6zpsbceKj1cJsm5fOah6rehhnvPLqIVYdxu67xk511mOt'
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

#user = api.me()
#print('Connected to twitter account: ', user.name, '\n')


print("Loading adjectives...")
link = "https://www.talkenglish.com/vocabulary/top-500-adjectives.aspx"
f = urllib.request.urlopen(link)
info = f.read()
#print(info)
index = 0
adjectives = []



############################### Adjectives #####################################

#find top of table
pos = info.find(b"<table border=\"0\" cellspacing=\"0\" cellpadding=\"0\">")
while pos != -1:
    #find where the actual word is (always preceeded by /how-to-use/)
    pos = info.find(b"<a href=\"/how-to-use/", pos)
    if pos == -1:
        break

    #move position pointer up past "<a href=" and "/how-to-use/" stuff
    pos = (info.find(b"/", pos)) + len("/how-to-use/")
    if pos == -1:
        break

    #find end of word
    end_pos = info.find(b"\"", pos)
    if end_pos == -1:
        break

    #print the word
    adjectives.append(info[pos:end_pos].decode("utf-8"))
    #print(index, ": ", adjectives[index])

    index = index + 1
    pos = end_pos



########################## Nouns ################################

print("Loading nouns...")
link = "https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx"
f = urllib.request.urlopen(link)
info = f.read()
#print(info)
index = 0
nouns = []

#################################################################

#find top of table
pos = info.find(b"<table border=\"0\" cellspacing=\"0\" cellpadding=\"0\">")
while pos != -1:
    #find where the actual word is (always preceeded by /how-to-use/)
    pos = info.find(b"<a href=\"/how-to-use/", pos)
    if pos == -1:
        break

    #move position pointer up past "<a href=" and "/how-to-use/" stuff
    pos = (info.find(b"/", pos)) + len("/how-to-use/")
    if pos == -1:
        break

    #find end of word
    end_pos = info.find(b"\"", pos)
    if end_pos == -1:
        break

    #print the word
    nouns.append(info[pos:end_pos].decode("utf-8"))
    #print(index, ": ", nouns[index])

    index = index + 1
    pos = end_pos


print("Found ", len(adjectives), " adjectives and ", len(nouns), " nouns")

#print one adjective and one noun (should be a funny possibility for a band name)
#--eventually interface with twitter API to tweet periodically or on a specific input--
again = "y"
while again != "n":
    print("\nBand Name: ", adjectives[random.randint(0,len(adjectives))], nouns[random.randint(0,len(nouns))])
    print("Again? (y/n): ")
    again = str(input())

print("Goodby World!")

