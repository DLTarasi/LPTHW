def tuscanycamp():
    print("You just landed in the beatiful green hills of Tuscany. How do you want to spend your time at camp?")
    print("You could train your FTP on the strade bianche, work on your sprint on the street of San Remo, or just sit around and eat pasta.")
    train = input("> ")
    if "ftp" in train or "strade" in train or "bianche" in train:
        print("Great. We'll work on your FTP.")
        wkg += .25
        campsuccess()
    elif "sprint" in train or "San" in train or "Remo" in train:
        print("Great. We'll work on your sprint.")
        sprint += 100
        campsuccess()
    elif "eat" in train or "sit" in train or "pasta" in train:
        print("That's not a good idea, but pasta is hard to resist! Try the cacio e pepe.")
        wkg -= .25
        campfail()
    else:
        print(f"Okay, we can {train}, but I don't think it will help.")
        campneutral()

def flanderscamp():
    print("You just landed in Flanders. Unsurprisingly, it's overcast, cold, and wet. Why did we come here again? Well, we need to train anyway. How do you want to spend your time at camp?")
    print("You could train your FTP on the cobbles, work on your sprint on the Koppenberg, or just sit around and eat frites.")
    train = input("> ")
    if "ftp" in train or "cobbles" in train:
        print("Great. We'll work on your FTP.")
        wkg += .2
        campsuccess()
    elif "sprint" in train or "koppenberg" in train or "Koppenberg" in train:
        print("Great. We'll work on your sprint.")
        sprint += 150
        campsuccess()
    elif "eat" in train or "sit" in train or "frites" in train:
        print("That's not a good idea, but frites are hard to resist! Make sure to get a beer too!")
        wkg -= .3
        campfail()
    else:
        print(f"Okay, we can {train}, but I don't think it will help.")
        campneutral()

def mallorcacamp():
    print("You just landed on the sunny island of Mallorca. Why did we ever consider Flanders? How do you want to spend your time at camp?")
    print("You could train your FTP on the Sa Colabra, work on your sprint on the short climb up Coll de sa Creu, or just sit around and eat tapas.")
    train = input("> ")
    if "ftp" in train or "Sa Colabra" in train or "colabra" in train:
        print("Great. We'll work on your FTP.")
        wkg += .4
        campsuccess()
    elif "sprint" in train or "short climb" in train or "Coll de sa Creu" in train or "coll" in train:
        print("Great. We'll work on your sprint.")
        sprint += 75
        campsuccess()
    elif "eat" in train or "sit" in train or "tapas" in train:
        print("That's not a good idea, but tapas are hard to resist! Try the papas bravas with a nice rioja.")
        wkg -= .2
        campfail()
    else:
        print(f"Okay, we can {train}, but I don't think it will help.")
        campneutral()

def othercamp():
    print("How do you want to spend your time at camp?")
    print("You could train your FTP on a long climb, work on your sprint on short hills, or just sit around and eat doughnuts.")
    train = input("> ")
    if "ftp" in train or "climb" in train or "long" in train:
        print("Great. We'll work on your FTP.")
        wkg += .25
        campsuccess()
    elif "sprint" in train or "short" in train or "hills" in train:
        print("Great. We'll work on your sprint.")
        sprint += 100
        campsuccess()
    elif "eat" in train or "sit" in train or "doughnuts" in train:
        print("That's not a good idea, but doughnuts are hard to resist! Make sure to have a coffee too.")
        wkg -= .25
        campfail()
    else:
        print(f"Okay, we can {train}, but I don't think it will help.")
        campneutral()

def campsuccess():
    print(f"Your training camp was successful. Your FTP is now {wkg} watts per kilo, and your sprint is now {sprint} watts.")
    print("It's time to race! Are we going to Roubaix or the Tour?")
    race = input("> ")
    if "France" in race or "Tour" in race:
        tdf()
    elif "Roubaix" in race or "Paris" in race:
        roubaix()

def campfail():
    print(f"Your training camp was a failure. Your FTP is now {wkg} watts per kilo, and your sprint is now {sprint} watts.")
    print("Oh well, we still need to race. Are we going to Roubaix or the Tour?")
    race = input("> ")
    if "France" in race or "Tour" in race:
        tdf()
    elif "Roubaix" in race or "Paris" in race:
        roubaix()

def campneutral():
    print(f"Your training camp was a wash. Your FTP is now {wkg} watts per kilo, and your sprint is now {sprint} watts.")
    print("Oh well, we still need to race. Are we going to Roubaix or the Tour?")
    race = input("> ")
    if "France" in race or "Tour" in race:
        tdf()
    elif "Roubaix" in race or "Paris" in race:
        roubaix()
