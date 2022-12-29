def amor(person):
    if person == "Pati":
        return f"Yo quiero a {person}"
    else:
        return f"No quiero a {person}, pero a Pati"

class Person:
    def __init__(self, name):
        self.name = name
