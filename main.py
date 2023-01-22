from random import *
from turtle import *
import pandas as pd
import csv

# TODO: I have to basically make it so at the end of the day, the number of cars at each highway exit segment lines
#  up with real life
ProjectData = pd.read_csv('ProjectData.csv')
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


# def SubtractAtExit(ThisExit, TotalCarsList):
#     CarsGettingOffHere = []
#     IndicesToRemove = []
#     for i in range(len(TotalCarsList)):
#         if TotalCarsList[i][2] == ThisExit:
#             CarsGettingOffHere.append(TotalCarsList[i])
#             IndicesToRemove.append(i)
#     IndicesToRemove.sort(reverse=True)
#     for i in IndicesToRemove:
#         del TotalCarsList[i]
#     NumCarsGettingOffHere = len(CarsGettingOffHere)
#     return TotalCarList, CarsGettingOffHere, NumCarsGettingOffHere


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
    while NotEqual:
        NotEqual = len(CorrectCarList) != SixToSevenTotal[Exit]
        LessThanNeeded = len(CorrectCarList) < SixToSevenTotal[Exit]
        GreaterThanNeeded = len(CorrectCarList) > SixToSevenTotal[Exit]
        if LessThanNeeded:
            Difference = SixToSevenTotal[Exit] - len(CorrectCarList)
            for i in range(Difference):
                CorrectCarList.append(AddCar(Exit))
        if GreaterThanNeeded:
            Difference = len(CorrectCarList) - SixToSevenTotal[Exit]
            for i in range(Difference):
                CorrectCarList.pop()
    return CorrectCarList


CorrectCarList = CorrectForNextExit(3, 1)
print(len(CorrectCarList))

# while len(CorrectCarList) > SixToSevenTotal[1]:
#     Difference = len(CorrectCarList) - SixToSevenTotal[i]
#     for x in range(Difference):
#         CorrectCarList.pop()
#         i += 1
#         print("Kentucky")
#     if len(CorrectCarList) < SixToSevenTotal[i]:
#         Difference = SixToSevenTotal[i] - len(CorrectCarList)
#         print(Difference)
#         for x in range(Difference):
#             AddCar(i)
#         print("Brazil")
#     print("China")
#     i += 1



    #     while len(CorrectCarList) > SixToSevenTotal[i]:
    #         CorrectCarList.remove(CorrectCarList[1])
    #         print("China")
    #         print(len(CorrectCarList), SixToSevenTotal[i])
    #         CorrectCarList.append("China")
    # else:
    #     AddCar(i)
    #     print("Brazil")
    #     CorrectCarList.append("Brazil)")

# MAKE THIS WORK (line up with rl)


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


# def ListChangeReport(MaxSegments, FullCarList):
#     Reports = []
#     for i in range(MaxSegments):
#         CurrentSegmentNumber = i + 1
#         SubtractingThisTime = SubtractAtExit(i, FullCarList)
#         NumberCarsGetOffHere = SubtractingThisTime[2]
#         ExitingCarsList = SubtractingThisTime[1]
#         RemainingCarsList = SubtractingThisTime[0]
#         YellowCars = []
#         BlueCars = []
#         GreenCars = []
#         RedCars = []
#         PurpleCars = []
#         for i in range(len(ExitingCarsList)):
#             if ExitingCarsList[i][1] == "Yellow":
#                 YellowCars.append(ExitingCarsList[i])
#             if ExitingCarsList[i][1] == "Blue":
#                 BlueCars.append(ExitingCarsList[i])
#             if ExitingCarsList[i][1] == "Green":
#                 GreenCars.append(ExitingCarsList[i])
#             if ExitingCarsList[i][1] == "Red":
#                 RedCars.append(ExitingCarsList[i])
#             if ExitingCarsList[i][1] == "Purple":
#                 PurpleCars.append(ExitingCarsList[i])
#         TextReportAtI = (f"At Segment Number {CurrentSegmentNumber}, "
#         f"{NumberCarsGetOffHere} cars exited the highway. \n"
#         f"Of the cars that got off, there were "
#         f"{len(YellowCars)} yellow cars, {len(BlueCars)} blue cars, "
#         f"{len(GreenCars)}, green cars, {len(RedCars)}, red cars, and {len(PurpleCars)} purple cars. \n"
#         f"There are {len(RemainingCarsList)} cars remaining.")
#         Reports.append(TextReportAtI)
#     return Reports
#
#
# TextReports = ListChangeReport(10)
# for i in range(len(TextReports) - 1):
#     print(TextReports[i])

# CarsGotOffHere = SubtractingThisTime[2]
# NumberCarsGetOffHere = SubtractingThisTime[1]
# print(CarsGotOffHere, NumberCarsGetOffHere)
