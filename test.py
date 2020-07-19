class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoIsThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoIsThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

class Parrot:
    # class attribute
    species = "bird"

    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age

    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is dancing"

peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.run()