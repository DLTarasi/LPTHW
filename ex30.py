people = 445
cars = 10
trucks = 10


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still cant decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's just stay home.")

if (people / 5) <= cars:
    print("We should take the cars.")
elif (people / 10) <= trucks:
    print("We should take the Trucks.")
else:
    print("Fine, let's just stay home.")
