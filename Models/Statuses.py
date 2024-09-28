# Данный класс создан для обработки сущности статус заявление

class Statuses:
    def __init__(self,id,status):
        self.__id = id
        self.__status = status

    @property
    def id(self):
        return self.__id
    @property
    def status(self):
        return self.__status

if __name__ == "__main__":
    status_one = Statuses(1,status="новое заявление")
    print(status_one.__id, status_one.__status)
    status_one.id = 2
    print(status_one.__id, status_one.__status)
