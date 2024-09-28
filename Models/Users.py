class Users:
    def __init__(self,id,login,password,phone,email,fullname,role_id ):
        self.__id = id
        self.__login = login
        self.__password = password
        self.__phone = phone
        self.__email = email
        self.__fullname = fullname
        self.__role_id = role_id


        @property
        def id(self):
            return self.__id

        def login(self):
            return self.__login

        def password(self):
            return self.__password

        def  phone(self):
            return self.__phone

        def email(self):
            return self.__email

        def fullname(self):
            return self.__fullname

        def rode_id(self):
            return self.__role_id

if __name__ == "__main__":
    Users_one = Users(1,"юсуфов690",16032,89004013454,"Yusufov_06@internet.ru","Юсуфов Фтрузджон","//html//")
    print(Users_one.__id, Users_one.__login, Users_one.__password, Users_one.__phone, Users_one.__email, Users_one.__fullname, Users_one.__role_id )
