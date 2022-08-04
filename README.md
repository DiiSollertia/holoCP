# holoquote_bot
Reddit bot for hololive-related copypastas

# Background
As a fellow community member, I have realized that there are a couple of bots that modified messages (_think peko or nanora_) or posted copypastas based on keywords in posts (_like the fubuki glasses bot_). However, I wanted to create something that could be summoned on demand (_via commands_) and had an extensive list of responses instead of a specific one, which led me to write this script.

# Current Configuration

| Parameters          | Values                       |
|---------------------|------------------------------|
| Language            | Python                       |
| Hosting Platform    | Heroku                       |
| Max Ratelimit       | 300 seconds                  |
| Dynohours           | 1000 hours/month             |

## Subreddit Whitelist
- r/testingground4bots
- r/test  
- r/hololive  
_This list can be expanded. While I prefer to message mods for approval first to avoid stepping on toes, it seems like I'm not getting any productive responses. [Contact me](#Contact) to suggest more subreddits that this bot would be useful in._

## Subreddit Blacklist
| Subreddit  | Reason                                                       |
|------------|--------------------------------------------------------------|
| r/Hololewd | Permabanned during approval request, no reason given to date |

# Main Script

## Available Commands
- `!phoenix`
- `!fbkglasses`
- `!guracars`
- `!pekopeko`
- `!pekolaugh`
- `!supernenechi`
- `!faq`
- `!hey`
- `!apex`
- `!when`
- `!piratebooty`

Detailed command descriptions [here](https://github.com/DiiSollertia/holoquote_bot/blob/main/main-script/README.md).

# Contact 
To contact me or submit suggestions, please report and issue via Github if you're comfortable with it or submit this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdQU66HN6aAVZjk7LNFqz8F0duhE_-wHRTVtN6wziMX9Aov5Q/viewform?usp=sf_link).

# Support 
Running and maintaining Reddit bots 24/7 requires hosting fees. To support me and/or this project, feel free to contribute using the following platforms. If you wish for 100% of your contribution to go towards this specific project (hosting fees and such), please do specify so in the _message_ sections available.
- [Ko-fi](https://ko-fi.com/sollertia)
- [Stream Elements](https://streamelements.com/sollertia_/tip)

# Future direction
- React to good bot/bad bot replies
- More extensive commands
- More robust system to handle rate limits
