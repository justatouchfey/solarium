# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aidana")

image steemopolis = Image("steemopolis_ex.jpg", xalign=0.75, yalign=0.25)

image tiger = Image("tiger.png", xalign=0.75, yalign=0.25)

image steempunknet = Image("steempunklogo.png", xalign=0.75, yalign=0.25)

image aristocrat_icon = Image("aristocrat_icon.png", xalign=0.25, yalign=0.25)

image adventurer_icon = Image("adventurer_icon.png", xalign=0.75, yalign=0.25)

define teleport = ImageDissolve("imagedissolveteleport.png", 1.0, 0)

image sun_one = Image("sun_one.png", xalign=0.7)
image sun_two = Image("sun_two.png", xalign=0.7)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene livingroombg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show aidana_neutral
    with teleport

    # These display lines of dialogue.

    a "{cps=35}Welcome to the introduction to the Solarium visual novel project.{/cps}"

    a "{cps=35}This little demo is meant to introduce you to the scope of the project and get a feel for the game's development roadmap.{/cps}"

    a "{cps=35}Please remember that the game is in development so many things may change before the end."

    a "{cps=35}This includes character sprites (even me!), backgrounds, game mechanics, and the framework.{/cps}"

    a "{cps=35}Before we begin, would you tell me your name?{/cps}"

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Torchwood"

    show aidana_happy
    hide aidana_neutral

    a "{cps=35}Hello [name], I'm Aidana Neapolis. I am the personal artificial intelligence assistant to many members of the Neapolis family. I'm here as your guide.{/cps}"

    show aidana_happy at left
    with move

    show steemopolis
    with dissolve

    a "{cps=35}This game takes place in the STEEMPUNK-NET universe, specifically in the Steemopolis Megacity.{/cps}"

    a "{cps=35}In it, Oona Neapolis, a member of a prestigious aristocratic family and prolific inventor, has contacted you, a fellow Clockwork Fighter, as a bounty hunter to recover...{/cps}"

    a "{cps=35}some of her creations that have gone missing.{/cps}"

    show aidana_special at left

    a "{cps=25}...{/cps}"

    show aidana_neutral at left
    hide aidana_special

    a "{cps=35}Oona is a lovely but sometimes troublesome person in our family...{/cps}"

    hide steemopolis

    show tiger
    with dissolve

    show aidana_happy at left
    hide aidana_neutral

    a "{cps=35}Oona is known as the brain behind the popular Clockwork Companions, new techno-organic pets that our family wishes the STEEMPUNK-NET syndicate to approve...{/cps}"

    a "{cps=35}as battle companions for their fighters in the Clockwork Arena. Members of the family believe that possibly a rival company has stolen the work in an attempt to beat us to the market.{/cps}"

    a "{cps=35}To gain your reward, you must investigate the crime scene, get to know the characters, and search various locations in the city for clues and recover the Clockwork Companions.{/cps}"

    show aidana_neutral at left
    hide aidana_happy

    a "{cps=35}Stay on your guard though. The thief may not take too kindly to you trying to track them down and as seasoned Clockwork Fighters all of your suspects have the brains and the brawn{/cps}"

    a "{cps=35} to take you out of the running for good.{/cps}"

    menu:
     "Tell me more about Steemopolis.":
         jump steempunk_exp

     "Let's move on.":
          jump move_on


label steempunk_exp:

    scene steemopolis_bg
    with dissolve

    a "{cps=35}The city is dominated by organizations and big corporations that have replaced governments. They compete against each other for power and the data of the citizens.{/cps}"

    show aidana_neutral
    with teleport

    a "{cps=35}Fiat currencies have become worthless. With cryptocurrencies, these corporations created new funds and are spending them on their loyal customers.{/cps}"

    show aidana_sad
    a "{cps=35}What began as a utopia has long since become a means of totalitarian consumer surveillance. Blockchains control the lives of all people in this new society.{/cps}"

    a "{cps=35}The corporations have gone so far as to create and enforce their own laws, backed by the power of their private militaries.{/cps}"

    scene livingroombg
    with dissolve

