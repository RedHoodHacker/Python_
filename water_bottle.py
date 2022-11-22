#!/usr/bin/python3


water_bottle = 0 

quantity = int(input("You don't know how much you can fill the water bottle, see how far you can fill it without spilling, give me a quantity: "))
measurement = input("What is the measurement you want to use? ")



def fill(quantity, measurement):
    for x in range(quantity):
        quantity += water_bottle
    
    print("You poured", str(water_bottle) + " " + measurement, "Into the water bottle! Nice!")


fill(quantity, measurement)
    
