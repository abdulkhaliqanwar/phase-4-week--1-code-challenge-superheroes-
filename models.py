from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='power', lazy=True, cascade="all, delete-orphan")

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description

    def __repr__(self):
        return f"<Power {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Hero {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'hero_powers': [hero_power.to_dict() for hero_power in self.hero_powers]
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    strength = db.Column(db.String(50), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', or 'Average'")
        return strength

    def __repr__(self):
        return f"<HeroPower {self.hero.name} - {self.power.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero.id,
            'power_id': self.power.id,
            'strength': self.strength,
            'hero': {
                'id': self.hero.id,
                'name': self.hero.name,
                'city': self.hero.city
            },
            'power': self.power.to_dict()
        }
