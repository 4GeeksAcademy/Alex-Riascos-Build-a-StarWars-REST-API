"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate # type: ignore
from flask_swagger import swagger # type: ignore
from flask_cors import CORS # type: ignore
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Character, Vehicle, Favorite_Planet, Favorite_Character, Favorite_Vehicle




app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

####################################
# CRUD for User
####################################

@app.route('/user', methods=['GET'])
def get_user():
    users= User.query.all()
    users = list(map(lambda x: x.serialize(), users))
    return jsonify(users), 200


@app.route('/user/<int:id>', methods=['GET'])
def get_user_id(id):
    user = User.query.get(id)
    return jsonify(user.serialize()), 200

@app.route('/user', methods=['POST'])
def create_user():
    request_body = request.get_json()
    user = User(
        username=request_body["username"], 
        email=request_body["email"], 
        password=request_body["password"], 
        suscription_date=request_body["suscription_date"]        
        )
    #exmple: dict = {"username": "test", "email": "test", "password": "test", "suscription_date": "2021-09-01"}
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 200

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        raise APIException("User not found", status_code=404)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize()), 200

####################################
# CRUD for Planet
####################################

@app.route('/planet', methods=['GET'])
def get_planet():
    planets= Planet.query.all()
    planets = list(map(lambda x: x.serialize(), planets))
    return jsonify(planets), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_planet_id(id):
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()), 200

@app.route('/planet', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    planet = Planet(
        name=request_body["name"], 
        population=request_body["population"], 
        climate=request_body["climate"], 
        terrain=request_body["terrain"], 
        diameter=request_body["diameter"], 
        rotation_period=request_body["rotation_period"], 
        orbital_period=request_body["orbital_period"], 
        gravity=request_body["gravity"], 
        surface_water=request_body["surface_water"], 
        created=request_body["created"]
        )
    #exmple: dict = {"name": "test", "population": 1, "climate": "test", "terrain": "test", "diameter": 1, "rotation_period": 1, "orbital_period": 1, "gravity": "test", "surface_water": 1, "created": "2021-09-01"}
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize()), 200

