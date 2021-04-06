from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_exist = [h for h in System._hardware if h.NAME == hardware_name]
        if not hardware_exist:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware_exist[0].install(express_software)
            System._software.append(express_software)
        except Exception as context:
            return str(context)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_exist = [h for h in System._hardware if h.NAME == hardware_name]
        if not hardware_exist:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware_exist[0].install(light_software)
            System._software.append(light_software)
        except Exception as context:
            return str(context)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_exist = [hardware for hardware in System._hardware if hardware_name == hardware.NAME]
        software_exist = [software for software in System._software if software_name == software.NAME]
        if hardware_exist and software_exist:
            hardware_exist[0].uninstall(software_exist[0])
            System._software.remove(software_exist[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        hardware_components = len(System._hardware)
        software_components = len(System._software)

        total_memory = 0
        for hardware in System._hardware:
            total_memory += hardware.MEMORY

        total_capacity = 0
        for hardware in System._hardware:
            total_capacity += hardware.CAPACITY

        total_free_memory = 0
        for hardware in System._hardware:
            total_free_memory += hardware.free_memory
        total_used_memory = total_memory - total_free_memory

        total_free_capacity = 0
        for hardware in System._hardware:
            total_free_capacity += hardware.free_capacity
        total_used_capacity = total_capacity - total_free_capacity

        return f"System Analysis\n" \
               f"Hardware Components: {hardware_components}\n" \
               f"Software Components: {software_components}\n" \
               f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {total_used_capacity} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.NAME}\n"
            express = 0
            light = 0
            for software in hardware.software_components:
                if software.TYPE == "Express":
                    express += 1
                elif software.TYPE == "Light":
                    light += 1
            result += f"Express Software Components: {express}\n" \
                      f"Light Software Components: {light}\n" \
                      f"Memory Usage: {hardware.MEMORY - hardware.free_memory} / {hardware.MEMORY}\n" \
                      f"Capacity Usage: {hardware.CAPACITY - hardware.free_capacity} / {hardware.CAPACITY}\n" \
                      f"Type: {hardware.TYPE}\n"
            if hardware.software_components:
                software_components_name = [software_components.NAME for software_components in
                                            hardware.software_components]
                result += f"Software Components: {', '.join(software_components_name)}"
            else:
                result += f"Software Components: None"
        return result
