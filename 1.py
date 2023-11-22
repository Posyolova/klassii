class Human:
    def __init__(self, n, a, h):
        print('Создан объект класса Human')
        self.__name=n
        self.__age=a
        self.__height=h
    
    def print(self):
        print(f'Имя:{self.__name}')
        print(f'Возраст:{self.__age}')
        print(f'Рост:{self.__height}')
     
    @property
    def name(self):
        return self.__name.upper()
        
    @name.setter    
    def name(self, n):
        self.__name=n.capitalize()
        
    
person1=Human("Полина", 17, 157)
person1.print()

person1.name='Дарья'
person1.print()
