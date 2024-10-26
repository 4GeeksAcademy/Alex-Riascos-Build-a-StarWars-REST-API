# This file will contain the models for the database.
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    suscription_date = db.Column(db.Date(), unique=False, nullable=False)    
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __init__(self, username, email, password, suscription_date):
        self.username = username
        self.email = email
        self.password = password
        self.suscription_date = suscription_date
        self.is_active = True
    

    # favorite_planet_id = db.Column(db.Integer, db.ForeignKey('favorite_planet.id'))
    # favorite_planet = db.relationship('Favorite_Planet', backref='users', foreign_keys=[favorite_planet_id])
    
    # favorite_character_id = db.Column(db.Integer, db.ForeignKey('favorite_character.id'))
    # favorite_character = db.relationship('Favorite_Character', backref='users', foreign_keys=[favorite_character_id])
    
    # favorite_vehicle_id = db.Column(db.Integer, db.ForeignKey('favorite_vehicle.id'))
    # favorite_vehicle = db.relationship('Favorite_Vehicle', backref='users', foreign_keys=[favorite_vehicle_id])
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "suscription_date": self.suscription_date,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.Integer, unique=False, nullable=False)
    created = db.Column(db.DateTime(), unique=False, nullable=False)

    def __init__(self, name, population, climate, terrain, diameter, rotation_period, orbital_period, gravity, surface_water, created):
        self.name = name
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.diameter = diameter
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.surface_water = surface_water
        self.created = datetime.now(timezone.utc)
     

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "surface_water": self.surface_water,
            "created": self.created
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False )
    age = db.Column(db.Integer, unique=False, nullable=False)
    homeworld = db.Column(db.String(120), unique=False, nullable=False)
    species = db.Column(db.String(120), unique=False, nullable = False)

    def __init__(self, name, height, mass, hair_color, age, homeworld, species):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.age = age
        self.homeworld = homeworld
        self.species = species

    def __repr__(self):
        return '<Character %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "age": self.age,
            "homeworld": self.homeworld,
            "species": self.species
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    manufacturer = db.Column(db.String(120), unique=False, nullable=False)
    length = db.Column(db.Integer, unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, unique=False, nullable=False)    
    passengers = db.Column(db.Integer, unique=False, nullable=False) #
    cargo_capacity = db.Column(db.Integer, unique=False, nullable=False)
    consumables = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, name, model, manufacturer, length, max_atmosphering_speed, passengers, cargo_capacity, consumables):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables      
    
    def __repr__(self):
        return '<Vehicle %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables
        }

# class Favorite_Planet(db.Model):
#     __tablename__ = 'favorite_planet'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

#     def __repr__(self):
#         return '<Favorite_Planet %r>' % self.id
    
#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "planet_id": self.planet_id
#         }

# class Favorite_Character(db.Model):
#     __tablename__ = 'favorite_character'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     character_id = db.Column(db.Integer, db.ForeignKey('character.id'))

#     def __repr__(self):
#         return '<Favorite_Character %r>' % self.id
    
#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "character_id": self.character_id
#         }
    
# class Favorite_Vehicle(db.Model):
#     __tablename__ = 'favorite_vehicle'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

#     def __repr__(self):
#         return '<Favorite_Vehicle %r>' % self.id
    
#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "vehicle_id": self.vehicle_id
#         }

