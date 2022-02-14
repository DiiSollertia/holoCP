import praw
from dotenv import load_dotenv
import os
load_dotenv()  # loads the configs from .env

#setup
r = praw.Reddit(username = "holoCP",
                password = str(os.getenv('REDDIT_PW')),
                client_id = str(os.getenv('REDDIT_ID')),
                client_secret = str(os.getenv('REDDIT_SECRET')),
                user_agent = "holoCP by /u/holoCP")

#responds to mentions
subr = r.subreddit('sollertiadev') # this chooses a subreddit you want to get comments from
for comment in subr.stream.comments(skip_existing=True): # this iterates through the comments from that subreddit as new ones are coming in
  try:
    if "!fbkglasses" in comment.body:
        comment.reply('''[Glasses are really versatile. First, you can have glasses-wearing girls take them off and suddenly become beautiful, or have girls wearing glasses flashing those cute grins, or have girls stealing the protagonist's glasses and putting them on like, "Haha, got your glasses!" That's just way too cute! Also, boys with glasses! I really like when their glasses have that suspicious looking gleam, and it's amazing how it can look really cool or just be a joke. I really like how it can fulfill all those abstract needs. Being able to switch up the styles and colors of glasses based on your mood is a lot of fun too! It's actually so much fun! You have those half rim glasses, or the thick frame glasses, everything! It's like you're enjoying all these kinds of glasses at a buffet. I really want Luna to try some on or Marine to try some on to replace her eyepatch. We really need glasses to become a thing in hololive and start selling them for HoloComi. Don't. You. Think. We. Really. Need. To. Officially. Give. Everyone. Glasses?](https://youtu.be/DTVAjI_ELyA?t=2515)''') # this is what your bot replies to the comment that has the keyword
    if "!pekolaugh" in comment.body:
        comment.reply('''AH↗️HA↘️HA↗️HA↘️HA↗️HA↘️HA↗️HA↘️''')
    if "!pekopeko" in comment.body:
        comment.reply('''PE↗KO↘PE↗KO↘PE↗KO↘''')
    if "!guracars" in comment.body:
        comment.reply('''Hello, ma'am do you have a minute to talk about our lord and savior Lightning McQueen?! Did you know that Lightning McQueen is the star of several feature films such as Cars, Cars 2, Cars 3, Planes: Fire and Rescue, Finding Dory, Toy Story 3, Coco and Ralph breaks the internet? As well as other short film such as Master and the Ghostlight, Miss Fritter's Racing Skoool, Television program such as Cars Toons, Pixar's Popcorn Cars series voiced by none other than Owen Wilson?''')
    if "!supernenechi" in comment.body:
        comment.reply('''Nene超進化! Super Hyper Ultra Ultimate Deluxe Perfect Amazing Shining God 流派東方不敗 Master Freedom Justice Ginga Victory Prime Strong Cute Beautiful Wonderful Champion Galaxy Baby 最高 勇者王 天元突破 無限 無敵 無双 NENEMAXMAXMAXSTORONG NENECHI!''')
  except praw.exceptions.APIException: # Reddit may have rate limits, this prevents your bot from dying due to rate limits
    print("probably a rate limit...")