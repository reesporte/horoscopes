import json
from time import sleep
import random
import tweepy
import config

"""
makes a horoscope using Mark McElroy's _A Guide to Tarot Meanings_
"""

def tweet_it(output):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    api.update_status(status=output)
    print(output)

def read_in():
    file = open('tarot_interpretations.json').read()
    data = json.loads(file)
    return data['tarot_interpretations']

def get_random_card(data):
    return random.choice(data)

def get_fortune(card):
    return random.choice(card['fortune_telling'])

def get_keyword(card):
    return random.choice(card['keywords'])

def get_light_meaning(card):
    return random.choice(card['meanings']['light'])

def get_dark_meaning(card):
    return random.choice(card['meanings']['shadow'])

def gen_scope(sign):
    data = read_in()
    card = get_random_card(data)
    fortune = get_fortune(card)
    keyword = get_keyword(card)
    light_meaning = get_light_meaning(card)
    dark_meaning = get_dark_meaning(card)

    keywords_will = [" will be important today.", " will be poignant.", " is of vital importance.", " could be important.", " may be essential."]

    horoscope = sign + ": \n" + fortune + ". " + keyword.capitalize()
    horoscope += random.choice(keywords_will) + " You have the potential to start " + light_meaning.lower()
    horoscope += ". But be careful not to end up " + dark_meaning.lower() + "."
    if len(horoscope) > 280:
        return horoscope[:280]

    return horoscope

def main():
    signs = ["Aries", "Capricorn", "Libra", "Cancer", "Leo",
            "Taurus", "Aquarius", "Scorpio", "Sagittarius",
            "Virgo", "Gemini", "Pisces"]

    for sign in signs:
        scope = gen_scope(sign)
        tweet_it(scope)
        sleep(15)


if __name__ == '__main__':
    main()
