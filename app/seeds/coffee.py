from app.models import db, Coffee


# Adds Coffees
def seed_coffee():
    #1
    espresso = Coffee(
        name='Espresso', year=1906, caffeine_content=64
    )

    #2
    black = Coffee(
        name='Black', year=1671, caffeine_content=12
    )

    #3
    latte = Coffee(
        name='Latte', year=1950, caffeine_content=64
    )

    db.session.add_all([ espresso, black, latte ])
    db.session.commit()


def undo_coffee():
    db.session.execute("DELETE FROM coffee")
    db.session.commit()
