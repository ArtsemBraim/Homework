class Sun:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = Sun()

        return cls._instance


if __name__ == "__main__":
    p = Sun.inst()
    f = Sun.inst()
    print(p is f)
