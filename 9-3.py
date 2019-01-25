class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print('该用户姓名是：', self.first_name + self.last_name)

    def greet_user(self):
        print('Hello!', self.first_name + self.last_name, '很高兴认识你！')

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)


a = User('谢', '晨', 0)
a.describe_user()
a.greet_user()
a.increment_login_attempts()
a.increment_login_attempts()
a.increment_login_attempts()
a.reset_login_attempts()
