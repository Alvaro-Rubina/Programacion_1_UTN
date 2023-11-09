class Motocicleta:
    # Atributo de clase
    condition = "Nueva"
    engine = False 

    # Precio por defecto
    default_price = 0
    # Atributos
    def __init__(self, color, license_plate, fuel_liters, wheels, brand, model, manufacture_date, top_speed, weight):
        self.color = color
        self.license_plate = license_plate
        self.fuel_liters = fuel_liters
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.manufacture_date = manufacture_date
        self.top_speed = top_speed
        self.weight = weight

    # Métodos
    def start(self):
        if self.engine == False:
            self.engine = True
            print("-- El motor se ha puesto en marcha --")
        else:
            print("-- El motor ya está en marcha, no es necesario arrancarlo nuevamente! --")

    def stop(self):
        if self.engine == True:
            self.engine = False
            print("-- Se ha detenido el motor --")
        else:
            print("-- El motor ya está detenido, no es necesario detenerlo nuevamente! --")

    # Metodo para mostrar la motocicleta
    def showing_motorcycle(self):
        print(f"\n<< {self.brand.upper()}, Modelo {self.model} >>")
        print(f"- Año de fabricación: {self.manufacture_date}")
        print(f"- Peso: {self.weight} Kg")
        print(f"- Capacidad de combustible: {self.fuel_liters}L")
        print(f"- Tope de velocidad: {self.top_speed} Km/h")
        print(f"- Color: {self.color}")
        print(f"- Numero de ruedas: {self.wheels}")
        print(f"\n---- PATENTE: [{self.license_plate}]")
        print(f"---- ESTADO: {self.condition}")

    # Consultar precio
    def price_checking(self):
        return self.default_price
