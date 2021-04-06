from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", capacity, memory)
        self.capacity = int(capacity * 2)
        self.memory = int(memory * 0.75)
