""" Class for car model """

from clasepython.core.abcs.car_abcs import  VehicleABC

MAX_DISTANCE_CAN_TRAVEL = 5

AVAILABLE_CAR_BRANDS: ['BMW', 'Toyota', 'Nissan' ]


class Car(VehicleABC):
    
    def __init__(self, brand:str, model:int, door_quantity:int):
        """ Constructor for Car class """
        self.__brand = brand
        self.__model = model
        self.__door = door_quantity
        self.__distance_traveled = 0
        self.__velocidad = 0

    def move(self, additional_distance) -> None:

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self.__distance_traveled += additional_distance
        else:
            self.__distance_traveled += MAX_DISTANCE_CAN_TRAVEL       

    def vel(self, pisarAcelerador) -> None:

        if move(pisarAcelerador == True) :
            self.__velocidad +=  + 10 
        else:
            self.__velocidad = 0       

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self.__brand = brand
        else:
            print("Inserte una marva válida.")    


