#!/usr/bin/env python
"""
Maak een functie die data (bv. van een sensor) in een lijst stopt. Er worden steeds 20 items in de lijst gestoken,
het gemiddelde print je af. Zorg dat je de loop kan onderbreken met een door jou gekozen symbool/letter/nummer/...
"""

# Import
import random

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"



def main():
    while True:
        list = random.sample(range(0, 30), 20)
        print(list)
        value = list
        addition = sum(value)
        length = len(value)
        average = addition/length
        print(average)
        if input("Press enter to get a new list, press q to quit\n") == "q":
            break

if __name__ == '__main__':  # code to execute if called from command-line
    main()
