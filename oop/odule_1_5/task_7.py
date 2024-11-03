class Memory:
    """Класс оперативной памяти."""

    def __init__(self, name: str, volume: int) -> None:
        self.name = name
        self.volume = volume  # объём памяти


class CPU:
    """Класс центрального процессора."""

    def __init__(self, name: str, frequency: int | float) -> None:
        self.name = name
        self.frequency = frequency  # тактовая частота


class MotherBoard:
    """Класс материнской платы."""

    def __init__(self, name: str, cpu: CPU, total_mem_slots: int):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = [
            Memory("Model", 8)
            for _ in range(1, self.total_mem_slots + 1)
        ]

    def _get_memory_slots(self) -> str:
        mems = [
            f'{memory.name} - {memory.volume}'
            for memory in self.mem_slots
        ]
        return '; '.join(mems)

    def get_config(self) -> list[str]:
        return [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.frequency}',
            f'Слотов памяти: {self.total_mem_slots}',
            f'Память: {self._get_memory_slots()}',
        ]


if __name__ == "__main__":
    cpu_1: CPU = CPU("Intel 64x", 5.5)

    mother_board = MotherBoard("MSI", cpu_1, 2)

    print(mother_board.get_config())
