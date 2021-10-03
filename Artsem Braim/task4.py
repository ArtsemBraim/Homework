class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can fly")

    def __str__(self):
        return f"{self.name} can walk and fly"


class FlyingBird(Bird):

    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def __str__(self):
        return f"{self.name} can walk, fly and eat"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def __getattribute__(self, name):
        if name == "fly":
            raise AttributeError(f"{self.name!r} object has no attribute {name!r}")
        return super().__getattribute__(name)

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def swim(self):
        print(f"{self.name} bird can swim")

    def __str__(self):
        return f"{self.name} can walk, swim and eat"


class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name, ration="fish"):
        super().__init__(name, ration)

    def eat(self):
        print(f"It eats {self.ration}")

    def __str__(self):
        return f"{self.name} can walk, fly, swim and eat"


if __name__ == "__main__":
    a = Bird("Any")
    a.fly()
    b = FlyingBird("Canary")
    print(str(b))
    b.eat()
    c = NonFlyingBird("Penguin", "fish")
    c.eat()
    d = SuperBird("Gull")
    d.eat()
    print(d)
    c.fly()
