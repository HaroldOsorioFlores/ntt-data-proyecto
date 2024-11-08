from app.models import Incident

def create_incident(data):
    return Incident(
        incident_name=data['incident_name'],
        incident_category=data['incident_category'],
        location_reference=data['location_reference'],
        latitud=data['latitud'],
        longitud=data['longitud'],
        direccion_fmt=data['direccion_fmt'],
        description=data['description']
    )