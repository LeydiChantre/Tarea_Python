""" Class for car model """

from _typeshed import SupportsWrite
from abc import ABCMeta
from clasepython.core.abcs.car_abcs import  VehicleABC

MAX_DISTANCE_CAN_TRAVEL = 5

AVAILABLE_CAR_BRANDS: ['Nissan', 'Toyota', 'Bmw' ]


class Car(VehicleABC):
    
    def __init__(self, brand:str, model:int, door_quantity:int):
        """ Constructor for Car class """
        self.__brand = brand
        self.__model = model
        self.__door_quantity = door_quantity
        self.__distance_traveled = 0
        self.__velocidad = 0
        self._stop= 0

    def move(self, additional_distance) -> None:

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self.__distance_traveled += additional_distance
        else:
            self.__distance_traveled += MAX_DISTANCE_CAN_TRAVEL       

    def vel(self, pisarAcelerador) -> None:

        if move(pisarAcelerador == True) :
            self.__velocidad +=  10 
        else:
            self.__velocidad = 0       

    def stop(self, stop_car) -> None:

        if move(stop_car == True) :
            self.__velocidad =  0
        else:
            print("El carro esta quieto")  


    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self.__brand = brand
        else:
            print("Inserte una marca válida.")    

    @property
    def distance_traveled(self):
        return self.__distance_traveled
    
    @distance_traveled.setter
    def distance_traveled(self, distance_traveled):
        self.__distance_traveled = distance_traveled

    @property
    def model(self):
        return self.model
    
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def door_quantity(self):
        return self.door_quantity
        
    @door_quantity.setter
    def door_quantity(self, door_quantity):
        self. __door_quantity = door_quantity
    
@property
    def velocidad(self):
        return self.velocidad
        
    @velocidad.setter
    def velocidad(self, velocidad):
        self. __velocidad = velocidad

    @property
    def stop(self):
        return self.stop
        
    @stop.setter
    def stop(self, stop):
        self. __stop = stop