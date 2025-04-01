from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower
from flask_migrate import Migrate

app = Flask(__name__)

# Configure database (SQLite for now)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migrations
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Welcome to the Superheroes API!"

# GET /heroes - Return all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

# GET /heroes/:id - Return details of a specific hero
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict())
    return jsonify({"error": "Hero not found"}), 404

# GET /powers - Return all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

# GET /powers/:id - Return details of a specific power
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    return jsonify({"error": "Power not found"}), 404

# PATCH /powers/:id - Update a power
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        data = request.get_json()
        description = data.get('description')
        if description:
            try:
                power.description = description
                db.session.commit()
                return jsonify(power.to_dict())
            except ValueError as e:
                return jsonify({"errors": [str(e)]}), 400
        return jsonify({"error": "Description is required"}), 400
    return jsonify({"error": "Power not found"}), 404

# POST /hero_powers - Create a new hero-power association
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    if not hero_id or not power_id or not strength:
        return jsonify({"error": "Missing required fields"}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"error": "Hero or Power not found"}), 404

    if strength not in ['Strong', 'Weak', 'Average']:
        return jsonify({"error": "Strength must be one of: 'Strong', 'Weak', or 'Average'"}), 400

    try:
        hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
        db.session.add(hero_power)
        db.session.commit()
        return jsonify(hero_power.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
