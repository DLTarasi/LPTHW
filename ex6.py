#assigns variable types_of_people as 10
types_of_people = 10
# assigns variable x as the formatted string with the value for types_of_people inserted
x = f"there are {types_of_people} types of people."
#assigns string binary to variable binary
binary = "binary"
#assigns string don't to variable do_not
do_not = "don't"
# inserts variables binary and do_not into string and assigns to y
y = f"Those who know {binary} and those who {do_not}."

#prints x and y
print(x)
print(y)

#prints strings below with strings x and y inserted
print(f"I said: {x}")
print(f"I also said '{y}'")

#asssigns value false to variable hilarious
hilarious = False
#assigns string to variable joke_evaluation. the empty curly braces allow a variable to be inserted at the end of the string in the line below
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

#assigns strings to the two variables
w = "this is the left side of..."
e = "a string with a right side."

#combines the two strings assigned to the variables
print(w + e)
