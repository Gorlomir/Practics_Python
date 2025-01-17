class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
        else:
            raise ValueError("Пароли не совпадают")

    @staticmethod
    def validate_password(password):
        if len(password) < 8 or len(password) > 14:
            return False

        has_digit = any(char.isdigit() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)

        return has_digit and has_uppercase and has_lowercase

    def set_password(self, password):
        if self.validate_password(password):
            self.password = password
        else:
            raise ValueError("Пароль не соответствует требованиям")


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Hello! Choice: \n1 - Login\n2 - Sing Up\n")

        if choice == '1':
            # Логика входа
            pass
        elif choice == '2':
            username = input("Enter your login: ")

            password = input("Enter your password: ")
            password_confirm = input("Repeat your password: ")

            try:
                user = User(username, password, password_confirm)

                print("\nТребования к паролю:")
                print("1. Минимальная длина: 8 символов")
                print("2. Максимальная длина: 14 символов")
                print("3. Содержать хотя бы одну цифру")
                print("4. Содержать хотя бы одну заглавную букву")
                print("5. Содержать хотя бы одну строчную букву")

                if user.validate_password(password):
                    database.add_user(user.username, user.password)
                    print(f"Пользователь {username} успешно добавлен.")
                    break
                else:
                    print("Пароль не соответствует требованиям. Попробуйте еще раз.")
            except ValueError as e:
                print(str(e))
        else:
            print("Неверный выбор. Попробуйте еще раз.")
print(database.data)