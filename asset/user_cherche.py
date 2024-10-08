
import requests
def main():
    user_or_name = input("username or name : ")
    url =[ "https://www.facebook.com/profile.php?id=",        # Facebook (User ID)
    "https://www.instagram.com/",                      # Instagram (Username)
    "https://twitter.com/",                            # Twitter/X (Username)
    "https://www.linkedin.com/in/",                    # LinkedIn (Username)
    "https://github.com/",                             # GitHub (Username)
    "https://www.pinterest.com/",                      # Pinterest (Username)
    "https://www.reddit.com/user/",                    # Reddit (Username)
    "https://www.tiktok.com/@",                        # TikTok (Username)
    "https://www.tumblr.com/blog/",                    # Tumblr (Username)
    "https://www.twitch.tv/",                          # Twitch (Username)
    "https://www.youtube.com/c/",                      # YouTube (Channel Username)
    "https://medium.com/@",                            # Medium (Username)
    "https://www.flickr.com/people/",                  # Flickr (User ID)
    "https://soundcloud.com/",                         # SoundCloud (Username)
    "https://www.behance.net/",                        # Behance (Username)
    "https://vimeo.com/",                              # Vimeo (Username)
    "https://www.deviantart.com/",                     # DeviantArt (Username)
    "https://www.quora.com/profile/",                  # Quora (Username)
    "https://www.goodreads.com/user/show/",            # Goodreads (User ID)
    "https://www.producthunt.com/@",                   # Product Hunt (Username)
    "https://angel.co/u/",                             # AngelList (Username)
    "https://www.vk.com/",                             # VK (Username or User ID)
    "https://www.meetup.com/members/",                 # Meetup (User ID)
    "https://ello.co/",                                # Ello (Username)
    "https://www.couchsurfing.com/people/",            # Couchsurfing (Username)
    "https://500px.com/",                              # 500px (Username)
    "https://www.strava.com/athletes/",                # Strava (Athlete ID)
    "https://www.mixcloud.com/",                       # Mixcloud (Username)
    "https://ok.ru/profile/",                          # Odnoklassniki (OK.ru) (User ID)
    "https://about.me/",                               # About.me (Username)
    "https://www.roblox.com/users/",                   # Roblox (User ID)
    "https://my.playstation.com/",                     # PlayStation Network (Username)
    "https://steamcommunity.com/id/",                  # Steam (Custom URL or SteamID)
    "https://www.epicgames.com/id/",                   # Epic Games (Username)
    "https://www.xboxgamertag.com/search/",            # Xbox (Gamertag)
    "https://battle.net/username/",                    # Battle.net (Username)
    "https://us.battle.net/sc2/en/profile/",           # StarCraft II (Profile URL)
    "https://www.uplay.com/",                          # Ubisoft Uplay (Username)
    "https://socialclub.rockstargames.com/member/",    # Rockstar Social Club (Username)
    "https://www.nintendo.com/switch/family/",         # Nintendo Switch (Profile)
    "https://www.chess.com/member/",                   # Chess.com (Username)
    "https://lichess.org/@/",                          # Lichess (Username)
    "https://letterboxd.com/",                         # Letterboxd (Username)
    "https://www.speedrun.com/user/",                  # Speedrun.com (Username)
    "https://osu.ppy.sh/users/",                       # Osu! (User ID)
    "https://www.geocaching.com/profile/?u=",          # Geocaching (Username)
    "https://www.anilist.co/user/",                    # AniList (Username)
    "https://myanimelist.net/profile/",                # MyAnimeList (Username)
    "https://kitsu.io/users/",                         # Kitsu (Username)
    "https://boardgamegeek.com/user/",                 # BoardGameGeek (Username)
    "https://www.furaffinity.net/user/",               # FurAffinity (Username)
    "https://scratch.mit.edu/users/",                  # Scratch (Username)
    "https://www.hackerrank.com/",                     # HackerRank (Username)
    "https://codeforces.com/profile/",                 # Codeforces (Username)
    "https://leetcode.com/",                           # LeetCode (Username)
    "https://www.hackerearth.com/@",                   # HackerEarth (Username)
    "https://devpost.com/",                            # Devpost (Username)
    "https://dribbble.com/",                           # Dribbble (Username)
    "https://www.artstation.com/",                     # ArtStation (Username)
    "https://www.polywork.com/",                       # Polywork (Username)
    "https://mastodon.social/@",                       # Mastodon (Username)
    "https://disqus.com/by/",                          # Disqus (Username)
    "https://replit.com/@",                            # Replit (Username)
    "https://itch.io/profile/",                        # Itch.io (Username)
    "https://stackexchange.com/users/",                # Stack Exchange (User ID)
    "https://stackoverflow.com/users/",                # Stack Overflow (User ID)
    "https://www.sporcle.com/user/",                   # Sporcle (Username)
    "https://kongregate.com/accounts/",                # Kongregate (Username)
    "https://www.giantbomb.com/profile/",              # Giant Bomb (Username)
    "https://www.newgrounds.com/portal/view/",         # Newgrounds (Username)
    "https://runescape.wiki/w/",                       # RuneScape (Username)
    "https://classic.wowhead.com/user/",               # Wowhead (Username)
]
    for url_list in url :
        print("url: " + url_list )
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            response = requests.get(url_list + user_or_name, timeout=10, headers=headers)
            urls = url_list + user_or_name 

            if response.status_code == 200:
                print("HERE -->:" + urls) 
            elif response.status_code == 404 or 403:
                print(f"user or person not found in {url_list} + {response.status_code}")
            else:
                print(f"Erreur: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la connexion à {url_list}: {e}")
        
main()