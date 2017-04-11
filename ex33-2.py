numbers = []

def count_up(i, number):
    for i in range(i, number):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


count_up(0, 6)
