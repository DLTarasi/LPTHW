def tuscanycamp():
    global wkg
    global sprint
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
        wkg -= .4
        campfail()
    else:
        print(f"Okay, we can {train}, but I don't think it will help.")
        campneutral()

def flanderscamp():
    global wkg
    global sprint
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
    global wkg
    global sprint
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
    global wkg
    global sprint
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

def tdf():
    print("TDF")

def roubaix():
    print("Roubaix")

#intro
print("It's the start of another hard offseason of training.")
print("Your goal is to win your race of choice, either the Tour de France or Paris-Roubaix.")
print("First, we should determine your current fitness. We'll need to know your power over a few different intervals and your weight.")


# function to calculate ftp
def wkg_calc(twenty_min_power, weight_in_lbs):
    ftp = round(twenty_min_power * .95)
    weight_in_kg = round(weight_in_lbs / 2.2, 2)
    w_per_kg = round(ftp / weight_in_kg, 2)
    return(w_per_kg)

######### This block gets user inputs for each variable and assigns them
wkg = wkg_calc(int(input("What is your 20 minute power in watts? ")), int(input("What is your weight in pounds? ")))
if wkg > 3.5:
    print(f"Your FTP is {wkg} watts per kilogram. That's pretty good. Let's see how your sprint is.")
else:
    print(f"Your FTP is {wkg} watts per kilogram. That's a little low. Maybe you are a better sprinter?")

sprint = int(input("What is your max sprint power (in watts)?: "))
if sprint > 1250:
    print(f"Your sprint power is {sprint} watts. That's pretty good. You should consider sprinting for the win.")
else:
    print(f"Your sprint power is {sprint} watts. That's a little low. Hopefully you're a good climber.")

print("We also need to make sure you don't crash out of the race.")
skills = input("Are you a good bike handler?: ")
if skills == "yes":
    print("Great, that might prove advantageous later.")
else:
    print("Uh oh, take it easy out there.")
##########

######### Tell what current stats are and get training camp location.
print(f"Now we know that your FTP is {wkg} watts per kilo, and you can sprint at {sprint} watts. It's time for training camp.")
print("Where do you want to go, Flanders or Mallorca are always good options.")

camp = input("> ")
########

###### adjust stats based on training camp location and starts camp function for that location
tuscany = ["Tuscany", "tuscany", "Tuscany.", "tuscany."]
flanders = ["Flanders", "flanders", "Flanders.", "flanders."]
mallorca = ["Mallorca", "mallorca", "mallorca.", "Mallorca."]

if camp in tuscany:
    print("I wouldn't have thought of that, but its a great idea!")
    sprint += 150
    wkg += .3
    tuscanycamp()
elif camp in flanders:
    print("Great. Hope you like cobbles!")
    sprint += 100
    flanderscamp()
elif camp in mallorca:
    print("Great. There is no where better to learn to climb.")
    wkg += .25
    mallorcacamp()
else:
    print(f"Fine, we can train in {camp}, but I don't think it's the best option.")
    othercamp()
########
