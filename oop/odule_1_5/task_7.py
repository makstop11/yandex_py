class Memory:
    """Класс оперативной памяти."""

    def __init__(self, name: str, volume: int) -> None:
        self.name = name
        self.volume = volume


class CPU:
    """Класс центрального процессора."""

    def __init__(self, name: str, frequency: int | float) -> None:
        self.name = name
        self.frequency = frequency


class MotherBoard:
    """Класс материнской платы."""

    def __init__(self, name: str, cpu: CPU, total_mem_slots: int):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots


if __name__ == "__main__":
    cpu_1: CPU = CPU("Intel 64x", 5.5)

    board = MotherBoard("MSI", cpu_1, 4)

    # TODO: дорешать
