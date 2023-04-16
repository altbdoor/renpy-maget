# The script of the game goes in this file.
default health = 100
default energy = 100
default days = 14

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define magomet = Character("Magomet", color='#ff0000')

# The game starts here.
label start:
    show screen stats

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    with dissolve

    # These display lines of dialogue.

menu:
    "huh"

    "yes":
        $ energy -= 20
    "no":
        pass

label foo:
    """
    say no one us saying shit

    and lmao
    """

    magomet "Your energy is [energy]."

    magomet "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
