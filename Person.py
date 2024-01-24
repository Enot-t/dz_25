try:
    class Person:
        def __init__(self, name, age, email):
            self.__name = name
            self.__age = age
            self.__email = email

        def info(self):
            return f"Имя - {self.__name} \nВозраст - {self.__age} \ne-mail - {self.__email}"

        def set_name(self, n_name):
            self.__name = n_name
        def set_age(self, n_age):
            if n_age > 0:
                self.__age = n_age
                print(self.__age)
            else:
                print("Введите возраст больше 0")

        def set_email(self, n_email):
            self.__email = n_email

        def get_name(self):
            return self.__name

        def get_age(self):
            return self.__age

        def get_email(self):
            return self.__email

    person = Person("Tolik", 20,"tolik001@gmail.com" )
    n_age = int(input("Введите возраст: "))
    person.set_age(n_age)
except ValueError:
    print("Введите положительное целое число!")





