import subprocess
import sys
import json
from config import Twitter, Customisation
from time import sleep

def install(package):
    # credit: https://stackoverflow.com/a/50255019
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        pass

def ensure_package_installed(package_name):
    """Ensures that a package is installed, installing it if necessary."""
    try:
        __import__(package_name)  # Attempt to import the package
        return
    except ImportError:
        print(f"The {package_name} module is not installed. Attempting to install...")
        install(package_name)
    try:
        __import__(package_name)  # Try to import again after installation
        return
    except ImportError as e:
        module = str(e).split()[3]  # Extracts the module name from the error
        print(f"The {module} module is not installed and could not be installed automatically!\n" +
                "Please run install.bat before running the bot\n" +
                f"Alternatively, you can open command prompt and enter `pip install {module}`")
        sleep(10)
        exit()

ensure_package_installed("requests")
from requests import get
ensure_package_installed("tweepy")
import tweepy

posting = Twitter.tweetEnabled
if not isinstance(posting, bool):
    print("postingEnabled in your config.py must either be set to True or False!")
    sleep(10)
    exit()

def getUser():
    with open('cache.json', 'r') as cachFile:
        cache = json.load(cachFile)
    return cache["user"]

if posting:
    # Updates the username in cache (less api calls on startup)
    def updateUser(user: str):
        with open('cache.json', 'r+') as cacheFile:
            cache = json.load(cacheFile)
            if cache["user"] != user:
                cache["user"] = user
                cacheFile.seek(0)  # Move to the start of the file to overwrite
                json.dump(cache, cacheFile, indent=3)
                cacheFile.truncate()  # Remove any leftover data

    consumerKey = Twitter.consumerKey
    consumerSecretKey = Twitter.consumerSecretKey
    accessToken = Twitter.accessToken
    accessTokenSecret = Twitter.accessTokenSecret

    if not all((consumerKey, consumerSecretKey, accessToken, accessTokenSecret)):
        print('\n\nYou have not entered your Twitter Api keys into the config.py file and tweeting is enabled!\n')
        # Means we need to revalidate keys if they were previously ok
        updateUser(None)
        print("You will be asked to input 4 different twitter api keys! See the github readme for more details.\n")
        print("Navigate to keys and tokens and regenerate API key and secret")
        consumerKey = input("Enter your API key: ")
        consumerSecretKey = input("Enter your API secret key: ")
        print("\nNavigate to keys and tokens again and generate Access token and secret")
        accessToken = input("Enter your access token: ")
        accessTokenSecret = input("Enter your access token secret: ")
        with open("config.py", "r+") as file:
            f = file.read()
            f = f.replace('consumerKey = ""', f'consumerKey = "{consumerKey}"')
            f = f.replace('consumerSecretKey = ""', f'consumerSecretKey = "{consumerSecretKey}"')
            f = f.replace('accessToken = ""', f'accessToken = "{accessToken}"')
            f = f.replace('accessTokenSecret = ""', f'accessTokenSecret = "{accessTokenSecret}"')
            file.seek(0)  # Move to the start of the file to overwrite
            file.write(f)
            file.truncate()  # Remove any leftover data
        print("\nYour api keys have now been saved!")

    # Api V1
    auth = tweepy.OAuthHandler(consumerKey, consumerSecretKey)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

    # Api V2
    client = tweepy.Client(consumer_key=consumerKey,
            consumer_secret=consumerSecretKey,
            access_token=accessToken,
            access_token_secret=accessTokenSecret)
    
    if not getUser():
        try:
            account = api.verify_credentials(skip_status=True,include_email=False)
            hi = json.dumps(account._json)
            hi = json.loads(hi)
            twitter_tag = hi['screen_name']
            user = hi['name']
            updateUser(user)
        except Exception as e:
            print(f'An error occurred verifying your api keys! Are they correct?\n{e}')
            sleep(10)
            exit()
    else:
        user = getUser()
elif getUser():
    user = getUser()
else:
    user = ""

print(f"\n\nWelcome {user} to SwiftNite's staging servers bot!\n\n"+
        "Feel free to follow me on twitter -> @SwiftNite\n"+
        "Use code Swift-Nite in Fortnite and the Epic Games Store to support me and this staging servers bot!\n\n\n"+
        "The bot is now looking for changes to the staging servers!\n"+
        f"Posting enabled: {posting}\n")
        

body = Customisation.Body
footer = Customisation.Footer

# Adds two new lines between main area and footer
if footer:
    footer = f"\n\n{footer}"

def main():
    try:
        stageUrls = [
            "https://fngw-mcp-ds-predeployb-prod.ol.epicgames.com/fortnite/api/version",
            "https://fngw-mcp-ds-consolecerta-prod.ol.epicgames.com/fortnite/api/version",
            "https://fngw-mcp-ds-consolecertb-prod.ol.epicgames.com/fortnite/api/version",
        ]

        with open('cache.json', 'r') as cache:
            cache = json.load(cache)

        stageMax = cache["version"]
        for url in stageUrls:
            try:
                stage = get(url).json()['version']
                if float(stage) > float(stageMax):
                    stageMax = stage
            except:
                pass # Sometimes a url may not respond and tbh idrc
        if float(stageMax) > float(cache["version"]):
            cache["version"] = stageMax 

            text = f"V{cache['version']} {body}{footer}"

            print(f"\n{text}\n")
            if posting:
                client.create_tweet(text = text)
                # This needs to be in the if statement, Don't want to scare users :0
                print('Posted Staging Servers Update!')

            with open('cache.json', 'w') as cahe:
                json.dump(cache, cahe, indent=3)
    except Exception as e:
        print(f"An error has occured checking for staging server updates!\n{e}")


if __name__ == "__main__":
    while True:
        main()
        sleep(15)