import os
import math
import BMICalc

def contact():
    print("hello!\n")
    f = float(input("height in feet? (please type a whole number): "))
    i = float(input("now input the remainder of your height in inches: "))
    w = float(input("please input your height in pounds: "))
    h = (f*12.0 + i) * 0.025
    print("\nnow calculating...")
    bmiCalc = BMICalc.BMICalc(h,w)
    print("Your bmi value is " + str(bmiCalc.bmi_value()))
    print("You are " + bmiCalc.giveBMI())

contact()