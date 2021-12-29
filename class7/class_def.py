
class KunaClass(object):
    def __init__(self):
        self.name = "kuna"
        self.gender = "male"

    #
    # def __new__(cls):
    #     return
    #

    def printname(self):
        print(self.name)

    def printgender(self):
        print(self.gender)


# fun = KunaClass()
# print(dir(fun))
# fun.printgender()
# fun.printname()

class RaoClass(KunaClass):
    def __init__(self):
        super().__init__()

    def printgender(self):
        print(self.name)


fun = RaoClass()
print(dir(fun))
fun.printgender()


# initially we will have a config (json)
# user config will overwrite our config

# cpu = 2, ram= 4, region= ap-south-1


