from abc import ABCMeta
from abc import abstractmethod

class VehicleABC(metaclass=ABCMeta):

    @abstractmethod
    def move(self, distance_traveled:int) -> None:
        pass

    @abstractmethod
    def vel(self, pisarAcelerador:bool) -> None:
        pass

    @abstractmethod
    def stop(self, stop_car:bool) -> None:
        pass
