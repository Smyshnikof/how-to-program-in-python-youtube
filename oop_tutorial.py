class Car:
    def __init__(self, mark, year):
        self.mark = mark
        self.year = year
        self.color = "Красный"
        self.is_running = False
    
    def info(self):
        print(f"Марка: {self.mark}. \n Год: {self.year} \n Цвет: {self.color} \n Двигатель: {self.is_running}")
        return self.mark, self.year, self.color, self.is_running
    
    
        
audi = Car("Audi", 2024)
print(audi.info())


bmw = Car("Bmw", 2000)
print(bmw.info())

print(bmw.mark)


