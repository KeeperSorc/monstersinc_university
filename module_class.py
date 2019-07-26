class Module():
    def __init__(self,subject,duration):
        self.__subject = subject
        self.__duration = duration

    def get_subject(self):
        return self.__subject

    def get_duration(self):
        return self.__duration