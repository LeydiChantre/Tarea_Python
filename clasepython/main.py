from clasepython.model.car import Car

def main():

    carro1: Car = Car("Nissan",2020,4)

    carro1.move(4)
    carro1.vel(True)
    carro1.st(True)

    print(carro1.distance_traveled)
    print(carro1.velocidad)
    print(carro1.stop)


if __name__ == "__main__":
    main()


