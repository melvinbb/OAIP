class Device:
    def __init__(self, power):
        self.power = power

    def turn_on(self):
        print(f"Turning on device with power {self.power}")


class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        super().__init__(power)
        self.ip_address = ip_address

    def connect(self):
        print(f"Connecting to network with IP address {self.ip_address}")


class PortableDevice(Device):
    def __init__(self, power, battery_level):
        super().__init__(power)
        self.battery_level = battery_level

    def charge(self):
        print(f"Charging device with battery level {self.battery_level}")


class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        # Явный вызов конструкторов родительских классов
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)

    def call(self):
        print("Making a phone call")


class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        super().__init__(power)
        self.ip_address = ip_address

    def connect(self):
        print(f"Connecting to network with IP address {self.ip_address}")

    def turn_on(self):
        print(f"Turning on networked device with power {self.power}")


class PortableDevice(Device):
    def __init__(self, power, battery_level):
        super().__init__(power)
        self.battery_level = battery_level

    def charge(self):
        print(f"Charging device with battery level {self.battery_level}")

    def turn_on(self):
        print(f"Turning on portable device with power {self.power}")


class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)

    def turn_on(self):
        print("Turning on smart phone:")
        NetworkedDevice.turn_on(self)
        PortableDevice.turn_on(self)

    def call(self):
        print("Making a phone call")


smartphone = SmartPhone(power=50, ip_address="192.168.1.100", battery_level=80)
smartphone.turn_on()
smartphone.connect()
smartphone.charge()
smartphone.call()
