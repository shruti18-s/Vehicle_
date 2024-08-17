class Vehicle:
    def __init__(self, manufacturerName, milesOnVehicle, price, numberOfSeats, options):
        self.setManufacturerName(manufacturerName)
        self.setMilesOnVehicle(milesOnVehicle)
        self.setPrice(price)
        self.setNumberOfSeats(numberOfSeats)
        self.options = options

    def getManufacturerName(self):
        return self.manufacturerName

    def setManufacturerName(self, manuName):
        name = str(manuName)
        if len(name) > 15:
            raise ValueError("Vehicle manufacturer name must contain a string with less than 16 characters.")
        self.manufacturerName = manuName


    def getMilesOnVehicle(self):
        return self.milesOnVehicle

    def setMilesOnVehicle(self, miles):
        if not isinstance(miles, (int, float)) or miles < 0:
            raise ValueError("Vehicle miles on vehicle must be a non-negative number.")
        self.milesOnVehicle = miles

    def getPrice(self):
        return self.price

    def setPrice(self, price):
         if price <= 0:
            raise ValueError("Vehicle price must be a non-negative number.")
         self.price = price

    def getNumberOfSeats(self):
        return self.numberOfSeats

    def setNumberOfSeats(self, seats):

        if not isinstance(seats, int) or seats < 0:
            raise ValueError("Vehicle number of seats must be a non-negative whole number.")
        self.numberOfSeats = seats

    def getOptions(self):
        return self.options
