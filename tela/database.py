import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        with open(self.filename, "r") as file:
            for line in file:
                email, password, name, created = line.strip().split(";")
                self.users[email] = (password, name, created)

    def get_user(self, email):
        return self.users.get(email, None)

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), self.get_date())
            self.save()
            return 1
        else:
            print("Email Inválido")
            return -1

    def validate(self, email, password):
        user = self.get_user(email)
        if user:
            return user[0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as file:
            for email, user_info in self.users.items():
                password, name, created = user_info
                file.write(f"{email};{password};{name};{created}\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
