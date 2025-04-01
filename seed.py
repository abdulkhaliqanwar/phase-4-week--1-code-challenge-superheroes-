from random import choice as rc
from app import app
from models import db, Hero, Power, HeroPower

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Power.query.delete()
        Hero.query.delete()
        HeroPower.query.delete()

        print("Seeding powers...")
        powers = [
            Power(name="super strength", description="gives the wielder super-human strength"),
            Power(name="flight", description="gives the wielder the ability to fly at supersonic speeds"),
            Power(name="super human senses", description="allows the wielder to use her senses at a superhuman level"),
            Power(name="elasticity", description="can stretch the human body to extreme lengths"),
        ]
        db.session.add_all(powers)

        print("Seeding heroes...")
        heroes = [
            Hero(name="Kamala Khan", city="Jersey City"),
            Hero(name="Doreen Green", city="New York City"),
            Hero(name="Gwen Stacy", city="New York City"),
            Hero(name="Janet Van Dyne", city="San Francisco"),
            Hero(name="Wanda Maximoff", city="Westview"),
        ]
        db.session.add_all(heroes)

        print("Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        hero_powers = []
        for hero in heroes:
            power = rc(powers)
            hero_powers.append(
                HeroPower(hero=hero, power=power, strength=rc(strengths))
            )
        db.session.add_all(hero_powers)
        db.session.commit()

        print("Done seeding!")
