'''
The section below is your Twitter developer keys & tokens required for posting to your Twitter!

You must have a Twitter dev account which you can sign up for at https://developer.twitter.com/
Once signed up, apply for elevated access if you do not already have it (can be found under project one)
If accepted, go to overview (under projects & apps) and create a project.

Once you have created your app within the project scroll to user authentication settings inside the app and click set up.
Inside you must select read and write permissions (permissions) and web app, automated app or bot (type).
For the required callback/redirect URL and website URL, the URL can be anything (you can even just use your Twitter eg. https://twitter.com/swiftnite)

Once saved, navigate to keys and tokens and regenerate API key and secret, fill these out in config.py (consumerKey and consumerSecretKey respectively)
Navigate to keys and tokens again and generate Access token and secret, fill these out in config.py (accessToken and accessTokenSecret respectively)

Your app's permissions MUST have Read + Write or else it will not post!!
'''
class keys:
    consumerKey = ""
    consumerSecretKey = ""
    accessToken = ""
    accessTokenSecret = ""
'''
The below section is for the customisation of the tweet itself
'''
class customisation:
    Body: str = "was added to the staging servers!" #NOTE: This is what appears after the version that was added to staging servers in the tweet
    Footer: str = "#Fortnite" #NOTE: This is what will appear under the body! Leave blank("") if you do not want a footer
'''
If you require assistance or have suggestions you can join the Discord support server!
https://discord.gg/jHsAW2FKnj
'''