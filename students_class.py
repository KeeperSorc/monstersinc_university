from monster_class import *

class Students(Monster):
    def __init__(self, student_id,skills):
        self.__student_id = student_id
        self.__skills = skills

    def get_student_id(self):
        return self.__student_id

    def get_skills(self):
        return self.get_skills()

    def set_student_id(self,student_id):
        self.__student_id = student_id

    def set_skills(self,skills):
        self.__skills = skills
