class Person:
    # private method declaration:
    def __init__(
        self, name: str, email: str, password: int, hobby: str, marital_status: bool
    ):
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

        # added additional property added:
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
