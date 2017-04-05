def ftp_calc(twenty_min_power, weight_in_lbs):
    ftp = round(twenty_min_power * .95)
    weight_in_kg = round(weight_in_lbs / 2.2, 2)
    w_per_kg = round(ftp / weight_in_kg, 2)
    print(f"Your FTP in watts per kilo is {w_per_kg}.")

ftp_calc(282, 165)


twenty_power = 282
pounds = 165
ftp_calc(twenty_power, pounds)


ftp_calc(int(input("What is your 20 minute power?")), int(input("What is your weight in pounds?")))
