class Angle():
    angleDegrees = None
    angleMinutes = None
    def __init__(self):
        #self.angle = ...       set to 0 degrees 0 minutes
        self.angleDegrees = 0
        self.angleMinutes = 0.0
    
    def setDegrees(self, degrees):
        self.angleDegrees = round(degrees)
        self.angleMinutes = (degrees - self.angleDegrees) * 60.0
    
    def setDegreesAndMinutes(self, degrees):
        if(len(degrees) == 0 | degrees == None):
            raise ValueError("No string entered")
        for i in degrees:
            if(i == "d" | i == 'd'):
                angleDegreesString = degrees[:i]
                angleMinutesString = degrees[i+1:]
                break    
        if(angleDegreesString == None):
            raise ValueError("No value found in the degrees field")
        if(angleMinutesString == None):
            raise ValueError("No value found in the minutes field")
        for i in angleDegreesString:
            if(i == "."):
                raise ValueError("Degrees value must be an integer")
        if(angleMinutesString[0] == "-"):
            raise ValueError("Minutes must be a positive value")
        try:
            self.angleDegrees = int(angleDegreesString)
        except:
            print("The degrees value was inputted incorrectly. Try again")
        try:
            self.angleDegrees = float(angleMinutesString)
        except:
            print("The minutes value was inputted incorrectly. Try again")
        self.angleModulo()
    
    def add(self, angle):
        self.angleDegrees += angle.angleDegress
        self.angleMinutes += angle.angleMinutes
        self.angleModulo()
    
    def subtract(self, angle):
        self.angleDegrees -= angle.angleDegress
        self.angleMinutes -= angle.angleMinutes
        self.angleModulo()
        pass
    
    def compare(self, angle):
        try:
            if(self.angleDegrees < angle.angleDegrees):
                return -1
            else if(self.angleDegrees == angle.angleDegrees && self.angleMinutes < angle.angleMinutes):
                return -1
            else if(self.angleDegrees == angle.angleDegrees && self.angleMinutes == angle.angleMinutes):
                return 0
            else if(self.angleDegrees == angle.angleDegrees && self.angleMinutes > angle.angleMinutes):
                return 1
            else:
                return 1
        except:
            print("Invalid instance of Angle")
    def getString(self):
        print("%dd%.1f",self.angleDegrees,self.angleMinutes)
    
    def getDegrees(self):
        if(self.angleDegrees<0)
            return self.angleDegrees-self.angleMinutes
        else
            return self.angleDegress+self.angleMinutes
    #implemented (internal) functions:
    def angleModulo(self):
        while(self.angleDegrees < 0):
            self.angleDegrees += 360
        while(self.angleDegrees > 360):
            self.angleDegrees -= 360
        while(self.angleMinutes > 60.0):
            self.angleMinutes -= 60
            self.angleDegrees += 1
        round(self.angleMinutes, 1)