from mongoengine import Document, StringField, IntField, BooleanField

class SMDocument(Document):
    meta = {'allow_inheritance': True}
    isDeleted = BooleanField(default=False)

    def delete(self):
        self.isDeleted = True
        self.save()

class User(SMDocument):
    name = StringField(required=True)
    age = IntField()
