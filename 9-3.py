class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('该用户姓名是：', self.first_name + self.last_name)

    def greet_user(self):
        print('Hello!', self.first_name + self.last_name, '很高兴认识你！')


a = User('谢', '晨')
a.describe_user()
a.greet_user()
