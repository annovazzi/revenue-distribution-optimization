# app/models.py

class Property:
    def __init__(self, property_id, property_name):
        self.property_id = property_id
        self.property_name = property_name
        # Adicione outros atributos conforme necessário

class Booking:
    def __init__(self, booking_id, booking_date, revenue, owner_id, host_id, commission_percentage):
        self.booking_id = booking_id
        self.booking_date = booking_date
        self.revenue = revenue
        self.owner_id = owner_id
        self.host_id = host_id
        self.commission_percentage = commission_percentage

    def calculate_distribution(self):
        # Adicione a lógica para calcular a distribuição de receitas
        return self.revenue * self.commission_percentage
