class User:
    def __init__(self, id, name, level_user='user'):
        self.id = id
        self.name = name
        self.level_user = level_user

    def info(self):
        print(f"{self.id} - Id")
        print(f"{self.name} - имя пользователя")
        print(f"{self.level_user} - уровень - пользователь")

class Admin(User):
    def __init__(self, id, name, level_admin='admin'):
        super().__init__(id, name)
        self.level_admin = level_admin

    def info(self):
        # Расширяем метод info для отображения уровня администратора
        super().info()
        print(f"{self.level_admin} - уровень - администратор")

    def add_user(self, new_user_name):
        print(f"Добавлен новый пользователь - {new_user_name}")

    def remove_user(self, user):
        print(f"Пользователь - {user} - удален")


user1 = User(1, "Иван")
user1.info()

admin = Admin(2, "Анна")
admin.info()

admin.add_user("Пётр")
admin.remove_user("Иван")










