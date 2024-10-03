# Jonathan Lee
# Purpose: Introduction the Object-Oriented Programming

# Import our person class
from bike import Bike

###############################################
# Instantiate a Person object
###############################################
try:

    specialized = Bike(numGear=15, currentGear=10, numWheels=2, brakeType="hand brakes")


    # Specialized
    # Now, instantiating a Person object with no information initially.
    # Then adding that information after the object has been created.
    #specialized = Bike()
    #specialized.setnumGear(15)
    #specialized.setcurrentGear(10)
    #specialized.setnumWheels(2)
    #specialized.setbrakeType("hand brakes")


    print("=====My New Bike Specs=====")
    print()
    print(f"Number of Gears: {specialized.getnumGear()}")
    print(f"Current Gear: {specialized.getcurrentGear()}")
    print(f"Number of wheels: {specialized.getnumWheels()}")
    print(f"Bike currently uses {specialized.getbrakeType()}")

    input("Press [ENTER] to continue \n")
    print()

    # Set Current Gear
    specialized.setcurrentGear(10)
    print(f"Current gear is set at {specialized.getcurrentGear()}.")
    print()

    # Increase Gear by 1
    input(f"Let's try to increase the gear by 1.")
    specialized.increaseGear()
    print(f"Gear increased by 1. New current gear is: {specialized.getcurrentGear()}")
    input("Press [ENTER] to continue \n")
    print()

    # Maximum Gear
    print(f"Let's take it to the max!")
    print(f"Gear increased by 1. New current gear is: {specialized.increaseGear()}")
    input("Let's do it again. \n")
    print(f"Gear increased by 1. New current gear is: {specialized.increaseGear()}")
    input("Keep going. \n")
    print(f"Gear increased by 1. New current gear is: {specialized.increaseGear()}")
    input("Almost there. \n")
    print(f"Gear increased by 1. New current gear is: {specialized.increaseGear()}")
    input("We're at top gear! Can we go higher? \n")
    print(f"Sorry, gear is at the max. Gear remains at: {specialized.increaseGear()}")
    print()


    # Minimum Gear
    input(f"Now let's try to decrease the gear below the minimum limit.")
    specialized.setcurrentGear(1)
    input(f"Current gear is reset to {specialized.getcurrentGear()}.")
    print()
    input(f"Can't go lower! Gear remains at: {specialized.decreaseGear()}")
    print()

    # Using "electric" brake type
    input(f"Finally, what happens if we try to change the brake type to 'electric'?")
    print()

    specialized.setbrakeType("electric")

    #except ValueError as e:
    print(f"Current brake type is {specialized.getbrakeType()}")
    print()

finally:
    print("Finished.")