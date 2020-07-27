from modules.printutils import *
import json

big_banner("""
    Spotify Playlist Using DICTS
""")

# ----------------------------------------
banner("""
    Solution 0:
    Just created the DICT completely manually.
""")

playlist = {
    "title": "Patagonia Bus",
    "author": "Colt Steele",
    "songs": [
        {
            "track": 1,
            "title": "Turn It Off",
            "artist": "Culture Abuse",
            "album": "Peach",
            "date_added": "2017-10-31",
            "runtime": "3:37"
        },
        {
            "track": 2,
            "title": "Eating Hooks - Siriusmo Remix - Solomun Edit",
            "artist": "Moderat Siriusmo Solomun",
            "album": "Eating Hooks (Siriusmo Remix - Solomun Edit)",
            "date_added": "2017-11-06",
            "runtime": "7:02"
        }
    ]
}

print(json.dumps(playlist, indent=2))


# ----------------------------------------
playlist = []

banner("""Solution 1:
    Manually add tracks using append(). Sure it
    works but why, it's just long.
""")

playlist.append({
    "track": 1,
    "title": "Turn It Off",
    "artist": "Culture Abuse",
    "album": "Peach",
    "date_added": "2017-10-31",
    "runtime": "3:37"
})
playlist.append({
    "track": 2,
    "title": "Eating Hooks - Siriusmo Remix - Solomun Edit",
    "artist": "Moderat Siriusmo Solomun",
    "album": "Eating Hooks (Siriusmo Remix - Solomun Edit)",
    "date_added": "2017-11-06",
    "runtime": "7:02"
})

print(json.dumps(playlist, indent=2))


# ----------------------------------------
playlist.clear()
banner("""Solution 2:
    Setup a dict of raw data ahead of time, then
    loop through it to populate the tracklist.
    Not gaining much here, too much code.
""")

data = {
    "titles": [
        "Turn It Off",
        "Eating Hooks - Siriusmo Remix - Solomun Edit",
        "Nights Off",
        "Tilted",
        "Don't Stop",
    ],
    "artists": [
        "Culture Abuse",
        "Moderat Siriusmo Solomun",
        "Siriusmo",
        "Christine and the Queens",
        "Knightlife",
    ],
    "albums": [
        "Peach",
        "Eating Hooks (Siriusmo Remix - Solomun Edit)",
        "Mosaik",
        "Tilted (Paradis Remix)",
        "Cut Copy Presents: Oceans Apart",
    ],
    "date_addeds": [
        "2017-10-31",
        "2017-11-06",
        "2017-11-06",
        "2017-11-06",
        "2017-11-06",
    ],
    "runtimes": [
        "3:37",
        "7:02",
        "4:08",
        "5:50",
        "6:13",
    ]
}

for t in range(0, len(data["titles"])):
    playlist.append({
        "track": t+1,
        "title": data.get('titles')[t],
        "artist": data.get('artists')[t],
        "album": data.get('albums')[t],
        "date_added": data.get('date_addeds')[t],
        "runtime": data.get('runtimes')[t]
    })

print(json.dumps(playlist, indent=2))

# ----------------------------------------
playlist.clear()
banner("""
    Solution 3:
    This one makes the most sense, the separation of
    data and logic. That being said, it uses the 
    json library, a json file, and file io that 
    we haven't learned yet to this point in the 
    course.
""")

with open("tracks.json", "r") as read_file:
    data = json.load(read_file)

for t in range(0, len(data["titles"])):
    playlist.append({
        "track": t+1,
        "title": data.get('titles')[t],
        "artist": data.get('artists')[t],
        "album": data.get('albums')[t],
        "date_added": data.get('date_addeds')[t],
        "runtime": data.get('runtimes')[t]
    })

print(json.dumps(playlist, indent=2))