@app.route('/planet/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
    if planet is None:
        raise APIException("Planet not found", status_code=404)
    db.session.delete(planet)
    db.session.commit()
    return jsonify(planet.serialize()), 200

####################################
# CRUD for Character
####################################

@app.route('/character', methods=['GET'])
def get_character():
    characters= Character.query.all()
    characters = list(map(lambda x: x.serialize(), characters))
    return jsonify(characters), 200

@app.route('/character/<int:id>', methods=['GET'])
def get_character_id(id):
    character = Character.query.get(id)
    return jsonify(character.serialize()), 200

@app.route('/character', methods=['POST'])
def create_character():
    request_body = request.get_json()
    character = Character(
        name=request_body["name"], 
        height=request_body["height"], 
        mass=request_body["mass"], 
        hair_color=request_body["hair_color"], 
        age=request_body["age"], 
        homeworld=request_body["homeworld"], 
        species=request_body["species"]
        )
    #exmple: dict = {"name": "test", "height": 1, "mass": 1, "hair_color": "test", "age": 1, "homeworld": "test", "species": "test"}
    db.session.add(character)
    db.session.commit()
    return jsonify(character.serialize()), 200

@app.route('/character/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    if character is None:
        raise APIException("Character not found", status_code=404)
    db.session.delete(character)
    db.session.commit()
    return jsonify(character.serialize()), 200

####################################
# CRUD for Vehicle
####################################

@app.route('/vehicle', methods=['GET'])
def get_vehicle():
    vehicles= Vehicle.query.all()
    vehicles = list(map(lambda x: x.serialize(), vehicles))
    return jsonify(vehicles), 200

@app.route('/vehicle/<int:id>', methods=['GET'])
def get_vehicle_id(id):
    vehicle = Vehicle.query.get(id)
    return jsonify(vehicle.serialize()), 200

@app.route('/vehicle', methods=['POST'])
def create_vehicle():
    request_body = request.get_json()
    vehicle = Vehicle(
        name=request_body["name"], 
        model=request_body["model"], 
        manufacturer=request_body["manufacturer"], 
        length=request_body["length"], 
        max_atmosphering_speed=request_body["max_atmosphering_speed"], 
        passengers=request_body["passengers"], 
        cargo_capacity=request_body["cargo_capacity"], 
        consumables=request_body["consumables"]
        )
    #exmple: dict = {"name": "test", "model": "test", "manufacturer": "test", "length": 1, "max_atmosphering_speed": 1, "passengers": 1, "cargo_capacity": 1, "consumables": "test"}
    db.session.add(vehicle)
    db.session.commit()
    return jsonify(vehicle.serialize()), 200

@app.route('/vehicle/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if vehicle is None:
        raise APIException("Vehicle not found", status_code=404)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify(vehicle.serialize()), 200


####################################
# GET Favorites
####################################

@app.route('/favorites/user/<int:user_id>', methods=['GET'])
def get_all_favorites(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException("User not found", status_code=404)    
    
    return jsonify(user.serialize_favorites()), 200

####################################
# CRUD for Favorite_Planet
####################################

@app.route('/favorite/user/<int:user_id>/planet/<int:planet_id>', methods=['POST'])
def create_favorite_planet(user_id, planet_id):
    # Verifica si los campos requeridos fueron proporcionados
    if user_id is None or planet_id is None:
        raise APIException("You need to specify the user_id and planet_id", status_code=400)

    # Verifica si el usuario y el planeta existen
    user = User.query.get(user_id)
    planet = Planet.query.get(planet_id)

    if user is None or planet is None:
        raise APIException("User or planet not found", status_code=404)

    # Verifica si el favorito ya existe
    existing_favorite_planet = Favorite_Planet.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    
    if existing_favorite_planet:
        raise APIException("Favorite already exists", status_code=400)

    # Crea un nuevo favorito si no existe
    favorite_planet = Favorite_Planet(user_id=user_id, planet_id=planet_id)
    
    db.session.add(favorite_planet)
    db.session.commit()

    return jsonify(favorite_planet.serialize()), 200


@app.route('/favorite/user/<int:user_id>/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(user_id, planet_id):
    favorite_planet = Favorite_Planet.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if favorite_planet is None:
        raise APIException("Favorite_planet not found", status_code=404)
    
    db.session.delete(favorite_planet)
    db.session.commit()
    return jsonify({"message": "Favorite vehicle deleted"}), 200

####################################
# CRUD for Favorite_Character
####################################

@app.route('/favorite/user/<int:user_id>/character/<int:character_id>', methods=['POST'])
def create_favorite_character(user_id, character_id):
    
    if user_id is None or character_id is None:
        raise APIException("You need to specify the user_id and character_id", status_code=400)
    
    user = User.query.get(user_id)
    character = Character.query.get(character_id)

    if user is None or character is None:
        raise APIException("User or character not found", status_code=404)

    existing_favorite_character = Favorite_Character.query.filter_by(user_id=user_id, character_id=character_id).first()

    if existing_favorite_character:
        raise APIException("Favorite already exists", status_code=400)

    favorite_character = Favorite_Character(user_id=user_id, character_id=character_id)    
    
    db.session.add(favorite_character)
    db.session.commit()
    return jsonify(favorite_character.serialize()), 200

@app.route('/favorite/user/<int:user_id>/character/<int:character_id>', methods=['DELETE'])
def delete_favorite_character(user_id, character_id):
    favorite_character = Favorite_Character.query.filter_by(user_id=user_id, character_id=character_id).first()
    if favorite_character is None:
        raise APIException("Favorite_character not found", status_code=404)
    db.session.delete(favorite_character)
    db.session.commit()
    return jsonify({"message": "Favorite vehicle deleted"}), 200

    
####################################
# CRUD for Favorite_Vehicle
####################################


@app.route('/favorite/user/<int:user_id>/vehicle/<int:vehicle_id>', methods=['POST'])
def create_favorite_vehicle(user_id, vehicle_id):
    
    if user_id is None or vehicle_id is None:
        raise APIException("You need to specify the user_id and vehicle_id", status_code=400)
    
    user = User.query.get(user_id)
    vehicle = Vehicle.query.get(vehicle_id)

    if user is None or vehicle is None:
        raise APIException("User or Vehicle not found", status_code=404)

    existing_favorite_vehicle = Favorite_Vehicle.query.filter_by(user_id=user_id, vehicle_id=vehicle_id).first()
    if existing_favorite_vehicle:
        raise APIException("Favorite already exists", status_code=400)

    favorite_vehicle = Favorite_Vehicle(user_id=user_id, vehicle_id=vehicle_id)    
    
    db.session.add(favorite_vehicle)
    db.session.commit()
    return jsonify(favorite_vehicle.serialize()), 200

@app.route('/favorite/user/<int:user_id>/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_favorite_vehicle(user_id, vehicle_id):
    try:
        # Buscar la relación Favorite_Vehicle con la sesión activa
        favorite_vehicle = Favorite_Vehicle.query.filter_by(user_id=user_id, vehicle_id=vehicle_id).one_or_none()

        if favorite_vehicle is None:
            raise APIException("Favorite_Vehicle not found", status_code=404)        
        db.session.delete(favorite_vehicle)
        db.session.commit()

        return jsonify({"message": "Favorite vehicle deleted"}), 200

    except APIException as e:
        return jsonify({"message": e.message}), e.status_code

    except Exception as e:
        db.session.rollback()  # Hacer rollback en caso de error
        return jsonify({"message": "Internal server error"}), 500


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
