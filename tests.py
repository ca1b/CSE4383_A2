import pytest
import BMICalc


class TestClass:
    def test_bmiValue(self):
        bmiCalc = BMICalc.BMICalc(1.5,120)
        bmiValue = bmiCalc.bmi_value()

        assert bmiValue == 24

    def test_BMIUnderweight1(self):
        testBMI = BMICalc.BMICalc(1,41.111111)
        #BMI of 18.45
        assert testBMI.giveBMI() == "Underweight"
    def test_BMIUnderweight2(self):
        testBMI = BMICalc.BMICalc(1,40)
        #BMI of 18
        assert testBMI.giveBMI() == "Underweight"

    def test_BMINormalweight1(self):
        testBMI = BMICalc.BMICalc(1,18.5/0.45)

        assert testBMI.giveBMI() == "Normal weight"
    def test_BMINormalweight2(self):
        testBMI = BMICalc.BMICalc(1,166/3)
        #BMI of 24.9
        assert testBMI.giveBMI() == "Normal weight"

    def test_BMIOverweight1(self):
        testBMI = BMICalc.BMICalc(1,500/9)
        #BMI of 25
        assert testBMI.giveBMI() == "Overweight"
    def test_BMIOverweight2(self):
        testBMI = BMICalc.BMICalc(1,580/9)
        #BMI of 29
        assert testBMI.giveBMI() == "Overweight"

    def test_BMIObese1(self):
        testBMI = BMICalc.BMICalc(1,200/3)
        #BMI of 30
        assert testBMI.giveBMI() == "Obese"
    def test_BMIObese2(self):
        testBMI = BMICalc.BMICalc(1,100)
        #BMI of 45
        assert testBMI.giveBMI() == "Obese"