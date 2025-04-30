from abc import ABC, abstractmethod


# Implementacja
class Device(ABC):
    def __init__(self):
        self.is_on = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Television(Device):
    def turn_on(self):
        if not self.is_on:
            print("Tv turned on")
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            print("Tv turned off")
            self.is_on = False

class Radio(Device):
    def turn_on(self):
        if not self.is_on:
            print("Radio turned on")
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            print("Radio turned off")
            self.is_on = False

# Abstrakcja
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()


tv = Television()
radio = Radio()

tv_remote = RemoteControl(tv)
radio_remote = RemoteControl(radio)

tv_remote.toggle_power()
tv_remote.toggle_power()

radio_remote.toggle_power()
radio_remote.toggle_power()