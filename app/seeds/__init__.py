from flask.cli import AppGroup
from .coffee import seed_coffee, undo_coffee


from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')


# Creates the 'flask seed all' command
@seed_commands.command('all')
def seed():
    seed_coffee()


# Creates the 'flask seed undo' command
@seed_commands.command('undo')
def undo():
    undo_coffee()
