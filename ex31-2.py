print("""The pre-race favorite attacks at the base of a steep climb.
Do you 1. Follow his attack or 2. Stay with the peloton?""")

choice = input("> ")

if choice == "1":
    print("You jump to follow, and form a small breakaway at the top of the climb!")
    print("What do you do?")
    print("1. Work together to try to make the break stick.")
    print("2. Sit on the other rider's wheel and refuse to work.")

    breakaway = input("> ")

    if breakaway == "1":
        print("The breakaway succeeds, but you are outsprinted at the finish for second.")
    elif breakaway == "2":
        print("The pack catches the breakaway, and you finish in 42nd place.")
    else:
        print(f"Well, doing {breakaway} is probably better.")
        print("The breakaway barely survives, and you outsprint the other rider for the Win!")

elif choice == "2":
    print("You watch the other rider slowly slip away up the climb. When you reach the summit, he is out of sight.")
    print("What do you do?")
    print("1. Descend with the peloton. There should be plenty of time to catch the break after the descent.")
    print("2. Stop for frites, no way we are catching this guy.")
    print("3. Throw caution to the wind and try to catch him on the descent!")

    peloton = input("> ")

    if peloton == "1":
        print("The breakaway is never seen again, but you win the bunch sprint for fifth.")
        print("Good job!")
    elif peloton =="2":
        print("The frites are delicious, but not as good as the taste of victory.")
    else:
        print("There is a patch of gravel in the final corner of the descent, and you plummet to your doom.")
        print("Should have gone with the breakaway!")

else:
    print("You weren't paying attention and crash into the rider ahead of you. Good Job!")
