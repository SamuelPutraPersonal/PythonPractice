# This is the conveyor and sensor program
# The conveyor will move at a constant speed and the sensor will detect the package and stop the conveyor


class Conveyor:
    def __init__(self, conveyor_id, speed_rpm):
        self.conveyor_id = conveyor_id
        self.speed_rpm = speed_rpm
        self.is_running = False
        self.items_on_belt = []  # an empty list
        print(f"Conveyor {self.conveyor_id} created (Speed: {self.speed_rpm} rpm).")

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"Conveyor {self.conveyor_id} started.")
        else:
            print(f"Conveyor {self.conveyor_id} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"Conveyor {self.conveyor_id} stopped.")
        else:
            print(f"Conveyor {self.conveyor_id} is not running.")

    def add_item(self, item):
        if self.is_running:
            self.items_on_belt.append(item)
            print(f"Item {item} added to the conveyor belt.")
        else:
            print(f"Conveyor {self.conveyor_id} is not running. Cannot add item.")

    def print_item_list(self):
        if len(self.items_on_belt) > 0:
            print(f"Items on the {self.conveyor_id}. ")
            for item in self.items_on_belt:
                print(f"- {item}")

        else:
            print(f"No items on the {self.conveyor_id}.")

    def get_status(self):
        return {
            "conveyor_id": self.conveyor_id,
            "speed_rpm": self.speed_rpm,
            "is_running": self.is_running,
            "items_on_belt": self.items_on_belt,
        }


class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.is_active = False
        print(f"Sensor {self.sensor_id} created.")

    def power_on(self):
        if not self.is_active:
            self.is_active = True
            print(f"Sensor {self.sensor_id} powered on.")
        else:
            print(f"Sensor {self.sensor_id} is already active.")

    def power_off(self):
        if self.is_active == True:
            self.is_active = False
            print(f"Sensor {self.sensor_id} powered off.")
        else:
            print(f"Sensor {self.sensor_id} is already inactive.")

    def scan(self, conveyor):
        if self.is_active == True:
            if conveyor.is_running == True:
                if len(conveyor.items_on_belt) > 0:
                    item = conveyor.items_on_belt.pop(0)
                    print(f"Item {item} detected by Sensor {self.sensor_id}.")
                else:
                    print(f"No items detected by Sensor {self.sensor_id}.")
            else:
                print(f"Conveyor {conveyor.conveyor_id} is not running. Cannot scan.")
        else:
            print(f"Sensor {self.sensor_id} is inactive. Cannot scan.")


### Place to run the program
print("Welcome to the Conveyor and Sensor program")
if __name__ == "__main__":
    print("Starting The Conveyor QA Program")

    # Create our objects
    main_conveyor = Conveyor("S-ALPHA-001", 1000)
    sorting_sensor = Sensor("S-ALPHA-002")

    print("\n" + "=" * 50 + "\n")

    # This loop will keep running until the user chooses to exit
    while True:
        # Display the current status and options to the user
        print("\nCurrent Status:")
        print(main_conveyor.get_status)
        print(
            f"Sensor {sorting_sensor.sensor_id} Status: {'Active' if sorting_sensor.is_active else 'Inactive' }\n "
        )

        print("\nWhat would you like to do?")
        print("1: Start Conveyor")
        print("2: Stop Conveyor")
        print("3: Power On Sensor")
        print("4: Power Off Sensor")
        print("5: Add an Item to the Belt")
        print("6: Scan the next Item")
        print("7: Print Item List")
        print("8: Exit Program")

        choice = input("Enter your choice (1-7): ")
        print("\n" + "=" * 50 + "\n")

        # Use if/elif/else to run the correct method based on user choice
        if choice == "1":
            main_conveyor.start()
        elif choice == "2":
            main_conveyor.stop()
        elif choice == "3":
            item = input("Enter the item to add to the conveyor belt: ")
            main_conveyor.add_item(item)
        elif choice == "4":
            sorting_sensor.power_on()
        elif choice == "5":
            sorting_sensor.power_off()
        elif choice == "6":
            sorting_sensor.scan(main_conveyor)
        elif choice == "7":
            main_conveyor.print_item_list()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
