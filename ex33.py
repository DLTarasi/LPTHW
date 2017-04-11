numbers = []

def count_up(i, number, step):
    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


count_up(5, 50, 5)
