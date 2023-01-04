class bus:
    def __init__(self, name_person, source, destination,num_bus):
        self.counter = 0
        self.__name_person = name_person
        self.__source = source
        self.__destination = destination
        self.__num_bus=num_bus

        self.Counter = self.counter
        self.counter += 1

    def get_seat_id(self):
        return self.seat_id

    def get_name_person(self):
        return self.__name_person

    def get_source(self):
        all_source = ["Aka", "Haifa", "Yaffa", "Quds"]
        if self.__source in all_source :
            return self.__source
        else:
            print("You have Error writing source")
            return None

    def get_destination(self):
        all_destinations = ["Gaza", "Rafah", "Bureij", "Nuseirat"]

        if self.__destination in all_destinations:
            return self.__destination
        else:
            print("You have Error writing destination")
            return None

    def get_num_bus(self):
        all_num_bus = ["1", "2", "3", "4"]
        # all_num_bus = [1, 2, 3, 4]
        if self.__num_bus in all_num_bus:
            return self.__num_bus
        else:
            print("You have Error writing num_bus")
            return None

    def validate_source_destination_all_num_bus(self):
        all_destinations = ["Gaza", "Rafah", "Bureij", "Nuseirat"]
        all_source = ["Aka", "Haifa", "Yaffa", "Quds"]
        all_num_bus = ["1", "2", "3", "4"]
        if self.__source in all_source and self.__destination in all_destinations and self.__num_bus in all_num_bus:
            return True
        else:
            return False

    def Reserve_seat(self):
        if self.validate_source_destination_all_num_bus() == True:
            self.seat_id=self.__num_bus[0]+self.__source[0]+self.__destination[0]+"0"+str(self.Counter)
            print("seat id will be: " + self.seat_id)
        else:
            return False



class records :
    seats = []

    def __init__(self, inst_name, instr_number):
        self.inst_name = inst_name
        self.instr_number = instr_number


    def add_Reserve_seat(self,seats):
        name_person=input("Enter your name : ")
      #  print("bus1  ", "bus2", "bus3", "bus4")
        print("1 :Gaza to Aka " ,"2 :Rafah to Haifa " )
        print("3 :Bureij to Yaffa " ,"4 :Nuseirat to Quds " )
        num_bus=input("chosie the number bus")
        print("Aka", "Haifa", "Yaffa", "Quds")
        source = input("Enter the your source : ")
        print("Gaza", "Rafah", "Bureij", "Nuseirat")
        destination = input("Enter the your destination : ")
        s1=bus(name_person, source, destination,num_bus)
        seats.append(s1)
        print("The name in bus added succesfully", s1.Reserve_seat())

      # name_person = input("Enter your name : ")
      # print("bus1 : ", "bus2", "bus3", "bus4")
      # in_bus=int(input("Enter number "))
      #   if in_bus == 1:
      #       print("")




    def search_seats(self,seats):
        if len(seats)==0:
            print("You dont have Reserve seat yet, please add  Reserve seat")
        else:
            set=input("Enter the set id: ")
            found=0
            for s in seats:
                if s.get_seat_id() == set:
                    found=1
                    print("The Reserve seat is ", s.get_name_person())
            if found==0:
                print("Reserve_seat doesn't exist, please try again")


    def diplay_all_seats(self,seats):
        if len(seats)==0:
            print("You dont have seat yet, please add  seat")
        else:
            for  s in seats:
                 print("The seat is ", s.get_name_person(), "seat id ", s.get_seat_id())

    def diplay_all_Bus_trips(self, seats):
        if seats== 0:
            print("You dont have trips yet, please add  trips")
        else:
            for s in seats:
                print("The trips moving on is ", s.get_source()," to" , s.get_destination() , " bus number " , s.get_num_bus())


def menu():
    print("Enter 1 if you want to add Reserve seat : ")
    print("Enter 2 if you want to search a seats: ")
    print("Enter 3 if you want to diplay all_seats: ")
    print("Enter 4 if you want to diplay all Bus trips: ")
    print("Enter 5 if you want to exit: ")

print("Account login")
print("user : bus  " , "pass : bus ")
in_user_name=input("Enter user name ")
in_passw=input("Enter password ")
in_name=input("Enter your name ")
nm=in_name
if in_user_name == in_passw :
    print("Thanks log in : ", nm )

else:
    print("wrong account ,please try again : " , nm)

obj=records(in_user_name,in_passw)
menu()
while(True):
    choice = int(input("Choose a number "))

    if choice==1:
        obj.add_Reserve_seat(records.seats)
        menu()

    elif choice==2:
        obj.search_seats(records.seats)
        menu()

    elif choice==3:
        obj.diplay_all_seats(records.seats)
        menu()

    elif choice==4:
        obj.diplay_all_Bus_trips(records.seats)
        menu()

    elif choice==5:
        break
    else:
        print("Wrong choice, please try again ")
        menu()

