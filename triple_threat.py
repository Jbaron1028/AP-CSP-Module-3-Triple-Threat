"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Name - Month Year
"""

import random

def main() -> None:
    cost = 1
    base: int = 10
    #roll three dice 
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    prize = 0
    if dice1==dice2 and dice1==dice3:
        multiplier=dice1
        prize = multiplier*base
    profit = int(cost)-prize

    print (f"Casino collects: ${cost}")
    print (f"Player rolls:  {dice1}-{dice2}-{dice3}")
    print (f"Casino pays out: ${prize}")
    print (f"Profit: ${profit}")
    

if __name__ == "__main__":
    main()