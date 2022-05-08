import random

def roll_dice(dice_eyes, amount):
    for i in range(0, int(amount)):
       dice_result = random.randint(0, int(dice_eyes))
       print(str(i+1) + ". Dice: " + str(dice_result))

if __name__ == "__main__":
    print("Dice Rolling Simulator\n")
    amount = input("Dice amount: ")
    dice_eyes = input("Dice eyes: ")

    roll_dice(dice_eyes, amount)
