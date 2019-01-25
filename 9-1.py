class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number = 0

    def describe_restaurant(self):
        print(self.restaurant_name, '这家餐馆很不错！')
        print('记得常来！,我们主要经营：', self.cuisine_type)

    def open_reataurant(self):
        print('正在营业中......')

    def number_served(self):
        print('到目前为止，一共有' + str(self.number) + '人就过餐！')

    def set_number_served(self, increment_number):
        self.number = increment_number
        print('到目前为止,共有', increment_number, '人就过餐！')


a = Restaurant('滋味中餐', 'Chinese_food')
a.describe_restaurant()
a.open_reataurant()
a.number_served()
a.number = 100
a.number_served()
a.set_number_served(200)
a.set_number_served(300)


class IceCreamStand(Restaurant):        # 定义子类
    def __init__(self, restaurant_name, cuisine_type):  # 初始化父类属性
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['苹果味', '香蕉味', '草莓味']    # 添加子类的属性

    def show_flavors(self):
        for i in self.flavors:
            print('冰淇淋的口味有：', i)


b = IceCreamStand('每一天冰淇淋', '冰淇淋')
b.show_flavors()




