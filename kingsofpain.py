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
wkg = wkg_calc(int(input("What is your 20 minute power? ")), int(input("What is your weight in pounds? ")))
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
print("Great. Now we know that your FTP is {wkg} watts per kilo, and you can sprint at {sprint} watts. It's time for training camp."
print("Where do you want to go, Flanders or Mallorca are always good options.")

camp = input(": ")
########

###### adjust stats based on training camp location
if camp == "Girona" or "girona" or "Girona." or "girona."
    print("I wouldn't have thought of that, but its a great idea!")
    sprint += 150
    wkg += .3
elif camp == "Flanders" or "flanders" or "Flanders." or "flanders.":
    print("Great. Hope you like cobbles!")
    sprint += 100
elif camp == "Mallorca" or "mallorca" or "mallorca." or "Mallorca.":
    print("Great. There is no where better to learn to climb.")
    wkg += .25
else:
    print(f"Fine, we can train at {camp}, but I don't think it's the best option.)
########

####### Flanders Training Camp
