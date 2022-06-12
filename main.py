import praw
import prawcore.exceptions
import os

#from dotenv import load_dotenv
#load_dotenv()  # loads the configs from .env for local dev

print('import done')

#setup
r = praw.Reddit(username = "holoquote_bot",
                password = os.environ['REDDIT_PW'],
                client_id = os.environ['REDDIT_ID'],
                client_secret = os.environ['REDDIT_SECRET'],
                user_agent = "Windows-10:holoquote_bot:v1 (by /u/holoquote_bot)",
                ratelimit_seconds = 300,
                )

print('setup done')

footer = "\n\n"+"---"+"\n\n_I am a copypasta bot. [Documentation here](https://github.com/DiiSollertia/holoquote_bot#readme)_"

#responds to mentions
subr = r.subreddit('testingground4bots+test+hololive') # this chooses a subreddit you want to get comments from
for comment in subr.stream.comments(skip_existing=True): # this iterates through the comments from that subreddit as new ones are coming in
    try:
        print('iterate')
        if "!fbkglasses" in comment.body:
            comment.reply('''[Glasses are really versatile. First, you can have glasses-wearing girls take them off and suddenly become beautiful, or have girls wearing glasses flashing those cute grins, or have girls stealing the protagonist's glasses and putting them on like, "Haha, got your glasses!" That's just way too cute! Also, boys with glasses! I really like when their glasses have that suspicious looking gleam, and it's amazing how it can look really cool or just be a joke. I really like how it can fulfill all those abstract needs. Being able to switch up the styles and colors of glasses based on your mood is a lot of fun too! It's actually so much fun! You have those half rim glasses, or the thick frame glasses, everything! It's like you're enjoying all these kinds of glasses at a buffet. I really want Luna to try some on or Marine to try some on to replace her eyepatch. We really need glasses to become a thing in hololive and start selling them for HoloComi. Don't. You. Think. We. Really. Need. To. Officially. Give. Everyone. Glasses?](https://youtu.be/DTVAjI_ELyA?t=2515)'''+footer)
        if "!pekolaugh" in comment.body:
            comment.reply('''AH↗️HA↘️HA↗️HA↘️HA↗️HA↘️HA↗️HA↘️'''+footer)
        if "!pekopeko" in comment.body:
            comment.reply('''PE↗KO↘PE↗KO↘PE↗KO↘'''+footer)
        if "!guracars" in comment.body:
            comment.reply('''[Hello, ma'am do you have a minute to talk about our lord and savior Lightning McQueen?! Did you know that Lightning McQueen is the star of several feature films such as Cars, Cars 2, Cars 3, Planes: Fire and Rescue, Finding Dory, Toy Story 3, Coco and Ralph breaks the internet? As well as other short film such as Master and the Ghostlight, Miss Fritter's Racing Skoool, Television program such as Cars Toons, Pixar's Popcorn Cars series voiced by none other than Owen Wilson?](https://youtu.be/vci-RuRSios?t=6175)'''+footer)
        if "!supernenechi" in comment.body:
            comment.reply('''Nene超進化! Super Hyper Ultra Ultimate Deluxe Perfect Amazing Shining God 流派東方不敗 Master Freedom Justice Ginga Victory Prime Strong Cute Beautiful Wonderful Champion Galaxy Baby 最高 勇者王 天元突破 無限 無敵 無双 NENEMAXMAXMAXSTORONG NENECHI!'''+footer)
        if "!phoenix" in comment.body:
            comment.reply('''# To those coming from r/all:  '''+'''\n\nHello! Welcome to the official subreddit for hololive production (wikipedia), a talent agency based out of Tokyo, Japan that manages Virtual YouTubers - think of streamers on Twitch and YouTube, but with virtual avatars instead of a facecam. Most of the talents in Hololive are Japanese, but there are also Indonesian and English branches too! The talents do all sorts of stuff, including but not limited to: gaming streams, karaoke streams, drawing streams and talking streams. Some of the content the talents offer is family friendly, others a bit more risque. The sidebar has links to each talent's Youtube and Twitter accounts.'''+footer)
        if "!faq" in comment.body:
            comment.reply('''[FAQ IS LOVE!](https://youtu.be/T142Djb4Jbw?t=5982)'''+footer)
        if "!hey" in comment.body:
            comment.reply('''[hey!  ](https://youtu.be/aD_niqW7BPM?t=2104)'''+'''\n\n [moona come on!!!!](https://youtu.be/aD_niqW7BPM?t=2104)'''+footer)
        if "!apex" in comment.body:
            comment.reply('''[^(DID SOMEBODY SAY)](https://youtu.be/VemenskFoBk)'''+'''\n\n [**APEX?!**](https://youtu.be/VemenskFoBk)'''+footer)
        if "!when" in comment.body:
            comment.reply('''# [TOMORROW!](https://youtu.be/EHpxi7khHb0?t=3005)'''+'''\n\n [*said Ina calmly.*](https://youtu.be/EHpxi7khHb0?t=3005)'''+footer)
        if "!piratebooty" in comment.body:
            comment.reply('''>"I don't think you would understand this. But my butt is really big, it's like "What happened to this?" To explain just how big it is. If I were to take a fall that would break a normal person's bones my butt will absorb all the damage. My bones would be completely fine. It will only end with a single bruise. My butt is the absolute strongest. It's very sturdy, the muscle is so thick. To explain just how thick it is... In my head, I think of myself as having a hitbox and I walk based on that. But while I walk, my butt sways left and right. It's not like it's swaying because I'm trying to shake it. It's just so big it moves on its own and it just becomes a shaky mess. I don't intend to shake it, I don't mean to walk like a penguin. But it's just so big my body is taken along for the ride. And my body is shaken around by my butt. So, then my hitbox gets misaligned so I start banging into things. Like I think I can get through here, but my butt goes BOOM! And you might think it hurts and that's that but my butt is so much like a cushion but it bounces and sends me flying. I think ...it's like that, it's just that bouncy it has its own hitbox. Then there's what happens in bed. You might not understand because you're boys, but when a woman with a butt as big as mine goes to bed, when I lay down my butt is so big my hips start floating. Understand???"'''+ '''  \n\n[Houshou Marine, 2021](https://youtu.be/OPrh4Wu9TmU?t=2205)''')
    except praw.exceptions.RedditAPIException:
        print("API Exception: Probably rate limit")
    except prawcore.exceptions.ResponseException:
        print("Response Exception: Probably HTTP 401 Authentication Error")
    except:
        print("Unknown Error")