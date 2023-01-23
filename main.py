from random import *
from turtle import *
import pandas as pd
import csv

# TODO: MAKE IT GENERALIZABLE
StartingTotal = 3100
NewData = {
    'Highway Segment': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    '6-7 CHANGE': [0, -650, 400, 700, -300, 350, 0 - 150, 250, 0 - 150, 850],
}

NewData['6-7 TOTAL'] = [sum([StartingTotal] + NewData['6-7 CHANGE'][1:i+1]) for i in range(len(NewData['6-7 CHANGE']))]

print(NewData['6-7 TOTAL'])


df = pd.DataFrame(NewData)

df.to_csv("C:/Users/blaze/OneDrive/Documents/Seth - Stochastic Modelling Project/NewData.csv")
ProjectData = pd.read_csv('NewData.csv')

HighwaySegmentsList = ProjectData["Highway Segment"]
SixToSevenChanges = ProjectData["6-7 CHANGE"]
SixToSevenTotal = ProjectData["6-7 TOTAL"]
TotalCarList = []


# def CreateNewCarComplex(OnRamp, TotalExit, IntendedExits):
#     # Returns a list of cars with a specific exit of I-93 picked as their destination and as their entry point,
#     # values chosen at random to line up with real traffic data?
#     CarColor = randrange(0, 6)
#     if CarColor == 1:
#         CarColor = "Green"
#     if CarColor == 2:
#         CarColor = "Blue"
#     if CarColor == 3:
#         CarColor = "Red"
#     if CarColor == 4:
#         CarColor = "Yellow"
#     if CarColor == 5:
#         CarColor = "Purple"
#
#     # for random exits ExitChoice = randrange(OnRamp, TotalExit)
#     ExitChoice = IntendedExits
#
#     Car = [OnRamp, CarColor, ExitChoice]
#     return Car
def CreateNewCar(OnRamp):
    # Returns a list of cars with a specific exit of I-93 picked as their destination and as their entry point,
    # values chosen at random to line up with real traffic data?
    CarColor = randrange(1, 6)
    if CarColor == 1:
        CarColor = "Green"
    if CarColor == 2:
        CarColor = "Blue"
    if CarColor == 3:
        CarColor = "Red"
    if CarColor == 4:
        CarColor = "Yellow"
    if CarColor == 5:
        CarColor = "Purple"

    # for random exits ExitChoice = randrange(OnRamp, TotalExit)

    Car = [OnRamp, CarColor]
    return Car


# CurrentOnRamp = HighwaySegmentsList[0][0]
# CurrentOnRampPlus = int(CurrentOnRamp) + 1
MaxCars6To7 = SixToSevenTotal[1]


def AddCar(CurrentOnRamp):
    CarList = []
    NewCar = CreateNewCar(int(CurrentOnRamp))
    CarList.append(NewCar)
    return CarList


CorrectCarList = []
for i in range(2900):
    CorrectCarList.append(AddCar(0))


def CorrectForNextExit(Exit, OnRamp):
    NotEqual = len(CorrectCarList) != SixToSevenTotal[Exit]
    CarsGettingOffHere = []
    CarsGettingOnHere = []
    while NotEqual:
        # NotEqual = len(CorrectCarList) != SixToSevenTotal[Exit]
        LessThanNeeded = len(CorrectCarList) < SixToSevenTotal[Exit]
        GreaterThanNeeded = len(CorrectCarList) > SixToSevenTotal[Exit]
        if LessThanNeeded:
            Difference = SixToSevenTotal[Exit] - len(CorrectCarList)
            for i in range(Difference):
                NewCar = AddCar(OnRamp)
                NewCar = NewCar[0]
                CorrectCarList.append([NewCar])
                CarsGettingOnHere.append(NewCar)
            YellowCars = []
            BlueCars = []
            GreenCars = []
            RedCars = []
            PurpleCars = []
            NumberCarsGetOnHere = len(CarsGettingOnHere)
            for i in range(len(CarsGettingOnHere)):
                if CarsGettingOnHere[i][1] == "Yellow":
                    YellowCars.append(CarsGettingOnHere[i])
                if CarsGettingOnHere[i][1] == "Blue":
                    BlueCars.append(CarsGettingOnHere[i])
                if CarsGettingOnHere[i][1] == "Green":
                    GreenCars.append(CarsGettingOnHere[i])
                if CarsGettingOnHere[i][1] == "Red":
                    RedCars.append(CarsGettingOnHere[i])
                if CarsGettingOnHere[i][1] == "Purple":
                    PurpleCars.append(CarsGettingOnHere[i])
            NumPurples = len(PurpleCars)
            NumGreens = len(GreenCars)
            NumBlues = len(BlueCars)
            NumYellows = len(YellowCars)
            NumReds = len(RedCars)
            Reports = (f"At Exit Number {Exit}, "
                       f"{NumberCarsGetOnHere} cars entered the highway. \n"
                       f"Of the cars that got on, there were "
                       f"{NumYellows} yellow cars, {NumBlues} blue cars, "
                       f"{NumGreens} green cars, {NumReds} red cars, "
                       f"and {NumPurples} purple cars. \n"
                       f"There are now {len(CorrectCarList)} cars on the highway.")

        if GreaterThanNeeded:
            Difference = len(CorrectCarList) - SixToSevenTotal[Exit]
            for i in range(Difference):
                CarLeaving = (CorrectCarList.pop())
                CarsGettingOffHere.append(CarLeaving)
            YellowCars = []
            BlueCars = []
            GreenCars = []
            RedCars = []
            PurpleCars = []
            NumberCarsGetOffHere = len(CarsGettingOffHere)
            for i in range(len(CarsGettingOffHere)):
                if CarsGettingOffHere[i][0][1] == "Yellow":
                    YellowCars.append(CarsGettingOffHere[i])
                if CarsGettingOffHere[i][0][1] == "Blue":
                    BlueCars.append(CarsGettingOffHere[i])
                if CarsGettingOffHere[i][0][1] == "Green":
                    GreenCars.append(CarsGettingOffHere[i])
                if CarsGettingOffHere[i][0][1] == "Red":
                    RedCars.append(CarsGettingOffHere[i])
                if CarsGettingOffHere[i][0][1] == "Purple":
                    PurpleCars.append(CarsGettingOffHere[i])
            NumPurples = len(PurpleCars)
            NumGreens = len(GreenCars)
            NumBlues = len(BlueCars)
            NumYellows = len(YellowCars)
            NumReds = len(RedCars)
            Reports = (f"At Exit Number {Exit}, "
                       f"{NumberCarsGetOffHere} cars exited the highway. \n"
                       f"Of the cars that got off, there were "
                       f"{NumYellows} yellow cars, {NumBlues} blue cars, "
                       f"{NumGreens} green cars, {NumReds} red cars, "
                       f"and {NumPurples} purple cars. \n"
                       f"There are {len(CorrectCarList)} cars remaining.")
        return CorrectCarList, Reports


for MyIterable in range(1, 10):
    FCarList = CorrectForNextExit(MyIterable, 1)
    print(FCarList[1])

# def ListCreation():
#     for i in range(len(HighwaySegmentsList)):
#         CurrentExit = HighwaySegmentsList[i][0]
#         for x in range(SixToSevenChanges[i]):
#
#             AddCar(CurrentExit, )
#     # for i in range(SixToSevenChanges[CurrentOnRamp]):
#
#     # for i in range()
#
# # print(FullCarList)
