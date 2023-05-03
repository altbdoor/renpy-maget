# ========================================
# variables
# ========================================
default health = 100
default energy = 100
default hour_current = 1
default hour_max = 20 * 24

default lady_name = "Bangs"

default gold_goal = 2000000
default gold_amount = 0

default tutorial_started = False
default tutorial_skip_self_punch = False
default tutorial_self_punch_deny_count = 0

default actions = []

default grind_hour = 6
default grind_energy = -15

default redbull_total = 0
default redbull_energy = 40
default redbull_hour = 1

default sleep_hour = 8
default sleep_energy = 80

# ========================================
# characters
# ========================================
define hero = Character("Magut", color="#ff0000")
define lady = Character("Bangs", color="#0000ff")

# ========================================
# python
# ========================================
init python:
    def clamp(val, smallest, largest):
        return max(smallest, min(val, largest))

# ========================================
# start
# ========================================
label start:
    """
    *Alarm sounds*

    You wake up feeling energized. You recalled the messages from [lady_name] yesterday, on the contest to grind gold in the game.

    You have promised her to do whatever it takes to help, and is planning to grind two million gold, minimum.

    As you get out of bed and start your day, thoughts of [lady_name] and how you can help her fill your mind. You are determined to make a difference, starting today.
    """

    scene bg room
    with dissolve

    hero "Okaaaaaaaay, lets go!"

    show hero
    with dissolve

    hero "Alright, we doing this. I am gonna stream with the boys, play some pumped up Rus-{w=0.5} Spanish music,{w=0.5} and grind."
    hero "And then..."

    show bg dream
    show hero at left
    show lady at right
    with dissolve

    hero "She will feel my love for her!"

    show hero at center
    hide lady
    show bg room
    with dissolve

    hero "Wait for me..."

    show screen stats with dissolve

    $ total_days = hour_max // 24

    """
    Your stats are visible on the top left of the screen.

    You have [total_days] days to complete the task, which will be measured in hours.
    """

menu:
    "They are mostly self explanatory, but do you need a small tutorial?"

    "Sure!":
        $ tutorial_started = True
        jump tutorial_start
    "Naaaah, naaaah, I am not a pussy":
        "My man!"
        jump start_day

# ========================================
# tutorial
# ========================================
label tutorial_start:
    """
    Health shows... your health.

    Energy shows... your energy.
    """

label tutorial_start_punch:
    pass

menu:
    "Try punching yourself for a bit!"

    "Fuck yeah, lets goooo!":
        $ health -= 98
        $ energy -= 5

        "Oof!" with vpunch

        "You forgot how strong you are sometimes. Come on, flex those guns."

        "Yeeeeah."

        "You looking good."

        "fr fr"

        "Okay, lets eat some tacos to heal up."

        $ health = 100
        $ energy = 100

        """
        That is the short of it. Good luck!
        """

    "Naaaah, naaaah, you trolling":
        $ tutorial_self_punch_deny_count += 1

        if tutorial_self_punch_deny_count <= 3:
            "Come on, I am gonna softlock you here because I am a lazy dev :^)"
        elif tutorial_self_punch_deny_count > 3 and tutorial_self_punch_deny_count <= 5:
            "I told you I am lazy :^)"
        else:
            $ tutorial_skip_self_punch = True
            "You sure are persistent :^("
            "But sure, good luck!"
            jump start_day

        jump tutorial_start_punch

label start_day:
    hero "It is a fresh day, day 1!"
    jump day_actions

# ========================================
# day actions
# ========================================
label day_actions:
    if hour_current >= hour_max:
        hero "It is time!"
        jump judgement_day
    elif gold_amount >= gold_goal:
        hero "I have done it! I have enough gold now!"
        jump judgement_day

    if hour_current == 1:
        hero "Plenty of things to do!"

    elif energy == 0:
        if "tired_max" not in renpy.get_attributes(tag="hero"):
            show hero tired_max
            with dissolve

        hero "I am completely wasted... I need to get some sleep!"

    elif energy <= 20:
        if "tired_medium" not in renpy.get_attributes(tag="hero"):
            show hero tired_medium
            with dissolve

        hero "I am getting kinda tired..."

