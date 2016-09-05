import tweepy
"""Follows twitter handles stored in handles.txt
@author Shyam Thiagarajan
"""


"""Logs in to Twitter using api codes
@return api
    authenticated api object
"""
def loginToTwitter():
    consumer_key = ''
    consumer_secret = ''
    key = ''
    secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    return api


"""Stores handles into @code companies
@param file_name
    file containing one collumn of twitter handles
        ex: @handle1234
            @handle1235
@returns handles
    list of handles to follow"""
def readFile(file_name):
    with open (file_name) as f:
        handles = f.read().splitlines()
    return handles


"""Follows handles on Twitter
@param companies
    list of handles to follow
@param api
    authenticated api object"""
def follow(handles, api):
    progress = 1
    for handle in handles:
        api.create_friendship(handle)
        print(str(progress) + 'of' + str(len(handles)))
        progress += 1


"""Main Method"""
def main():
    api = loginToTwitter()
    handles = readFile('handles.txt')
    follow(handles, api)


main()
