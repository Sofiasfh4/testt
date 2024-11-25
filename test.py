class Temperature:
    def __init__(self, temperature: float, unit: str):
        # Доступні одиниці вимірювання
        if unit not in {'K', 'C', 'F'}:
            print("Помилка: Невірна одиниця вимірювання. Використовуйте 'K', 'C' або 'F'.")
            return

        # Перевірка фізично допустимих значень
        if unit == 'C' and temperature < -273.15:
            print("Помилка: Температура у Цельсіях не може бути нижчою за -273.15 °C.")
            return
        elif unit == 'K' and temperature < 0:
            print("Помилка: Температура у Кельвінах не може бути нижчою за 0 K.")
            return
        elif unit == 'F' and temperature < -459.67:
            print("Помилка: Температура у Фаренгейтах не може бути нижчою за -459.67 °F.")
            return

        # Зберігаємо дані
        self.temperature = temperature
        self.unit = unit

    # Метод для конвертації в Кельвіни
    def to_kelvin(self):
        if self.unit == 'K':
            print("Температура вже в Кельвінах.")
            return

        if self.unit == 'C':
            self.temperature += 273.15
        elif self.unit == 'F':
            self.temperature = (self.temperature + 459.67) * 5 / 9

        self.unit = 'K'

    # Метод для конвертації в Цельсій
    def to_celsius(self):
        if self.unit == 'C':
            print("Температура вже в Цельсіях.")
            return

        if self.unit == 'K':
            self.temperature -= 273.15
        elif self.unit == 'F':
            self.temperature = (self.temperature - 32) * 5 / 9

        self.unit = 'C'

    # Метод для конвертації в Фаренгейти
    def to_fahrenheit(self):
        if self.unit == 'F':
            print("Температура вже у Фаренгейтах.")
            return

        if self.unit == 'C':
            self.temperature = self.temperature * 9 / 5 + 32
        elif self.unit == 'K':
            self.temperature = self.temperature * 9 / 5 - 459.67

        self.unit = 'F'

    # Метод для представлення об'єкта у вигляді рядка
    def __str__(self):
        return f"{self.temperature:.2f} °{self.unit}"


# Створення об'єкта Temperature
temp1 = Temperature(25, 'C')  # Температура у Цельсіях
print(temp1)  # Виведе: 25.00 °C

# Створення об'єкта з недопустимою температурою
temp2 = Temperature(-300, 'C')  # Температура нижче -273.15 °C

# Створення об'єкта з температурою 0°C та конвертація в Кельвіни
temp3 = Temperature(0, 'C')
temp3.to_kelvin()
print(temp3)  # Виведе: 273.15 °K