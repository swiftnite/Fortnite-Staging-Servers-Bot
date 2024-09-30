# Fortnite Staging Servers Bot
A Fortnite staging servers bot that posts to twitter as soon as a new version is added! 

## Example
<p align="center">
    <img src="https://github.com/user-attachments/assets/a1090990-c976-4b76-8af7-dfaedfbe6771">
</p>


## Requirements
- Python MUST be **installed** and **added to PATH**
<p align="center">
    <img src="https://user-images.githubusercontent.com/74127135/212615961-10c507f5-01de-483a-914b-3270109cdb2b.png"><br>
    <sub><sup>Image via <a href="https://medium.com/@omoshalewa/why-you-should-add-python-to-path-and-how-58693c17c443">medium.com</a></sub></sup>
 </p>
 
- Twitter Developer Account (Need help getting started? [Watch this basic guide](https://user-images.githubusercontent.com/74127135/212822054-c886df92-72bf-4749-8011-1f8e4f67a4ac.mp4) or [Follow along with the in text guide](#twitter-developer-account-setup))

## Getting Started
- [Download](https://github.com/swiftnite/Fortnite-Staging-Servers-Bot/archive/refs/heads/main.zip) and extract the Bot.
- Open the **config.py** file inside a text editor of your choice (Visual studio code is recommended) and fill in all required fields
- Start the bot by opening **run.bat**!!

If the bot cannot automatically install requirement then:
- Run **install.bat**! 
- If the install does not work then:
Open command prompt and enter each line:
~~~
pip install tweepy
pip install requests
~~~
Alternatively: 
~~~
pip3 install tweepy
pip3 install requests
~~~

## Assistance & Suggestions
If you require assistance or have suggestions you can:
- [Join the Discord support server](https://discord.gg/jHsAW2FKnj)
- [Message me on Twitter](https://twitter.com/intent/follow?screen_name=SwiftNite)

## Support Project
If you enjoy my staging servers bot then you can follow me on [Twitter](https://twitter.com/intent/follow?screen_name=SwiftNite)!

If you would like to further support me and the staging servers bot then consider donating through buy me a coffee below!

<p align="center">
    <a href="https://www.buymeacoffee.com/Swiftnite"><img width="300" alt="bmc-button" src="https://user-images.githubusercontent.com/74127135/233548032-c051ea07-9f03-43e3-a4d1-bfaced2e41db.png"></a>
</p>
<br>

Also consider using my support-a-creator code **Swift-Nite** in the Fortnite item shop or for any other Epic Games Store purchases!
<br>
In connection with Epic Games’ Support-A-Creator Program, I may receive payouts from your in-game purchases.

I much appreciate all support!

## Twitter Developer Account Setup
You must have a Twitter developer account which you can sign up for at https://developer.twitter.com/
Once signed up, apply for elevated access if you do not already have it (can be found under project one)
If accepted, go to overview (under projects & apps) and create a project.

Once you have created your app within the project scroll to user authentication settings inside the app and click set up.
Inside you must select read and write permissions (permissions) and web app, automated app or bot (type).
For the required callback/redirect URL and website URL, the URL can be anything (you can even just use your Twitter eg. ```https://twitter.com/swiftnite```)

Once saved, navigate to keys and tokens and regenerate API key and secret, fill these out in ```config.py``` (consumerKey and consumerSecretKey respectively)
Navigate to keys and tokens again and generate Access token and secret, fill these out in ```config.py``` (accessToken and accessTokenSecret respectively)

Your app's permissions **MUST** have **Read + Write** or else it will not post!!

## Project Credits
Bot Created by [Swift-Nite](https://twitter.com/intent/follow?screen_name=SwiftNite)
