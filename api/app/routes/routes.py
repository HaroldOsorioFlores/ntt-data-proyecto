from flask import Blueprint, request, jsonify

from app.models import db, Incident
from app.services.incident_service import create_incident

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return {"status": "success", "message": "Security API is active"}


@main.route('/incident', methods=['GET'])
def get_incident():
    incidents = Incident.query.all()

    incidents_data = [
        {
            'id': incident.id,
            "incident_name": incident.incident_name,
            "incident_category": incident.incident_category,
            "location_reference": incident.location_reference,
            "latitud": incident.latitud,
            "longitud": incident.longitud,
            "direccion_fmt": incident.direccion_fmt,
            "created_at": incident.created_at,
            "description": incident.description
        }
        for incident in incidents
    ]
    return jsonify(incidents_data), 200

@main.route('/incident', methods=['POST'])
def post_incident():
    data = request.get_json()
    new_incident = create_incident(data)
    db.session.add(new_incident)
    db.session.commit()

    return jsonify({'message': 'Incident created successfully'}), 201
