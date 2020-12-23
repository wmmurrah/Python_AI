# reflex_vacuum_agent.py
"""From pseudocode on page 49 of 
AIMA 4"""

def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return print("Suck")
    elif location == "A":
        return print("Right")
    elif location == "B":
        return print("Left")
    else:
        return print("Error: Unknown input")


reflex_vacuum_agent("A", "Dirty")
reflex_vacuum_agent("B", "Dirty")
reflex_vacuum_agent("A", "Clean")
reflex_vacuum_agent("B", "Clean")
reflex_vacuum_agent("C", "Clean")

name = input("What is your name? ")
