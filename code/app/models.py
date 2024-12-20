from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, UUID, Text,ForeignKey


db = SQLAlchemy()

class Planta(db.Model):
    __tablename__ = 'plantas'
    id = Column(UUID, primary_key=True) 
    name = Column(String(80), unique=True)
    image = Column(String(255))
    description = Column(Text)
    mantenimiento = db.relationship('Mantenimiento') 

class Mantenimiento(db.Model):
    __tablename__ = 'mantenimientos'
    id = Column(UUID, primary_key=True)
    care = Column(Text)
    planta_id = Column(UUID, ForeignKey('plantas.id'))  

    