skills = "no"
wkg = 3.5
sprint = 1500

def tdf():
    print("It is the penultimate day of the 2017 Tour De France.")
    print("Things have gone well for you and your team.")
    print("You have a narrow 10 second lead over the pre-race favorite, Chris Froome.")
    print("Froome attacks at the base of a Alp d'Huez.")
    print("Do you 1. Follow his attack or 2. Stay with the peloton?")

    choice = input("> ")

    if choice == "1" and wkg >= 4:
        print("You jump to follow, and stick to his wheel as you near the top of the climb!")
        print("What do you do?")
        print("1. Throw caution to the wind and try to drop him on the descent!")
        print("2. Stay close but don't take any chances.")

        breakaway = input("> ")

        if breakaway == "1" and skills == "yes":
            print("It worked - he's no match for you supertuck skills. All that is left is to coast to victory!")
        elif breakaway == "1" and skills != "yes":
            print("There is a patch of gravel in the final corner of the descent, and you plummet to your doom.")
        elif breakaway == "2" and sprint >= 1250:
            print("You did it! You held on during the descent and were able to sprint away for the Win!")
            print("Tomorrow you'll be poppin' champagne in Paris. Congrats!")
        elif breakaway == "2" and sprint < 1250:
            print("What a heartbreaking loss! You held on for the entire descent but got dropped on the sprint into the finish.")
            print("Second place is not bad, but you'll always be left to wonder what might have been if you'd just trained your sprint a bit harder.")
        else:
            print("You weren't paying attention and crash into the rider ahead of you. Good Job!")


    elif choice == "1" and wkg < 4:
        print("You try to follow, but you're just no match. You watch Froome float away, along with your hopes and dreams. Maybe you should have trained harder at camp.")
        print("The effort saps your last bit of power, and you fall off the back of the peloton. You'll be lucky to hold on to a top ten!")
    elif choice == "2":
        print("You watch Froome slowly slip away up the climb. When you reach the summit, he is out of sight.")
        print("What do you do?")
        print("1. Descend with the peloton. We have a small lead and might still hold on for the win!")
        print("2. Throw caution to the wind and try to catch him on the descent!")

        peloton = input("> ")

        if peloton == "1" and sprint < 1250:
            print("Froome is never seen again, but you finish safely with the group and will stand on the second step of the podium in Paris with thoughts of what might have been.")
        elif peloton == "1" and sprint >= 1250:
            print("As you reach the bottom of the descent, you can see Froome off in the distance.")
            print("You launch an all out sprint and are able to catch him just as you cross the line.")
            print("Tomorrow you'll be poppin' champagne in Paris. Congrats!")
        elif peloton == "2" and skills == "yes":
            print("It worked. You catch him just short of the finish and hold on to your narrow lead.")
            print("Tomorrow you'll be poppin' champagne in Paris. Congrats!")
        elif peloton == "2" and skills != "yes":
            print("There is a patch of gravel in the final corner of the descent, and you plummet to your doom.")
            print("Did you really think that was a good idea with your poor bike handling skills?")
        else:
            print("You weren't paying attention and crash into the rider ahead of you. Good Job!")

    else:
        print("You weren't paying attention and crash into the rider ahead of you. Good Job!")

tdf()

#def roubaix():
#    print("""All of your training has come down to this. It's hard to believe, but after 170km of freezing rain, mud, and cobbles,
#    you find yourself in a select group of riders, including Tom Boonen and Peter Sagan. With only a few sectors to go, someone has to make a move.""")
#    print("Boonen attacks at the start of the Carrefour de l'Arbre")
