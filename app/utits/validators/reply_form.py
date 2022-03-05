from wtforms import Form, StringField, validators

class ReplyForm(Form):
    title = StringField('title', [validators.Length(min=4, max=64)])
    content = StringField('content', [validators.Length(min=4)])