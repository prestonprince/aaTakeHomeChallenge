from flask.cli import AppGroup
from .coffee import seed_coffee, undo_coffee
from .posts import seed_posts, undo_posts


from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')


# Creates the 'flask seed all' command
@seed_commands.command('all')
def seed():
    seed_coffee()
    seed_posts()


# Creates the 'flask seed undo' command
@seed_commands.command('undo')
def undo():
    undo_posts()
    undo_coffee()
