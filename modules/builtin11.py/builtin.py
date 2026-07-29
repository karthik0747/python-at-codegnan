import random
steps=rolls=0
while True:
    input("to roll dicefor that click enter button")
    dice_val=random.randint(1,6)
    rolls+=1
    if steps +dice_val<=100:

        steps+=dice_val
    if steps==100:
        print(f"your reached top in {rolls} rolls")
        break
    print(f"for {rolls} rolls your {steps} position")
