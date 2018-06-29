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

        "What Part of your body seems to be having issues?"

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
        "Nose":
            jump nose
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
    scene back
    "Back"
    return
label abdomen:
    scene abdomen
    "Abdomen"
    return

label Pregion:
    scene Pregion
    "Pelvic Region"
    return

#Arm subsections

label upper_arm:
    scene upper_arm
    "Upper Arm"
    return
label elbow:
    scene elbows
    "Elbows"
    return

label lower_arm:
    scene lower_arm
    "Lower Arm"
    return
label hand:
    scene hand
    "Hands"
    return   


#Head

label eyes:
    scene eyes
    menu:
        "Section: Eyes"
        "General Pain":
            jump gen_pain
        "Vision Loss":
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
        "Throat":
            jump throat
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
        "Section: Head->Other"
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

    scene thighs

    "{b}thighs{/b}."
    return

label knees:

    scene knees

    "{b}knees{/b}."
    return

label lower_leg:

    scene lower_leg

    "{b}lower leg{/b}."
    return

label foot:

    scene foot

    "{b}foot{/b}."
    return



#chest symptoms
label tightness:
    scene black
    "Tightness"
    return
label trouble_breathing:
    scene black
    "Trouble Breathing"
    return

label muscle_pain:
    scene black
    "Muscle Pain"
    return

label other_chest:
    scene black
    "Other"
    return


#mouth symptoms

label teeth:

    scene teeth

    "{b}Teeth{/b}."
    return

label tongue:

    scene tongue

    "{b}Tongue{/b}."
    return

label throat:

    scene throat

    "{b}Throat{/b}."

    return
label other_mouth:

    scene _other_mouth

    "{b}Other->mouth{/b}"
    return

#eyes symptoms
label gen_pain:

    scene eyes_pain

    "{b}General Pain -> eyes{/b}."
    return

label vision_loss:

    scene eyes_vision_loss

    "{b}Vision Loss{/b}."
    return

label watery_eyes:

    scene watery_eyes

    "{b}Watery Eyes/Irritation/b}."
    return
label other_eyes:

    scene other_eyess

    "{b}Other{/b}"
    return

#nose symptoms

label runny_nose:

    scene _runny_nose

    "{b}Runny Nose{/b}."
    return
label congestion:

    scene _congestion

    "{b}Congestion{/b}."
    return
label sneezing:

    scene _sneezing

    "{b}Sneezing{/b}."
    return
label other_nose:

    scene _other_nose

    "{b}Nose->Other{/b}."
    return




#other symptoms
label headache:

    scene headache

    "Headache."

    menu:
        "Please Describe your headache."
        "Throbbing":
            jump throbbing_head
        "Burning":
            jump burning_head
        "Dull":
            jump dull_head
        "Other":
            jump other_headache
    return

#throbbing headache
label throbbing_head:
    scene throbbing_headache
    "{b}Throbbing Headache{/b}"
    return  
#burning headache  
label burning_head:
    scene burning_head
    "{b}Burning Headache{/b}"
    return  
    
#dull headache
label dull_head:
    scene dull_head
    "{b}Dull Headache{/b}"
    return
#other headache
label other_headache:
    scene other_headache
    "{b}Other Headache{/b}"
    return       
label fever:

    scene fever

    "{b}Fever{/b}."
    return
label psych:

    scene psych

    "{b}Psych{/b}."
    return
label other_other:

    scene _other_other

    "{b}Other->Other{/b}."
    return
