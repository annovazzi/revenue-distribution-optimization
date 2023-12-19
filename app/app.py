# app/app.py

from flask import render_template, jsonify
from app import app
from app.models import Property, Booking

# Crie algumas instâncias de propriedades e reservas para fins de exemplo
property1 = Property(property_id=1, property_name="Property 1")
booking1 = Booking(booking_id=1, booking_date="2023-01-01", revenue=1000, owner_id=1, host_id=1, commission_percentage=0.1)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para a API de distribuição de receitas
@app.route('/api/distribution/<int:property_id>')
def api_distribution(property_id):
    # Suponha que você tenha uma lista de reservas associadas a uma propriedade
    bookings = [booking1]  # Adicione mais reservas conforme necessário
    total_revenue = 0

    # Calcule a distribuição total de receitas para a propriedade
    for booking in bookings:
        if booking.owner_id == property_id:
            total_revenue += booking.calculate_distribution()

    # Retorna os resultados em formato JSON
    return jsonify({
        'property_id': property_id,
        'total_revenue': total_revenue
    })
