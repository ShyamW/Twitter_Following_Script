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
    file containing one collumn of company twitter handles
        ex: @company123
            @company124
@returns companies
    list of companies to follow"""
def readFile(file_name):
    with open (file_name) as f:
        companies = f.read().splitlines()
    return companies


"""Follows compananies on Twitter
@param companies
    list of companies to follow
@param api
    authenticated api object"""
def follow(companies, api):
    progress = 1
    for utility_company in companies:
        api.create_friendship(utility_company)
        print(str(progress) + 'of' + str(len(companies)))
        progress += 1


"""Main Method"""
def main():
    api = loginToTwitter()
    companies = readFile('handles.txt')
    follow(companies, api)


main()
