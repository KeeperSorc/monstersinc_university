from monstersinc_university import *

class Monster(Monstersinc_University):
    def __init__(self, name, age, legs, scary_look):
        self.__name = name
        self.__age = age
        self.__legs = legs
        self.__scary_look = scary_look

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_legs(self):
        return self.__legs

    def get_scary_look(self):
        return self.__scary_look

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_legs(self,legs):
        self.__legs = legs

    def set_scary_look(self,scary_look):
        self.__scary_look = scary_look

