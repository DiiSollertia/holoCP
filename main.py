import praw
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

r = praw.Reddit(username = "holoCP",
                password = str(os.getenv('REDDIT_PW')),
                client_id = str(os.getenv('REDDIT_ID')),
                client_secret = str(os.getenv('REDDIT_SECRET')),
                user_agent = "holoCP by /u/holoCP")