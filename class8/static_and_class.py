

class StaticAndClass:
    def __init__(self):
        self.name = "kuna"


    @staticmethod
    def static_method(name):
        print(name)
        return name

    @classmethod
    def class_method(cls, name):
        cls.static_method(name)
        cls.name = "rao"

    def print_name(self):
        print(self.name)

    def update_name(self):
        self.name = "overwritten name"



k = StaticAndClass()
k.static_method("rao")
k.class_method("one more")

print("*" * 15)
k.print_name()
print("*" * 5)



k.update_name()


print("*" * 15)
k.print_name()
print("*" * 5)