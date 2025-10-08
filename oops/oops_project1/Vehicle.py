from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Vehicle Management System (OOP in Python)
        We’ll model:
        Different types of vehicles (Car, Truck, ElectricCar)
        Common behavior (start, stop, info)
        Polymorphism (different vehicle types behave differently)
        Encapsulation (hide internal details)
        Abstraction (common interface for all vehicles)
    """
    def __init__(self,brand,model):
        self._brand = brand # protected (encapsulation)
        self._model = model # protected (encapsulation)
        
        
    @abstractmethod   
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def get_info(self):
        return f"Brand: {self._brand}, Model: {self._model}"
    
    
    
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.__fuel_type = fuel_type   # private (encapsulation)
        
    def start(self):
        print(f"{self.get_info()} with {self.__fuel_type} engine started.")

    
    def stop(self):
        print(f"{self.get_info()} stopped.")
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Fuel: {self.__fuel_type}"
    


class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.__battery_capacity = battery_capacity  # private (encapsulation)
        
    def start(self):
        print(f"{self.get_info()} with {self.__battery_capacity}kWh battery started silently.")
    
    def stop(self):
        print(f"{self.get_info()} stopped.")
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Battery Capacity: {self.__battery_capacity}kWh"
    


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.__load_capacity = load_capacity  # private (encapsulation)
        
    def start(self):
        print(f"{self.get_info()} with {self.__load_capacity} tons load capacity started.")
    
    def stop(self):
        print(f"{self.get_info()} stopped.")
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Load Capacity: {self.__load_capacity} tons"
    
    
    

def main():
    vehicles = [
        Car("Toyota", "Camry", "Gasoline"),
        ElectricCar("Tesla", "Model S", 100),
        Truck("Ford", "F-150", 5)
    ]
    
    for vehicle in vehicles:
        vehicle.start()
        print(vehicle.get_info())
        vehicle.stop()
        print("-" * 30)
        
if __name__ == "__main__":
    main()