class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        return self.commands


class Pet(Animal):
    def __init__(self, name, birth_date, pet_type):
        super().__init__(name, birth_date)
        self.pet_type = pet_type


class PackAnimal(Animal):
    def __init__(self, name, birth_date, load_capacity):
        super().__init__(name, birth_date)
        self.load_capacity = load_capacity


class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def classify_animal(self, name, birth_date, animal_type, additional_info):
        if animal_type in ['Собака', 'Кошка', 'Хомяк']:
            animal = Pet(name, birth_date, pet_type=animal_type)
        elif animal_type in ['Лошадь', 'Верблюд', 'Осел']:
            animal = PackAnimal(name, birth_date, load_capacity=additional_info)
        else:
            print("Неизвестный тип животного.")
            return
        self.add_animal(animal)
        print(f"Животное {name} добавлено в реестр как {animal_type}.")

    def find_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        print(f"Животное с именем {name} не найдено.")
        return None

    def train_animal(self, name, command):
        animal = self.find_animal(name)
        if animal:
            animal.add_command(command)
            print(f"Животное {name} обучено команде: {command}")

    def show_animal_commands(self, name):
        animal = self.find_animal(name)
        if animal:
            commands = animal.list_commands()
            if commands:
                print(f"Список команд для {name}: {', '.join(commands)}")
            else:
                print(f"Животное {name} пока не знает команд.")

    def menu(self):
        while True:
            print("\nМеню:")
            print("1. Завести новое животное")
            print("2. Показать команды животного")
            print("3. Обучить животное новой команде")
            print("4. Выйти")
            choice = input("Выберите действие: ")
            if choice == '1':
                name = input("Введите имя животного: ")
                birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
                animal_type = input("Введите тип животного (Собака, Кошка, Хомяк, Лошадь, Верблюд, Осел): ")
                if animal_type in ['Лошадь', 'Верблюд', 'Осел']:
                    additional_info = input("Введите грузоподъемность (в кг): ")
                else:
                    additional_info = None
                self.classify_animal(name, birth_date, animal_type, additional_info)
            elif choice == '2':
                name = input("Введите имя животного: ")
                self.show_animal_commands(name)
            elif choice == '3':
                name = input("Введите имя животного: ")
                command = input("Введите новую команду: ")
                self.train_animal(name, command)
            elif choice == '4':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


class Counter:
    def __init__(self):
        self.count = 0
        self._in_context = False
        self._closed = False

    def add(self, fields_filled):
        if not self._in_context:
            raise RuntimeError("Counter должен использоваться в блоке 'with'.")
        if self._closed:
            raise RuntimeError("Ресурс уже закрыт.")
        if fields_filled:
            self.count += 1
        else:
            raise ValueError("Заполните все поля перед добавлением нового животного.")

    def close(self):
        if self._closed:
            raise RuntimeError("Ресурс уже закрыт.")
        self._closed = True

    def __enter__(self):
        self._in_context = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        self._in_context = False


if __name__ == "__main__":
    registry = AnimalRegistry()
    registry.menu()

    try:
        with Counter() as counter:
            fields_filled = True
            counter.add(fields_filled)
            print(f"Текущее значение счетчика: {counter.count}")

        counter.add(True)
    except RuntimeError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка заполнения полей: {e}")
