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
#main sections
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

label arms:

    scene black
    menu:
        "Section: Arms"
        "Upper Arms":
            jump upper_arm
        "Elbows":
            jump elbow
        "Lower Arms":
            jump lower_arm
        "Hand":
            jump hand

    "{b}Arms{/b}."
    return




#Midsection
label chest:
    scene black

    menu:
        "Chest"
        "Tightness":
            jump tightness
        "Trouble Breathing":
            jump trouble_breathing
        "Muscle Pain":
            jump muscle_pain
        "Other":
            jump other_chest


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

#Arms subsections

label upper_arm:
    scene black
    "Back"
    return
label elbow:
    scene black
    "Abdomen"
    return

label lower_arm:
    scene black
    "Pelvic Region"
    return
label hand:
    scene black
    "Pelvic Region"
    return   


#Head

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

label nose:

    scene black

    menu:
        "Section: Nose"
        "Runny Nose":
            jump runny_nose
        "Congestion":
            jump congestion
        "Sneezing":
            jump sneezing
        "Other":
            jump other_nose

    return

label other:

    scene black

    menu:
        "Section: Other"
        "Headache":
            jump headache
        "Fever":
            jump fever
        "Psychological":
            jump psych
        "Other":
            jump other_other
    return

#legs subsections

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



#chest symptoms
label tightness:
    scene black
    "Back"
    return
label trouble_breathing:
    scene black
    "Abdomen"
    return

label muscle_pain:
    scene black
    "Pelvic Region"
    return

label other_chest:
    scene black
    "Pelvic Region"
    return


#mouth symptoms

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

#eyes symptoms
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

#nose symptoms

label runny_nose:

    scene black

    "{b}thighs{/b}."
    return
label congestion:

    scene black

    "{b}thighs{/b}."
    return
label sneezing:

    scene black

    "{b}thighs{/b}."
    return
label other_nose:

    scene black

    "{b}thighs{/b}."
    return




#other symptoms
label headache:

    scene black

    "{b}thighs{/b}."
    return
label fever:

    scene black

    "{b}thighs{/b}."
    return
label psych:

    scene black

    "{b}thighs{/b}."
    return
label other_other:

    scene black

    "{b}thighs{/b}."
    return
