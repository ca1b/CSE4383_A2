import math

class BMICalc:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight * 0.45

    def bmi_value(self):
        bmi_value = self.weight / (self.height ** 2)
        return bmi_value
    
    def giveBMI(self):
        bmi_value = self.bmi_value()
        if bmi_value < 18.5:
            return "Underweight"
        elif bmi_value < 25.0:
            return "Normal weight"
        elif bmi_value < 30:
            return "Overweight"
        else:
            return "Obese"