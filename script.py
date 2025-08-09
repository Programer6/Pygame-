class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password  
        self._email = email

    def clean_email(self):
        return self._email.replace(" ", "").lower()

User1 = User("user1", "password1", "duiheuidh")

print(User1.clean_email())
