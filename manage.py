#! /usr/bin/env python

from thermos import app, db
from thermos.models import User
from flask_script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
    """
    Initializes the database.
    """
    db.create_all()
    db.session.commit()
    print('Initialized the database')


@manager.command
def dropdb():
    """
    Drops the database.
    """
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print('Dropped the database')


@manager.command
def testdb():
    """
    Initializes the test database.
    """
    db.create_all()
    db.session.add(User(username="milagan", email="milagan@mail.com", password="test"))
    db.session.add(User(username="milagan1", email="milagan1@mail.com", password="test"))
    db.session.commit()
    print('Initialized the database for testing')


if __name__ == '__main__':
    manager.run()
