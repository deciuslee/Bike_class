#Create a Bike Class

#Properties
# Gear Number: getGearNum(), setGearNum()
# Current Gear: getcurrentGear(), setcurrentGear()
# Wheels: getWheels(), setWheels()
# Brakes: getBrakeType(), setBrakeType()

# Max Gear: max 15
# Min Gear: min 1

# Methods
# increaseGear()
# decreaseGear()
# resetGear()

# Define a class
class Bike:
    # Private properties
    __numGear: int = 1
    __currentGear: int = 1
    __numWheels: int = 2
    __brakeType: str = ""
    #__brakes = ["hand brakes" or "foot brakes"]

# Instantiate a copy of this class
    def __init__(self, numGear = 15, currentGear = 1, numWheels = 2, brakeType = "hand brakes" or "foot brakes"):

    # Set all properties
        self.setnumGear(numGear)
        self.setcurrentGear(currentGear)
        self.setnumWheels(numWheels)
        self.setbrakeType(brakeType)


# Getter and setter for the number of gears property
    def getnumGear(self) -> int:
        return self.__numGear

    def setnumGear(self, numGear: int) -> None:
        try:
            if 1 <= numGear <= 15:
                self.__numGear = int(numGear)
            else:
                print(f"Invalid gear selection. Number of gears will be reset to default {self.__numGear}")

        except Exception as e:
            print(f"Error has occurred: {e}")


# Getter and setter for the current gear property
    def getcurrentGear(self) -> int:
        return self.__currentGear

    def setcurrentGear(self, currentGear: int) -> None:
        try:
            if 1 <= currentGear <= 15:
                if currentGear <= self.__numGear:
                    self.__currentGear = int(currentGear)
                else:
                    print(f"The selected gear is beyond the bike's gear range. Your current gear will be "
                          f"reset to default of {self.__currentGear}.")

        except Exception as e:
            print(f"Error occurred: {e}")


# Getter and setter for the number of wheels property
    def getnumWheels(self) -> int:
        return self.__numWheels

    def setnumWheels(self, numWheels: int) -> None:
        try:
            if 1 <= numWheels <= 4:
                self.__numWheels = int(numWheels)

            else:
                print(f"Number of wheels entered is incorrect. "
                      f"Wheel number will be reset to default of {self.__numWheels}.")

        except Exception as e:
            print(f"Error has occurred: {e}")


# Getter and setter for the type of brakes property
    def getbrakeType(self) -> str:
        return self.__brakeType

    def setbrakeType(self, brakeType: str) -> None:
        try:
            if brakeType == "hand brakes" or brakeType == "foot brakes":
                self.__brakeType = brakeType

            else:
                print(f"Invalid brake type entered. Brake type must be 'hand brakes' or 'foot brakes.'")

        except Exception as e:
            print(f"Error has occurred: {e}")

# Reset Gear property to 1
    def resetGear(self):
        self.setcurrentGear(1)
        print(f"Current Gear reset to 1.")


# Increase Gear property (max = 15)
    def increaseGear(self) -> int:
        try:
            if 1 <= self.getcurrentGear() < self.getnumGear():
                self.setcurrentGear(self.getcurrentGear() + 1)

            else:
                print(f"Cannot shift gear above the maximum (15).")

            return self.getcurrentGear()

        except Exception as e:
            print(f"Error occurred: {e}")


# Decrease Gear property (min = 1)
    def decreaseGear(self) -> int:
        try:
            if 1 < self.getcurrentGear() <= self.getnumGear():
                self.setcurrentGear(self.getcurrentGear() - 1)

            else:
                print(f"Cannot shift gear below the minimum (1).")


            return self.getcurrentGear()

        except Exception as e:
            print(f"Error occurred: {e}")





