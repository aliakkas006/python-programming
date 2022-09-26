import random


class Person:
    # private method declaration:
    def __init__(self, name: str, email: str, password: int, hobby: str, marital_status: bool):
        self.__name = name  # private property declaration
        self.__email = email
        self.__password = password
        self.hobby = hobby  # public property declaration
        self.is_married = marital_status

    # public method declaration:
    def get_person_property(self):
        return self.__name, self.__email, self.__password, self.hobby, self.is_married


instance = Person("Ali Akkas", "ali@gmail.com", 12345, "football", False)
# print(instance.get_person_property())


class Student(Person):
    def __init__(
        self,
        name: str,
        email: str,
        password: int,
        hobby: str,
        marital_status: bool,
        student_id: int,
        class_name: str,
        home_town: str,
    ):
        super().__init__(name, email, password, hobby, marital_status)

        # added additional property:
        self.student_id = student_id
        self.class_name = class_name
        self.home_town = home_town

    def __str__(self):
        return (
            self.__name,
            self.__email,
            self.__password,
            self.hobby,
            self.is_married,
            self.student_id,
            self.class_name,
            self.home_town,
        )

    def __repr__(self):
        return (
            self.__name,
            self.__email,
            self.__password,
            self.hobby,
            self.is_married,
            self.student_id,
            self.class_name,
            self.home_town,
        )


instance_2 = Student(
    "Anis", "anis@gmail.com", 12354678, "tour", False, 254785, "b.pharma", "Chandpur"
)


# another lec.:
class People:
    def __init__(self, name, home):
        self.name = name      # instance variable
        self.home = home        # instance variable

    @property    # getter
    def name(self):
        return self._name

    @name.setter    # setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name!")
        self._name = name

    @property    #getter
    def home(self):
        return self._home

    @home.setter    #setter
    def home(self, home):
        if home not in ["Chandpur", "Khulna", "Dhaka"]:
            raise ValueError("Invalid house!")
        self._home = home

    def __str__(self):
        return f"{self.name} lives at {self.home}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        district = input("District: ")
        return cls(name, district)


def main():
    student = People.get()
    print(student)

if __name__ == '__main__':
    main()


class Hat:
    houses = ["Bari", "Ghor", "Dalan", "Kotha"]     # class variable

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Ali Akkas")


class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name!")
        self.name = name


class Learner(Wizard):          # inherit from Wizard
    def __init__(self, name, house):
        super().__init__(name)         # reference to the super class of this class
        self.house = house


class Professor(Wizard):        # inherit from Wizard
    def __init__(self, name, subject):
        super().__init__(name)      # reference to the super class of this class
        self.subject = subject


student = Learner("Ali Akkas", "Chandpur")
print(student.name)

