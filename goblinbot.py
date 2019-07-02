import tweepy, random, sys, time

#---------------------------------------
# Setup OAuth
#---------------------------------------

# Consumer keys and access tokens, used for OAuth
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#---------------------------------------
# Generation
#---------------------------------------

# Names
part1_names = ["Boar", "Grog", "Rot", "Zob", "Slug", "Mak", "Gunk", "Slag", "Wart", "Drab", "Giz", "Fig", "Mug", "Gib", "Bag", "Sak",
 "Snot", "Rok", "Log", "Mud", "Sick", "Hag", "Fart", "Flem", "Cram", "Spug", "Pog"]

part2_names = ["gax", "nax", "log", "gil", "murch", "gub", "foot", "belly", "maggle", "bog", "lub", "lug", "kul", "sog", "rod", "sok", 
"stab", "face", "rider", "killa", "nash", "jaw", "biter", "gut", "root", "bog"]

single_names = ["Droop", "Stabber", "Igor", "Stabface", "Toot", "Sizzle", "Gnish", "Bagface", "Slug", "Lenny", "Gobbo", "Dung", "Feral",
"Rooty", "Vomit", "Gassy"]

# Visual
colours = ["light green", "green", "dark green", "light brown", "brown", "dark brown", "dark yellow"]
appearance1 = ["Muddy", "Small", "Scarred", "Chubby", "Fat", "Surprisingly clean", "Grotesque", "Scaly", "Skinny", "Bony"]
appearance2 = ["Sweaty", "Smelly", "Pungent", "Slimy", "Pot-Bellied", "Revolting"]
c_thing = [colours, appearance2]

# Behaviours
personality = ["Vomitting", "Unwell", "Sulking", "Confused", "Hostile", "Frustrated at something", "Frustrated at someone", "Blind", "Angry at someone", "Angry at something", "Sleeping",
"Coming towards you", "Approaching curiously", "Guilty", "Lonely", "Alone", "Scared", "Frightened", "Lost", "Attempting to hide", "Looking for something", "Looking for someone", "Hiding something"]

# Weapons
weapons = ["dagger", "spear", "club", "scimitar", "shortsword", "mace", "hatchet", "hammer", "warhammer", "trident", "morningstar"]
weaponDesc = ["rusty", "dirty", "blunt", "crude", "bloodied", "polished", "worn", "broken", "crusty", "muddy", "stolen", "hand-made", "sheathed"]
weaponCarryType = ["carrying", "holding", "swinging", "wielding"]

# Subclass
subclass = ["swamp", "tinker", "mountain", "hill", "forest", "cave"]

# Joiners
endJoin = ["appears to be", "is"]

def CreateDescription():
    name = ""
    if random.random() < .2:
        name = random.choice(single_names)
    else:
        name = random.choice(part1_names) + random.choice(part2_names).lower()
    
    desc1 = random.choice(appearance1).lower()
    desc2 = random.choice(random.choice(c_thing)).lower()
    pers = random.choice(personality).lower()

    weapon = ""
    if random.random() < .8:
        weapon = " and " + random.choice(weaponCarryType) + " a " + random.choice(weaponDesc).lower() + " " + random.choice(weapons).lower()
    else:
        weapon = ""

    goblinType = random.choice(subclass)

    a = ""
    b = ""

    if random.random() < .5:
        a = desc1
        b = desc2
    else:
        a = desc2
        b = desc1

    return name + " - a " + a + " " + b + " " + goblinType + " goblin who " + random.choice(endJoin)+ " " + pers + weapon + " #DND"


#---------------------------------------
# Tweeting
#---------------------------------------

def run():
    desc = CreateDescription()
    print(desc)
    api.update_status(desc)

# Runs every 20 minutes via a crontab
run()

# Alternativley run this python script with a sleep
# while True:
#    run()
#    time.sleep(900)
