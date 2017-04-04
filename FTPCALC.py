print("Let's calculate your FTP in Watts per Kilogram.")

#this section gets input of users 20 min power and calculates then displays FTP
print("One common way to calcuLate FTP is by taking 95 percent of your 20 minute power.")
print("What is your best 20 minute power (in watts)?", end=' ')
twenty_minute_power = int(input())
ftp = round(twenty_minute_power * .95)
print(f"Your FTP is {ftp}.")

#this calculates and displays weight in KG rounded to 2 decimals from input of weight in pounds
print("What is your weight in pounds?", end=' ')
weight_in_lbs = int(input())
weight_in_kg = round(weight_in_lbs / 2.2, 2)
print(f"Your weight in kilograms is {weight_in_kg}.")

#uses FTP and weight in KG to calc and display W per kg rounded to 2 decimals
w_per_kg = round(ftp / weight_in_kg, 2)
print(f"Your FTP in watts per kilo is {w_per_kg}.")
