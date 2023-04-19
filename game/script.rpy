# The script of the game goes in this file.
default health = 100
default energy = 100
default current_day = 1
default total_days = 14

default tutorial_started = False
default tutorial_skip_self_punch = False
default tutorial_self_punch_deny_count = 0

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define hero = Character("Magut", color='#ff0000')
define lady = Character("Meowmeoe", color="#0000ff")

# The game starts here.
label start:
    """
    *Alarm sounds*

    You wake up feeling energized. You recalled her messages yesterday, on the contest to grind gold in the game.

    You have promised her to do whatever it takes to help, and is planning to grind two million gold, minimum.

    As you get out of bed and start your day, thoughts of her and how you can help her fill your mind. You're determined to make a difference, starting today.
    """

    scene bg room
    with dissolve

    hero "Okaaaaaaaay, lets go!"

    show hero
    with dissolve

    hero """
    Alright, we doing this. I'm gonna stream with the boys, play some pumped up Rus-{w=1.0} Spanish music,{w=1.0} and grind.

    And then...
    """

    hide hero
    show lady
    show bg dream
    with dissolve

    hero "She will feel my love for her!"

    show hero
    hide lady
    show bg room
    with dissolve

    hero "Wait for me..."

    show screen stats with dissolve

    """
    Your stats are visible on the top left of the screen.
    """

menu:
    "They are mostly self explanatory, but do you need a small tutorial?"

    "Sure!":
        $ tutorial_started = True
    "Naaaah, naaaah, I'm not a pussy":
        "My man!"
        jump start_first_day

"""
Health shows... your health.

Energy shows... your energy.
"""

label tutorial_punch:
    pass

menu:
    "Try punching yourself for a bit!"

    "Fuck yeah, lets goooo!":
        $ health -= 98
        $ energy -= 5
        "Oof!" with vpunch

        """
        You forgot how strong you are sometimes. Come on, flex those guns.

        Yeeeeah.

        You looking good.

        fr fr

        Okay, lets eat some tacos to heal up.
        """

        $ health = 100
        $ energy = 100

        """
        That's the short of it. Good luck!
        """

    "Naaaah, naaaah, you trolling":
        $ tutorial_self_punch_deny_count += 1

        if tutorial_self_punch_deny_count <= 3:
            "Come on, I'm gonna softlock you here because I am a lazy dev :^)"
        elif tutorial_self_punch_deny_count > 3 and tutorial_self_punch_deny_count <= 5:
            "I told you I'm lazy :^)"
        else:
            $ tutorial_skip_self_punch = True
            "You sure are persistent :^("
            "But sure, good luck!"
            jump start_first_day

        jump tutorial_punch

label start_first_day:
    hero "It is a fresh day, day [current_day] out of [total_days]!"
    jump day_actions

label day_actions:
    pass

menu:
    hero "Plenty of things to do!"

    "Play game":
        pass
    "Check room":
        jump check_room
    "Drink BlueCow":
        pass
    "Sleep":
        pass

label check_room:
    pass

menu:
    hero "A clean and tidy room... as expected from a pro-gamer!"

    "Check EasyPeasyMethod book":
        "Nice book"
        jump check_room
    "Back to actions":
        jump day_actions
