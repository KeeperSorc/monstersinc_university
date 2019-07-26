from module_class import *
from students_class import *
from lecturers_class import *

class Batch():
    def __init__(self,module,start_date,list_of_students):
        self.__module = module
        self.__start_date = start_date
        self.__list_of_students = list_of_students

    def get_module(self):
        return self.__module

    def get_start_date(self):
        return self.__start_date

    def get_list_of_students(self):
        return self.__list_of_students

    def set_module(self,module):
        self.__module = module

    def set_start_date(self,start_date):
        self.__start_date = start_date

    def set(self,list_of_students):
        self.__list_of_students = list_of_students