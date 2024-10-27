class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class CPU:
    pass


class MotherBoard:
    def __init__(self, name, cpu, mems):
        self.name = name
        self.cpu = cpu
        self.mems = mems
