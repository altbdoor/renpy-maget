# The script of the game goes in this file.

default energy = 100

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define magomet = Character("Magomet", color='#ff0000')

# The game starts here.
label start:

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
        pass
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
