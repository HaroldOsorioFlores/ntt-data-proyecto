from datetime import datetime

from app.models import db

class Incident(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    incident_name = db.Column(db.String(100), nullable=False)
    incident_category = db.Column(db.String(100), nullable=False)
    location_reference = db.Column(db.String(100), nullable=False)
    latitud = db.Column(db.String(100), nullable=False)
    longitud = db.Column(db.String(100), nullable=False)
    direccion_fmt = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            "id": self.id,
            "incident_name": self.incident_name,
            "incident_category": self.incident_category,
            "location_reference": self.location_reference,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "direccion_fmt": self.direccion_fmt,
            "created_at": self.created_at,
            "description": self.description
        }