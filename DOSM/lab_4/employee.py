from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, base_rate, position):
        self.name = name
        self.base_rate = base_rate
        self.position = position

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_info(self):
        print(f"Сотрудник: {self.name}({self.position}). Зарплата: {self.calculate_salary()}.")

    @abstractmethod
    def work(self):
        pass

    def promote(self, increase):
        self.base_rate += increase


class Manager(Employee, ABC):
    def __init__(self, name, base_rate):
        super().__init__(name, base_rate, "Менеджер")

    def calculate_salary(self):
        return self.base_rate * 1.5

    def work(self):
        print("Организует работу команды.")


class Developer(Employee, ABC):
    def __init__(self, name, base_rate):
        super().__init__(name, base_rate, "Разработчик")

    def calculate_salary(self):
        return self.base_rate + 500

    def work(self):
        print("Пишет код и исправляет ошибки.")


employees = [
    Manager("Иван", 5000),
    Developer("Анна", 5000),
    Manager("Ольга", 6000),
    Developer("Петр", 4500)
]

employees[0].promote(500)

for emp in employees:
    emp.get_info()
    emp.work()
