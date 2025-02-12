# task 1

class ClassForTwoNums:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def display(self):
        print(f"a: {self.a}, b: {self.b}")

    def change(self, a: int, b: int):
        self.a = a
        self.b = b

    def sum(self) -> int:
        return self.a + self.b

    def max_value(self) -> int:
        return max(self.a, self.b)


nums = ClassForTwoNums(10, 20)
nums.display()
print("Сумма:", nums.sum())
print("Наибольшее значение:", nums.max_value(), "\n")




# task 2

class DecimalCounter:
    def __init__(self, min_value: int = 0, max_value: int = 10):
        self.min_value = min_value
        self.max_value = max_value
        self.current = min_value

    def increase(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            self.current = self.min_value

    def decrease(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            self.current = self.max_value

    def get_state(self) -> int:
        return self.current

counter = DecimalCounter(0, 5)
print("Текущее значение:", counter.get_state())
counter.increase()
counter.increase()
counter.increase()
print("Текущее значение:", counter.get_state())
counter.decrease()
print("Текущее значение:", counter.get_state())




# task 3

class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name: str, price: float):
        self.products[name] = price

    def remove_product(self, name: str):
        if name in self.products:
            del self.products[name]

    def find_product(self, name: str):
        return self.products.get(name, "Продукт не найден")


shop = Shop()
shop.add_product("Яблоко", 50)
shop.add_product("Банан", 30)
print("\nЯблоко: ", shop.find_product("Яблоко"))
shop.remove_product("Яблоко")
print("Яблоко: ", shop.find_product("Яблоко"), "\n")




# task 4

class MoneyBox:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v: int) -> bool:
        return self.coins + v <= self.capacity

    def add(self, v: int):
        if self.can_add(v):
            self.coins += v


money_box = MoneyBox(10)
print(money_box.can_add(5))
money_box.add(5)
print(money_box.coins)
print(money_box.can_add(6))