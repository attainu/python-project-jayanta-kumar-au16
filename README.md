# **PARKINGLOT**
Design a parkinglot using python with list data structure .

## **Dependies**
This code is only compatible with python 3
## **Description**
This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy approach while being parked in the slots.

**ParkingLot.py** file defines the following functions -
-

1. **create_parking_lot n** - Given n number of slots, create a parking lot

2. **park car_regno car_color** - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".

3. **status**- Prints the slot number, registration number and color of the parked vehicles.

4. **leave x** - Removes vehicle from slot number x
There are few query functions to retrieve slot number from registration number of car, get registration numbers of cars with particular color etc.1.

### **vehicle.py** 
This file contain only  class Car 




### **Main.py** 
This  file for execution the program ,by using  python built-in  **Open()**  function   for read and run all the commands from the 'Command.txt'  file. 

Run through **manual input** **-**

**OUTPUT**

*******************************
For manual input press : 1     
Execute through file press : 2 
*******************************
PRESS --> 1

 $ create_parking_lot 3

 $ park KA-01-HH-9999 White

Allocated slot number : 1

 $ park KA-01-BB-0001 Black

Allocated slot number : 2

 $ park KA-01-HH-7777 Red

Allocated slot number : 3

 $ leave 2

slot number 2 is free

 $ status

SLOT NO     &nbsp;     REGISTRATION NO  &nbsp;       COLOUR

1        &nbsp;  &nbsp; &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     KA-01-HH-9999   &nbsp;    &nbsp;   &nbsp; &nbsp;    White

3     &nbsp;  &nbsp; &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;           KA-01-HH-7777  &nbsp;&nbsp;&nbsp;        &nbsp;  &nbsp; Red

 $ park KA-01-P-333 White

Allocated slot number : 2

 $ registration_numbers_for_cars_with_colour White

KA-01-HH-9999  ,  KA-01-P-333

 $ exit





&nbsp;
&nbsp;

Run through **Command.txt** file



*******************************
For manual input press : 1

Execute through file press : 2
*******************************
PRESS --> 2

created a parking lot with 6 slots

Allocated slot number : 1

Allocated slot number : 2

Allocated slot number : 3

Allocated slot number : 4

Allocated slot number : 5

Allocated slot number : 6

slot number 4 is free

SLOT NO  &nbsp; &nbsp;        REGISTRATION NO&nbsp;&nbsp;&nbsp;&nbsp;        COLOUR

1  &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          KA-01-HH-1234  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         White

2  &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              KA-01-HH-9999   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;          White

3   &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                   KA-01-BB-0001   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;    &nbsp;         Black

5   &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                 KA-01-HH-2701   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;    &nbsp;              Blue

6   &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               KA-01-HH-3141   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;    &nbsp;                      Black

Allocated slot number : 4

Sorry , parking lot is full

KA-01-HH-1234  ,  KA-01-HH-9999  ,  KA-01-P-333

1  ,  2  ,  4

6

Not found