#What is  an access token.generate your access token for any API.(for example Twitter,Spotify etc).
# An access token is an object that describes the security context of a process or thread.The information in a token includes the identity and privileges of the user account associated with the process or thread. ... The security identifier (SID) for the user's account.
# SIDs for the groups of which the user is a member.
# for example-1 twitter.com
# import tweepy
#
# consumer_key="1011130041516769282-1tnanoKiNjvWczjwBvPZOxDLeKUTKp"
# consumer_secret="BpFnOsMgFwcDdZud9UmC0nPty9Tq63SDoEZcIb6wFm28c"
# access_token='1011130041516769282-1tnanoKiNjvWczjwBvPZOxDLeKUTKp'
# access_token_secret='BpFnOsMgFwcDdZud9UmC0nPty9Tq63SDoEZcIb6wFm28c'

#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
# C:\Users\Dell>nslookup google.com
# *** Default servers are not available
# Server:  UnKnown
# Address:  127.0.0.1
#
# *** UnKnown can't find google.com: No response from server
#
# C:\Users\Dell>nslookup facebook.com
# Server:  UnKnown
# Address:  2405:200:800::1
#
# Non-authoritative answer:
# Name:    facebook.com
# Addresses:  2a03:2880:f126:83:face:b00c:0:25de
#           31.13.78.35
#
#
# C:\Users\Dell>nslookup  twitter.com
# Server:  UnKnown
# Address:  2405:200:800::1
#
# Non-authoritative answer:
# Name:    twitter.com
# Addresses:  104.244.42.129
#           104.244.42.193

#.3 - Using Tweepy library try to extract tweets from Twitter.
# 
# import tweepy
# 
# consumer_key="1011130041516769282-1tnanoKiNjvWczjwBvPZOxDLeKUTKp"
# consumer_secret="BpFnOsMgFwcDdZud9UmC0nPty9Tq63SDoEZcIb6wFm28c"
# access_token='1011130041516769282-1tnanoKiNjvWczjwBvPZOxDLeKUTKp'
# access_token_secret='BpFnOsMgFwcDdZud9UmC0nPty9Tq63SDoEZcIb6wFm28c'
# auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)
# api=tweepy.API(auth)
# n=str(input("enter any hash tag for search"))
# tweets=api.search(n,lang="en",count=10,tweet_mode="extended")
# 
# #print(tweets)
# 
# for tweet in tweets:
#     print("---------------------------------------")
#     print(tweet.full_text)
#     print("----------------------------------------")

#4 difference between  library and api


# A library is a collection of sources of information and similar resources,
# made accessible to a defined community for reference or borrowing.
#     [1] It provides physical or digital access to material, and 
#     may be a physical building or room, or a virtual space, or both.
#     [2] A library's collection can include books, periodicals, newspapers, manuscripts, ' \
#     'films, maps, prints, documents, microform, CDs, cassettes, ' \
#     'videotapes, DVDs, Blu-ray Discs, e-books, audiobooks, databases,' \
#      and other formats.
# In computer
# programming,an application programming interface(API) is a set of subroutine definitions, 
# protocols, and tools for building application software.In general terms, it is a set of
# clearly defined methods of communication between various software components.
# A good API makes it easier to develop a computer program by providing all the
# building blocks, which are then put together by the programmer.An API may be for
# a web-based system, operating system, database system, computer hardware, or software library.
# An API specification can take many forms, but often includes specifications for routines, 
# data structures, object classes, variables, or remote calls.POSIX, Windows API and ASPI are
# examples of different forms of APIs.Documentation for the API is usually provided to facilitate 
# usage and implementation.