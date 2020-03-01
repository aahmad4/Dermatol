# Module being imported for current date and time
import datetime

# Creating a database allowing user credentials to be added to textfile
class DataBase:

    # Initializing the class
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    # Allowing the database to read the users.txt file
    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        # Defining the format of the txt file and how user credentials will be displayed
        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    # Saving the txt file with the user credentials
    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    # Allowing todays date to be shown when adding user credentials to txt file
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]