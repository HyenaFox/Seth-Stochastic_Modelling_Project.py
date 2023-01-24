from random import *
from turtle import *
import pandas as pd
import csv

# TODO: RUN A MILLION TIMES, ALSO ADD ANIMATION
StartingTotal = 6500
CustomChange1 = randrange(-1000, 1000)
CustomChange2 = randrange(-1000, 1000)
CustomChange3 = randrange(-1000, 1000)
CustomChange4 = randrange(-1000, 1000)
CustomChange5 = randrange(-1000, 1000)
CustomChange6 = randrange(-1000, 1000)
CustomChange7 = randrange(-1000, 1000)
CustomChange8 = randrange(-1000, 1000)
CustomChange9 = randrange(-1000, 1000)

RealLifeChanges = [0, -650, 400, 700, -300, 350, -150, 250, -150, 850]

CustomChanges = [0, CustomChange1, CustomChange2, CustomChange3, CustomChange4, CustomChange5, CustomChange6,
                 CustomChange7, CustomChange8, CustomChange9]

NewData = {
    'Highway Segment': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    '6-7 CHANGE': [CustomChanges[0], CustomChanges[1], CustomChanges[2], CustomChanges[3], CustomChanges[4],
                   CustomChanges[5], CustomChanges[6], CustomChanges[7], CustomChanges[8], CustomChanges[9]]
}

NewData['6-7 TOTAL'] = [sum([StartingTotal] + NewData['6-7 CHANGE'][1:i + 1]) for i in
                        range(len(NewData['6-7 CHANGE']))]

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


# TODO: Comment out text "Reports", remake it with just numbers and then assign it to the dataframe to be added to the CSV
def CorrectForNextExit(Exit, OnRamp):
    NotEqual = len(CorrectCarList) != SixToSevenTotal[Exit]
    CarsRemaining = len(CorrectCarList)
    CarsGettingOffHere = []
    CarsGettingOnHere = []
    Reports = []
    Colors = 0
    GotOffCount = "No cars exited the highway."
    GotOnCount = "No Cars entered the highway."
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
            NumYellows = 0
            NumBlues = 0
            NumGreens = 0
            NumReds = 0
            NumPurples = 0
            NumberCarsGetOnHere = len(CarsGettingOnHere)
            for i in range(len(CarsGettingOnHere)):
                if CarsGettingOnHere[i][1] == "Yellow":
                    NumYellows += 1
                if CarsGettingOnHere[i][1] == "Blue":
                    NumBlues += 1
                if CarsGettingOnHere[i][1] == "Green":
                    NumGreens += 1
                if CarsGettingOnHere[i][1] == "Red":
                    NumReds += 1
                if CarsGettingOnHere[i][1] == "Purple":
                    NumPurples += 1
            CarsRemaining = len(CorrectCarList)
            Colors = [NumYellows, NumBlues, NumGreens, NumReds, NumPurples]
            GotOnCount = f"{NumberCarsGetOnHere} entered the highway."
            Reports = (f"At Exit Number {Exit}, "
                       f"{NumberCarsGetOnHere} cars entered the highway. \n"
                       f"Of the cars that got on, there were "
                       f"{NumYellows} yellow cars, {NumBlues} blue cars, "
                       f"{NumGreens} green cars, {NumReds} red cars, "
                       f"and {NumPurples} purple cars. \n"
                       f"There are now {CarsRemaining} cars on the highway.")

        if GreaterThanNeeded:
            Difference = len(CorrectCarList) - SixToSevenTotal[Exit]
            for i in range(Difference):
                CarLeaving = (CorrectCarList.pop())
                CarsGettingOffHere.append(CarLeaving)
            NumYellows = 0
            NumBlues = 0
            NumGreens = 0
            NumReds = 0
            NumPurples = 0
            NumberCarsGetOffHere = len(CarsGettingOffHere)
            for i in range(len(CarsGettingOffHere)):
                if CarsGettingOffHere[i][0][1] == "Yellow":
                    NumYellows += 1
                if CarsGettingOffHere[i][0][1] == "Blue":
                    NumBlues += 1
                if CarsGettingOffHere[i][0][1] == "Green":
                    NumGreens += 1
                if CarsGettingOffHere[i][0][1] == "Red":
                    NumReds += 1
                if CarsGettingOffHere[i][0][1] == "Purple":
                    NumPurples += 1
            Colors = [NumYellows, NumBlues, NumGreens, NumReds, NumPurples]
            CarsRemaining = len(CorrectCarList)
            Reports = (f"At Exit Number {Exit}, "
                       f"{NumberCarsGetOffHere} cars exited the highway. \n"
                       f"Of the cars that got off, there were "
                       f"{NumYellows} yellow cars, {NumBlues} blue cars, "
                       f"{NumGreens} green cars, {NumReds} red cars, "
                       f"and {NumPurples} purple cars. \n"
                       f"There are {CarsRemaining} cars remaining.")
            GotOffCount = f"{NumberCarsGetOffHere} cars exited the highway."
        if len(Reports) == 0:
            Colors = ("You'll never see this. And it's not because I don't want you to... just that this can't occur."
                      "You're in a dream, you know.")
            Reports.append(["You are at the last stop, which is theoretically impossible, because this code will "
                            "never reach this. It is a mathematical impossibility. This should be impossible, "
                            "this line is just here so that it prints... SOMETHING instead of an error. You know that "
                            "feeling, don't you, dear reader?"])
        return CorrectCarList, Reports, Colors, GotOnCount, GotOffCount, CarsRemaining

ResultDataIterable = {

}
ResultData = {
    'ColorReports': [],
    'EnterReports': [],
    ''
    
    'TextReports': []
}
for MyIterable in range(1, 10):
    FCarList = CorrectForNextExit(MyIterable, 1)
    ResultData['TextReports'].append(FCarList[1])

print(ResultData)


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
