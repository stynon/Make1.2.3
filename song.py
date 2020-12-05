#!/usr/bin/env python
"""
Info about our project comes here.
"""

# Import


__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


class Liedje:
    def __init__(self, tekst):
        self.tekst = tekst


    def zingen(self):
        count = 0
        for line in self.tekst:
            print(line.strip())


doc = input("Geef de naam van het document.\n")
doc = doc + ".txt"
file1 = open(doc)
tekst = file1.readlines()
verjaardagslied = Liedje(tekst)
verjaardagslied.zingen()