menu:
    "Play game":
        if energy + grind_energy <= 0:
            hero "I do not have enough energy to grind the game right now..."
            jump day_actions

        $ actions.append("game")
        $ energy = clamp(energy + grind_energy, 0, 100)
        $ hour_current += grind_hour

        $ current_gold = renpy.random.randint(20000, 50000)
        $ current_gold_display = f"{current_gold:,}"

        $ gold_amount += current_gold
        "You have grinded [current_gold_display] gold!"

        jump day_actions

    # "Check room":
    #     $ actions.append("check_room")
    #     jump check_room

    "Drink a BlueCow":
        if energy == 0:
            hero "I am too weak for a BlueCow right now..."
            jump day_actions

        $ actions.append("redbull")
        $ redbull_total += 1
        $ redbull_current_count = actions[-6:].count("redbull")

        show hero drink
        with dissolve

        "You drink a BlueCow..."

        if redbull_current_count >= 6:
            jump redbull_overdose

        python:
            redbull_restore_bonus = renpy.random.randint(0, redbull_energy // 2)
            redbull_restore_minus = renpy.random.randint(0, redbull_total) * 10
            redbull_restore = redbull_energy + redbull_restore_bonus - redbull_restore_minus

        $ energy = clamp(energy + redbull_restore, 0, 100)
        $ hour_current += redbull_hour

        if redbull_current_count <= 3:
            if redbull_restore > 0:
                show hero drink_ok
                with dissolve

                hero "Alright, I feel energized!"
            else:
                show hero drink_bad
                with dissolve

                hero "Tastes weird... I felt weaker."
        elif redbull_current_count < 6:
            if redbull_restore > 0:
                show hero drink_danger_ok
                with dissolve

                hero "Ugh, I still feel weird, but the BlueCow kinda helped..."
            else:
                show hero drink_danger_bad
                with dissolve

                hero "Ugh, did someone stick their pepe into this BlueCow? Bleurgh!"

        show hero
        with dissolve

        jump day_actions

    "Sleep":
        $ actions.append("sleep")
        $ initial_energy = energy
        $ energy = clamp(energy + sleep_energy, 0, 100)
        $ current_sleep_hour = sleep_hour + renpy.random.randint(0, 3)

        show bg room_bed
        hide hero
        with dissolve

        hero "Zzz..."

        if initial_energy <= 10 and renpy.random.randint(0, 3) != 0:
            $ hour_current += current_sleep_hour * 2

            hero "Oh no! I have overslept! Agh, what time is it?"

        else:
            $ hour_current += current_sleep_hour

            "You slept for [current_sleep_hour] hours... You feel refreshed!"

        show bg room
        show hero
        with dissolve

        jump day_actions

# ========================================
# check room
# ========================================
# label check_room:
#     show bg room_side
#     with dissolve

# menu:
#     "Check EasyPeasyMethod book":
#         "Nice book"
#         jump check_room

#     "Back to actions":
#         jump day_actions

# ========================================
# redbull overdose
# ========================================
label redbull_overdose:
    $ health = 0

    scene bg redbull_overdose
    with dissolve

    """
    You have consumed too many BlueCows over a short period of time.

    Generally a large can of BlueCow has approximately 30mg of caffeine, and consuming more than 100mg a day, severely increases the risk of overdosing.

    Every year, more and more deaths are attributed to over consumption of energy drinks.

    Please, consume energy drinks responsibly.
    """

    return

# ========================================
# judgement day
# ========================================
label judgement_day:
    if gold_amount >= gold_goal:
        jump judgement_day_success
    else:
        jump judgement_day_failure

label judgement_day_success:
    scene bg judgment
    show hero judgement_happy
    hide screen stats
    with dissolve

    hero "I made it!"

    jump the_end

label judgement_day_failure:
    scene bg judgment
    show hero sad
    hide screen stats
    with dissolve

    hero "I... I did not make it! There was not enough time... Stupid fucking mistakes, man!"

    "You realized that you were not able to grind enough gold to impress [lady_name]. You feel discouraged and disheartened."

    hero "How do I even face her..."

    show hero sad at left
    show lady at right
    with dissolve

    lady "Hey, Magut! How did the grind go?"

    hero "W-well... ahaha... {w=0.5} it is what it is!"

    $ gold_amount_display = f"{gold_amount:,}"
    "You nervously traded over the sum of [gold_amount_display] gold, hoping for the best."

    hero "I... did my best... but I did not have enough time."

    show hero at left
    with dissolve

    hero "It is not much, but I hope you can win the contest, [lady_name]!"

    show lady happy at right
    with dissolve
    lady "Thanks Magut! That is so kind of you."

    show lady at right
    with dissolve
    lady "I appreciate it."
    lady "I gotta attend to my stream for a bit, I will talk to you later?"
    hero "Haha, sure!"
    lady "Goodbye!"

    show hero sad at center
    hide lady
    with dissolve

    """
    As the blip of [lady_name]'s presence icon turn offline, you felt a tinge of sadness in your heart.

    It was not the outcome you had hoped for, but you have tried your very best...
    """

    if redbull_total > 10:
        "...with [redbull_total] cans of BlueCow."

    show hero
    with dissolve

    hero "It is what it is... what could you do about it, right?"
    hero "I think..."
    hero "I think I will go to gym..."

    hide hero
    with dissolve

    """
    In the end, you realized that you had been too focused on impressing her and had neglected to see the value in the friendships that you had built along the way.

    Sometimes it is not about the gifts or the material things, but about the connections and relationships that we build.

    You closed your computer, feeling grateful for the experience and the lessons learned.

    Ready to face new challenges with a positive mindset.
    """

    jump the_end

# ========================================
# end
# ========================================
label the_end:
    "-- END --"
    return
