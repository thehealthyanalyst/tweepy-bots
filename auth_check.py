#tutorial - https://realpython.com/twitter-bot-python-tweepy/

import tweepy
auth = tweepy.OAuthHandler("kpKdIMmLTCyss12TnqnalI8Es", 'xBKplApGjCjaxUFce0Yb41KvbG9aCyRUuanlrl5pT2AMGi3qMh')
auth.set_access_token('926438084849254400-tQALEXZh2w9t2nQhXgD1VsvRMD7zdOL','61x35SwQ4PYELa1lH3mOlrBgrCWN3i1ffGMOCmh699FN4')

#Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#Setting wait_on_rate_limit and wait_on_rate_limit_notify to True makes the API object print a message and wait if the rate limit is exceeded:

user = api.get_user('SoumyaG101')

print('User details:')
print(user.name)
print(user.description)
print(user.location)
#try:
    #api.verify_credentials()
    #print("Authentication OK")
#except:
    #print("Error during Authentication")
