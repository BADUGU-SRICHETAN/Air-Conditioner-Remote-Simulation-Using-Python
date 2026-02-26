#!/usr/bin/env python
# coding: utf-8

# In[1]:


class AirConditioner:

    def __init__(self):
        self.__power = False
        self.__temperature = 24
        self.__mode = "Cool"
        self.__fan_speed = "Medium"
        self.__swing = False

    def power_toggle(self):
        self.__power = not self.__power
        state = "ON" if self.__power else "OFF"
        print(f"AC is now {state}")

    def increase_temp(self):
        if self.__power:
            if self.__temperature < 30:
                self.__temperature += 1
                print("Temperature Increased:", self.__temperature)
            else:
                print("Maximum temperature reached!")
        else:
            print("Turn ON the AC first!")

    def decrease_temp(self):
        if self.__power:
            if self.__temperature > 16:
                self.__temperature -= 1
                print("Temperature Decreased:", self.__temperature)
            else:
                print("Minimum temperature reached!")
        else:
            print("Turn ON the AC first!")

    def change_mode(self):
        if self.__power:
            modes = ["Cool", "Heat", "Fan", "Dry"]
            current_index = modes.index(self.__mode)
            self.__mode = modes[(current_index + 1) % len(modes)]
            print("Mode changed to:", self.__mode)
        else:
            print("Turn ON the AC first!")

    def change_fan_speed(self):
        if self.__power:
            speeds = ["Low", "Medium", "High"]
            current_index = speeds.index(self.__fan_speed)
            self.__fan_speed = speeds[(current_index + 1) % len(speeds)]
            print("Fan Speed:", self.__fan_speed)
        else:
            print("Turn ON the AC first!")

    def toggle_swing(self):
        if self.__power:
            self.__swing = not self.__swing
            state = "ON" if self.__swing else "OFF"
            print("Swing is", state)
        else:
            print("Turn ON the AC first!")

    def display_status(self):
        print("\n----- AC STATUS -----")
        print("Power:", "ON" if self.__power else "OFF")
        print("Temperature:", self.__temperature)
        print("Mode:", self.__mode)
        print("Fan Speed:", self.__fan_speed)
        print("Swing:", "ON" if self.__swing else "OFF")
        print("----------------------\n")


# In[3]:


ac = AirConditioner()

while True:
    print("1. Power ON/OFF")
    print("2. Increase Temperature")
    print("3. Decrease Temperature")
    print("4. Change Mode")
    print("5. Change Fan Speed")
    print("6. Toggle Swing")
    print("7. Display Status")
    print("8. Exit")

    choice = input("Enter choice: ")
    print("-----------------------------------------")

    if choice == "1":
        ac.power_toggle()
    elif choice == "2":
        ac.increase_temp()
    elif choice == "3":
        ac.decrease_temp()
    elif choice == "4":
        ac.change_mode()
    elif choice == "5":
        ac.change_fan_speed()
    elif choice == "6":
        ac.toggle_swing()
    elif choice == "7":
        ac.display_status()
    elif choice == "8":
        print("Exiting Remote...")
        break
    else:
        print("Invalid choice!")


# In[ ]:




