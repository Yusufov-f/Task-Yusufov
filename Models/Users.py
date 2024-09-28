# Данный класс задаёт атрибуты для сущности Пользователей
class Users:
    def __init__(self,id,login,password,number,email,fullname,role_id ):
        self.__id = id
        self.__login = login
        self.__password = password
        self.__phone = number
        self.__email = email
        self.__fullname = fullname
        self.__role_id = role_id


        @property
        def id(self):
            return self.__id
        @property
        def login(self):
            return self.__login
        @property
        def password(self):
            return self.__password
        @property
        def  number(self):
            return self.__number
        @property
        def email(self):
            return self.__email
        @property
        def fullname(self):
            return self.__fullname
        @property
        def rode_id(self):
            return self.__role_id

if __name__ == "__main__":
    ivan = Users(1,"юсуфов690",16032,89004013454,"Yusufov_06@internet.ru","Юсуфов Фтрузджон",1)
    print(ivan.number)
