class User:
    def __init__(self, id, name, level_user='user'):
        self.__id = id  # Приватный атрибут
        self.__name = name  # Приватный атрибут
        self.__level_user = level_user  # Приватный атрибут

    # Геттеры
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_level_user(self):
        return self.__level_user

    # Сеттеры
    def set_name(self, name):
        self.__name = name


    def set_level_user(self, level_user):
        self.__level_user = level_user

    # Метод для отображения информации о пользователе
    def info(self):
        print(f"{self.__id} - Id")
        print(f"{self.__name} - имя пользователя")
        print(f"{self.__level_user} - уровень - пользователь")


class Admin(User):
    def __init__(self, id, name, level_admin='admin'):
        super().__init__(id, name)
        self.__level_admin = level_admin  # Приватный атрибут

    # Геттеры
    def get_level_admin(self):
        return self.__level_admin

    # Сеттеры
    def set_level_admin(self, level_admin):
        self.__level_admin = level_admin

    # Расширенный метод info для отображения уровня администратора
    def info(self):
        super().info()
        print(f"{self.__level_admin} - уровень - администратор")

    # Метод для добавления нового пользователя
    def add_user(self, new_user_name):
        print(f"Добавлен новый пользователь - {new_user_name}")

    # Метод для удаления пользователя
    def remove_user(self, user_name):
        print(f"Пользователь - {user_name} - удален")

user1 = User(1, "Иван")
user1.info()

# Изменяем имя пользователя через сеттер
user1.set_name("Сергей")
user1.info()

# Создаем администратора
admin = Admin(2, "Анна")
admin.info()

# Добавляем нового пользователя через администратора
admin.add_user("Пётр")

# Удаляем пользователя через администратора
admin.remove_user("Иван")









