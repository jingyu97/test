class Person:
    count = 0
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        Person.count += 1

    def get(self):
        print("姓名是：{},年龄是：{}".format(self.Name,self.Age))

    def Count(self):
        print("count is {}".format(Person.count))

user1 = Person('张三',30)
user2 = Person('李四',40)
user1.get()
user2.get()
user1.Count()
user2.Count()

