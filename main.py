try:
    from requests import get
except:
    print("The requests module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install requests")
    sleep(10)
    exit()

try:
    import tweepy
except:
    print("The tweepy module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install tweepy")
    sleep(10)
    exit()

import json
from time import sleep
from config import keys, customisation

consumerKey = keys.consumerKey
consumerSecretKey = keys.consumerSecretKey
accessToken = keys.accessToken
accessTokenSecret = keys.accessTokenSecret

if not all((consumerKey, consumerSecretKey, accessToken, accessTokenSecret)):
    print('WARNING!!!\nYou have not entered your Twitter Api keys into the config.py file!\nThis bot CANNOT run unless you enter these keys!!')
    sleep(10)
    exit()

auth = tweepy.OAuthHandler(consumerKey, consumerSecretKey)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

client = tweepy.Client(consumer_key=consumerKey,
        consumer_secret=consumerSecretKey,
        access_token=accessToken,
        access_token_secret=accessTokenSecret)

try:
    account = api.verify_credentials(skip_status=True,include_email=False)
    hi = json.dumps(account._json)
    hi = json.loads(hi)
    twitter_tag = hi['screen_name']
    user = hi['name']
except Exception as e:
    print(f'An error occurred verifying your api keys! Are they correct?\n{e}')

Body = customisation.Body
Footer = customisation.Footer

if Footer!="":
    Footer = f"\n\n{Footer}"

print(f"\nWelcome {user} to SwiftNite's staging servers bot!\n\nFeel free to follow me on twitter -> @SwiftNite\nUse code Swift-Nite in Fortnite and the Epic Games Store to support me and this staging servers bot!\n\n\nThe bot is now looking for changes to the staging servers!\n")

def main():
    try:
        stage = get('https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version').json()['version']
        
        with open('cache.json', 'r') as cache:
            cache = json.load(cache)

        if cache != stage:
            text = f"V{stage} {Body}{Footer}"

            print(f"\n{text}\n")
            client.create_tweet(text = text)

            print('Posted Staging Servers Update!')

            with open('cache.json', 'w') as cahe:
                json.dump(stage, cahe, indent=3)
    except Exception as e:
        print(f"An error has occured checking for staging server updates!\n{e}")


if __name__ == "__main__":
    while True:
        main()
        sleep(15)
