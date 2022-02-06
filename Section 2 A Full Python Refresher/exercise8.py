#INHERITANCE

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
    def connect(self):
        self.connected = True


printer = Device("Printer", "USB")
print(printer)


# inherited class
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)  
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if self.remaining_pages == 0 or self.remaining_pages - pages < 0:
            raise TypeError("There are not enough pages left, fill paper please")
        if not self.connected:
            raise TypeError("Device is disconnected at this time, cannot print.")
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
    def add_pages(self,amount):
        self.remaining_pages += amount


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.print(50)
print(printer)
printer.disconnect()
printer.connect()
printer.print(120)
print(printer)
printer.print(310)
print(printer)
printer.add_pages(120)
print(printer)