import random

if __name__ == "__main__":
    print("Enter a range of numbers (seperated with a comma)")
    range_values = input("Range (e.g.: 10,20): ")

    range_values = range_values.split(",")
    random_int = random.randint(int(range_values[0]), int(range_values[1]))
    print(random_int)

    while True:
        guess = int(input("Enter your guess: "))
        if guess == random_int:
            print("Congratulations! " + str(guess) + " was correct!")
            break
        else:
            print("Wrong guess! Try again.")