label move_on:

    hide tiger
    show aidana_neutral at left

    a "{cps=35}Even though the big corporations are always in a fight for the upper hand, they have a common goal: total control of the citizen.{/cps}"

    a "{cps=35}Therefore, for specific tasks, the companies associate themselves to syndicates if that furthers the common goal.{/cps}"

    show steempunknet
    with dissolve

    hide aidana_neutral
    show aidana_happy at left

    a "{cps=35}One such syndicate is STEEMPUNK-NET which hosts the fights in the Clockwork Arena.{/cps}"

    a "{cps=35}Brought to life by the most important corporations, fighting in the Clockwork Arena offers rebellious citizens the possibility to pit their strength against others in duels and to break out of the{/cps}"

    a "{cps=35}system in a controlled way.{/cps}"

    hide steempunknet
    show aidana_happy at center
    with move

    a "{cps=35}In the Clockwork Arena, there are two class types. The first is the aristocrat.{/cps}"

    show aristocrat_icon
    with dissolve

    a "{cps=35} The aristocrats are at the very top - in the truest sense of the word. The elite of the richest entrepreneurial families with thrones on the highest floors of the skyscrapers of all urban megacities.{/cps}"

    a "{cps=35}Equipped with the latest technology, their potential is artificially improved before they are born - genetic optimization, sophisticated implants, performance-enhancing{/cps}"

    a "{cps=35}stimulation packs. But the price for life in luxury and trans-humanistic performance enhancement is high: young aristocrats are constantly under observation starting{/cps}"

    a "{cps=35}with the first cell division in the womb. Always online, always tracked, always analyzed - and of course...{/cps}"

    show aidana_angry

    a "{cps=35}the blockchain never forgets anything.{/cps}"

    hide aidana_angry

    a "{cps=35}The second class is the adventurer.{/cps}"

    show adventurer_icon
    with dissolve

    hide aidana_happy
    show aidana_neutral

    a "{cps=35}The adventurers are at the bottom, often regulated to Ground Zero, where basic needs are not adequately met. There is a lack of water, food, Internet access and crypto money.{/cps}"

    a "{cps=35}While the beautiful new world reigns in the upper floors, the lower class has lost everything: knowledge, possessions, culture... Instead, you have a freedom down there that the upper world{/cps}"

    a "{cps=35}can only dream of. Anyone who is offline eludes the all-embracing grip of the corporations. Here the law of the strongest - or that of the cleverest - prevails.{/cps}"

    a "{cps=35}Anyone who can still gain access to secure network connection can make a lot of money...{/cps}"

    show aidana_special

    a "{cps=35}...provided you don't care about decency and morality.{/cps}"

    hide aidana_special

    a "{cps=35}Registering for the Clockwork Arena is easy and the possible rewards are high. Every fighter is equipped with an Ultima Corporation biomedical implant, which records information{/cps}"

    a "{cps=35}about your health and the battle. Aristocrats have this implant from birth, but having it as a requirement for battle can bring more reluctant adventurers into the arms of the data kraken.{/cps}"

    hide aristocrat_icon
    with dissolve

    hide adventurer_icon
    with dissolve

    hide aidana_neutral
    show aidana_happy

    a "{cps=35}[name], are you an aristocrat or an adventurer?{/cps}"

    menu:
     "An aristocrat.":
         jump aristocrat

     "An adventurer.":
          jump adventurer


label aristocrat:
    a "{cps=35}Oh! So you're an aristocrat then? Hopefully your wits and social connections will work to your advantage!{/cps}"

    jump continue

label adventurer:
    a "{cps=35}Oh! So you're an adventurer then? You may not have the social connections, but hopefully your life of hardship will work to your advantage!{/cps}"

label continue:

    a "{cps=35}This game will use several different mechanics to help you find Oona’s lost creations.{/cps}"

    a "{cps=35}You will have a series of locations available to you and you will search them to see if any clues are available and if any of Oona’s creations are there.{/cps}"

    a "{cps=35}This will most likely be accomplished through a hidden object mechanic that will respond to you as the player clicking in scene objects to find something.{/cps}"

    a "{cps=35}Locations are spread out all over Steemopolis city. Depending on which location you want to explore, you may need to develop relationships with different Clockwork Fighters to gain access.{/cps}"

    a "{cps=35}After all, if someone doesn’t know you they probably won’t let you search their house…{/cps}"

    a "{cps=35}Depending on your class, you will find that different Clockwork Fighters respond to you differently at first so you’ll have to be clever to gain access to all the locations.{/cps}"

    show aidana_neutral

    a "{cps=35}Besides getting to know the other Clockwork Fighters to search different locations, you’ll have to pay attention to the things they say, because you also want to be on the lookout for the thief.{/cps}"

    a "{cps=35}That person may not take too kindly to you returning Oona’s creations to her. If things go really awry, you might find yourself having to defend against attacks.{/cps}"

    show aidana_special

    a "{cps=35}The STEEMPUNK-NET syndicate frowns upon that kind of thing outside the arena, but since each corporation makes its own rules there’s a chance it could happen!{/cps}"

    hide aidana_special

    a "{cps=35}Not everything is as it seems on the surface of Steemopolis, as those who fall through the cracks know all too well.{/cps}"



    show sun animated behind aidana_neutral, aidana_angry:
        "sun_one"
        pause 1
        "sun_two"
        pause .5
    with teleport

    show aidana_angry

    a "{cps=25}...{/cps}"

    hide sun animated
    with teleport

    hide aidana_angry
    with teleport

    hide aidana_neutral
    with teleport

    hide aidana_happy
    with teleport

    # This ends the game.

    return
