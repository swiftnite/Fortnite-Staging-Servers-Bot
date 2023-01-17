'''
The section below is your Twitter developer keys & tokens required for posting to your Twitter!

You must have a Twitter dev account which you can sign up for at https://developer.twitter.com/
Once signed up, apply for elevated access if you do not already have it (can be found under project one)
If accepted, go to overview (under projects & apps) and create a standalone app (The name of the app may be used as the source of the tweet eg. Twitter for iPhone)

Once created scroll to user authentication settings and click set up.
Inside you must select read and write permissions (permissions) and web app, automated app or bot (type).
For the required callback/redirect URL and website URL, the URL can be anything (you can even just use your Twitter eg. https://twitter.com/swiftnite)

Once saved, navigate to keys and tokens and regenerate API key and secret, fill these out in config.py (consumer_key and consumer_secret_key)
Navigate to keys and tokens again and generate Access token and secret, fill these out in config.py (access_token and access_token_secret)

Your app's permissions must have Read + Write or else it will not post!!
'''
class keys:
    consumer_key = ""
    consumer_secret_key = ""
    access_token = ""
    access_token_secret = ""
'''
The below section is for the customisation of the tweet itself
'''
class customisation:
    Body: str = "was added to the staging servers!" #NOTE: This is what appears after the version that was added to staging servers in the tweet
    Footer: str = "#OK" #NOTE: This is what will appear under the body! Leave blank("") if you do not want a footer
'''
If you have any issues please message me on Discord or Twitter and I will respond as quickly as possible!!
Twitter: @SwiftNite
Discord: Swift-nite#9078
'''
