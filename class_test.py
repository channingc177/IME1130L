# Experimenting with classes and operator hijacking

class Element:
    def __init__(self, iden):
        self.__ids = [
            "void",
            "water",
            "fire",
            "steam",
        ]
        self.set_id(iden)

    def set_id(self, user_in):
        if str(user_in).isdigit():
            self.__id = self.__ids[user_in] if 0 <= user_in <= \
                len(self.__ids) - 1 else self.__ids[0]
        else:
            self.__id = "void"

    def print_id(self):
        print(self.__id)

    def get_id(self):
        return self.__id

    def __add__(self, other_elem):
        return Element(3) if "water" in [self.get_id(), \
            other_elem.get_id()] and "fire" in [self.get_id(), \
            other_elem.get_id()] else Element(0)


def Main():
    elem1, elem2 = Element(2), Element(2)
    print(f"{elem1.get_id()} plus {elem2.get_id()} is {(elem1 + elem2).get_id()}.")

Main()