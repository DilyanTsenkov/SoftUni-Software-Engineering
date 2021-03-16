from abc import ABC, abstractmethod


class Robot(ABC):
    @abstractmethod
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def sensors_count(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class Android(Robot):
    def __init__(self, type):
        super().__init__(type)
        self.type = type

    @property
    def sensors_count(self):
        return 4

    @property
    def get_type(self):
        return self.type


class Chappie(Robot):
    def __init__(self, type):
        super().__init__(type)
        self.type = type

    @property
    def sensors_count(self):
        return 6

    @property
    def get_type(self):
        return self.type


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.sensors_count)


def robot_types(robots: list):
    for robot in robots:
        print(robot.get_type)


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)
robot_types(robots)
