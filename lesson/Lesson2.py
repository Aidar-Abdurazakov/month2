# # Родительский класс
# class User:
#     def __init__(self, name, login, password):
#         self.name = name
#         self.login = login
#         self.password = password
#
#     def user_login(self, password):
#         if password == self.password:
#             return "Ok"
#         return "fail"
#
#
# # Дочерний класс
# class UserVIP(User):
#
#     def __init__(self, name, login, password, last_name, midle_name):
#         super().__init__(name, login, password)
#         self.last_name = last_name
#         self.midle_name = midle_name
#
#     def vip_login(self, name):
#         if name == self.name:
#             return "OK"
#         return "fail"
#
#     def user_login(self, login):
#         if login == self.login:
#             return "Правильно!!"
#         return "не верный логин!!"
#
#
# ardager = User("Ardager", "ardager@inbox.ru", "Def2638")
# john = UserVIP("John", "john_doe@list.ru", "Def2633", "Doe")
#
# print(john.last_name)
# # print(type(ardager))
# # print(type(john))
# # print(ardager.user_login("ardager@inbox.ru"))
# # print(john.user_login("john_doe@list.ru"))


class Swim:
    pass
    # def action(self):
    #     print("Swim")
class Fly:
    def action(self):
        print("Fly")
class Animal(Fly, Swim):
    pass
    # def action(self):
    #     print('step')
# donald_duck = Animal()
# donald_duck.action()
# print(Animal.__mro__ )

class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(A):
    def action(self):
        super().action()
        print("C")
class D(B, C):
    def action(self):
        super().action()
        print("D")

test_obj = D()
test_obj.action()
print(D.__mro__)