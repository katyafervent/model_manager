from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    # TODO: use password hashes
    password = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email, password, user=None, manager=None,
                 is_admin=False, first_name=None, last_name=None, phone=None,
                 organisation=None, operator=None, roles=None, key_account=None, is_active=None):
        # self.token = token or Token()
        self.username = username
        self.password = password
        self.user = user
        self.manager = manager
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.organisation = organisation
        self.operator = operator
        self.roles = roles or []
        self.key_account = key_account

        self.enabled = is_active
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % self.username


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class ReclassModelTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
