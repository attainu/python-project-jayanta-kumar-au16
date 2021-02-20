from Vehicle import Car


class ParkingLot:

    def __init__(self):
        self.capacity = 0
        self.slot_num = 0
        self.Occupied_slots = 0

    def Create_parking_lot(self, capacity):
        self.slots = [-1]*capacity
        self.capacity = capacity
        return self.capacity

    def empty_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, reg_no, colour):
        if self.Occupied_slots < self.capacity:
            slot_id = self.empty_slot()
            self.slots[slot_id] = Car(reg_no, colour)
            self.slot_id = slot_id + 1
            self.Occupied_slots = self.Occupied_slots + 1
            return slot_id + 1
        else:
            return -1

    def leave(self, slot_id):
        if self.Occupied_slots > 0 and self.slots[slot_id-1] != -1:
            self.slots[slot_id-1] = -1
            self.Occupied_slots = self.Occupied_slots-1
            return True
        else:
            return False

    def status(self):
        print("SLOT NO \t REGISTRATION NO \t COLOUR")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1)
                      + "\t\t"
                      + str(self.slots[i].reg_no)
                      + "\t\t"
                      + str(self.slots[i].colour))
            else:
                continue

    def getRegNoFromColour(self, colour):
        Reg = []
        for i in self.slots:
            if i == -1:
                continue
            if i.  colour == colour:
                Reg.append(i.reg_no)
        return Reg

    def getSlotNoFromRegNO(self, reg_no):
        for i in range(len(self.slots)):
            if self.slots[i].reg_no == reg_no:
                return i+1
            else:
                continue
        return -1

    def getSlotNoFromColour(self, colour):
        slots = []
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].colour == colour:
                slots.append(str(i+1))
        return slots

    def show(self, line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.Create_parking_lot(n)
            print(f"created a parking lot with {str(res)} slots")
        elif line.startswith("park"):
            reg_no = line.split(' ')[1]
            colour = line.split(' ')[2]
            res = self.park(reg_no, colour)
            if res == -1:
                print("Sorry , parking lot is full")
            else:
                print(f"Allocated slot number : {str(res)}")
        elif line.startswith("leave"):
            leave_slot = int(line.split(' ')[1])
            cur_status = self.leave(leave_slot)
            if cur_status:
                print(f"slot number {str(leave_slot)} is free")
        elif line.startswith("status"):
            self.status()
        elif line.startswith("registration_numbers_for_cars_with_colour"):
            colour = line.split(' ')[1]
            reg = self.getRegNoFromColour(colour)
            print('  ,  ' .join(reg))
        elif line.startswith("slot_numbers_for_cars_with_colour"):
            colour = line.split(' ')[1]
            slotid = self.getSlotNoFromColour(colour)
            print('  ,  ' .join(slotid))
        elif line.startswith("slot_number_for_registration_number"):
            reg = line.split(' ')[1]
            slots = self.getSlotNoFromRegNO(reg)
            if slots == -1:
                print("Not found")
            else:
                print(slots)
        elif line.startswith("exit"):
            exit(0)
