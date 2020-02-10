from application.extensions import db

class Data(db.Document):
    meta = {
        'db_alias': 'data_db',
    }

    sku = db.IntField(required=True, unique=True)

    item_id = db.IntField()
    title = db.StringField()

    primary_image = db.StringField()
    item_available = db.BooleanField()