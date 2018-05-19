# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")




# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene bg lecturehall
    with fade

    s"Hi I'm *Insert Doctor name*! "
    scene bg uni
    show sylvie green normal
    menu:

        "What Part of your  body seems to be having issues?"

        "Midsection":
            jump midsection
        "Legs.":
            jump legs
        "Arms.":
            jump arms
        "Head.":
            jump head

    return

label midsection:

    scene red
    menu:
     "chest":
        jump chest
     "Back":
        jump back
     "Abdomen":
        jump abdomen
     "Pelvic Region":
        jump Pregion

return

label legs:
    scene red
    menu:
        "Thighs.":
            jump thighs
        "Knees.":
            jump knees
        "Lower Leg.":
            jump lower_leg
        "Foot.":
            jump foot

    return

label thighs:

    scene black

    "{b}thighs{/b}."
    return

label knees:

    scene black

    "{b}knees{/b}."
    return

label lower_leg:

    scene black

    "{b}lower leg{/b}."
    return

label foot:

    scene black

    "{b}foot{/b}."
    return

label head:
    scene blue
    menu:
        "Section: Head"
        "Eyes":
            jump eyes
        "Mouth":
            jump mouth
        "Other":
            jump other


    return


label eyes:
    scene violet
    menu:
        "Section: Head"
        "Eyes":
            jump gen_pain
        "Mouth":
            jump vision_loss
        "Watery Eyes/Irritation":
            jump watery_eyes
        "Other":
            jump other_eyes

    return

label gen_pain:

    scene black

    "{b}General Pain -> eyes{/b}."
    return

label vision_loss:

    scene black

    "{b}Vision Loss{/b}."
    return

label watery_eyes:

    scene black

    "{b}Watery Eyes/Irritation/b}."
    return
label other_eyes:

    scene black

    "{b}Other{/b}"
    return

label mouth:

    scene black

    menu:
        "Section: Mouth"
        "Teeth":
            jump teeth
        "Tongue":
            jump tongue
        "Gums":
            jump gums
        "Other":
            jump other_mouth

    return

label teeth:

    scene black

    "{b}Teeth{/b}."
    return

label tongue:

    scene black

    "{b}Tongue{/b}."
    return

label gums:

    scene black

    "{b}Gums{/b}."
    return
label other_mouth:

    scene black

    "{b}Other->mouth{/b}"
    return
label other:

    scene black

    "{b}Other-> Head{/b}."
    return


label arms:

    scene black

    "{b}Arms{/b}."
    return




label chest:
    scene black
    "Chest"
    return

label back:
    scene black
    "Back"
    return
label abdomen:
    scene black
    "Abdomen"
    return

label Pregion:
    scene black
    "Pelvic Region"
    return
