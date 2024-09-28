from psutil import users  # Данный класс описывает методи для значений атрибутов сущности Пользователей
 from Models.Users import Users

 class UsersController(Users):
        def __init__(self,id,login,password,number,email,fullname,role_id ):
            super().__init__(id, login, password, number, email, fullname, role_id )
        # список пользователей
        users = []
        # методы Регистрации, Авторизации, Вывод польного имени
        # метод Регистрации - добавляет значения атрибутов объекта в список users
        def add(self):
            self.users.append(
                {
                            'id':self.id,
                            'login':self.login,
                            'password':self.password,
                            'number':self.number,
                            'email':self.email,
                            'fullname':self.fullname,
                            'role_id':self.role_id
                    

                }
            )

        @staticmethod
        def


  if __name__ == "__main__":
    users_1 = UsersController (1,
                               'ivan',
                               '4123455',
                               444444,
                               'Ivan@iv.iv',
                               'Ivanov Ivan',
                               1)
    users_1.add()
    UsersController.get()
    users_2 = UsersController(2,
                              'Peter',
                              "13246543554",
                              333333,
                              "Peter@pet.pet",
                              "Peter Petrov",
                              2)
    users_2.add()
    print("___________")
    UsersController.get()
    UsersController.login_users('Peter','1234562')




