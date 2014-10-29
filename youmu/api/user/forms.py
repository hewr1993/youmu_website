__author__ = 'badpoet'

from wtforms import Form, TextField, PasswordField, validators
from youmu.models.user import User
from youmu.api.user.service import UserService

class LoginForm(Form):
    username = TextField('UserId', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = UserService.load_user_by_id(self.username.data)
        if user is None:
            self.username.errors.append('Unknown user id')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        return True