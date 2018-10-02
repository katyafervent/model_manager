from database import db
from database.models import ReclassModelTemplate


def create_model(data):

    new_model = ReclassModelTemplate()
    db.session.add(new_model)
    db.session.commit()


def update_user(user_id, data):
    pass


def delete_user(user_id):
    pass
