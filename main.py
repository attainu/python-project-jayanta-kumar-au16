from parkinglot import ParkingLot


if __name__ == "__main__":
    print("*******************************")
    print("For manual input press : 1\nExecute through file press : 2")
    print("*******************************")
    user = input("PRESS --> ")
    print()
    parkinglot = ParkingLot()
    if user == "1":
        while True:
            line = input(" $ ")
            parkinglot.show(line)
    elif user == "2":
        File = open("Command.txt", "r")
        for line in File:
            line = line.rstrip('\n')
            parkinglot.show(line)
