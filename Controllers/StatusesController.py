from Models.Statuses import Statuses


class StatusesController(Statuses):
    def __init__(self,id,status):
        super().__init__(id,status)

    statuses = [] # Список (массив) в котором храняется словари  со значениями атрибутов классов Statuses
    #метод CRUD - методы создания, чтения (вывода), измения, удвление значения атрибутов

    # Метод создания
    def add(self):
        self.statuses.append({'id':self.id, 'status':self.status})  # в список statuses добавляется словарь
                                                                    # ключу id передаётся значения метода (геттера)
                                                                    # id (он выводит значения защищённого отрибута id)
                                            # в список statuses добавляется словарь
                                            # ключу id передаётся значения метода (геттера)
                                            # id (он выводит значения защищённого отрибута id)
    # метод вывода всех записей из записка statuses
    @property
    def get(self):
        for element in self.statuses:
            print(element)
