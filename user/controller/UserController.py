import hashlib

from user.models import User


class UserController(object):

    def __init__(self, request=None):
        self.request = request

    def __set_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_userid(self, userid=None):
        if userid is None:
            return False
        return User.objects.filter(userid=userid).first()

    def create_user(self, userid=None, userpassword=None):
        if userid is None or userpassword is None:
            return False

        member = User(userid=userid, password=self.__set_password(userpassword))
        try:
            member.publish()
            return True
        except InterruptedError:
            return False

    def login_user(self, userid=None, userpassword=None):
        if userid is None or userpassword is None:
            return False

        member = User.objects.filter(userid=userid).first()
        if member is None:
            return False

        if member.get_userid() == userid and member.get_userpassword() == self.__set_password(userpassword):
            self.request.session['useridx'] = member.get_useridx()
            return True

        return False

    def read_session(self):
        return self.request.session.get('useridx', None)

    def logout(self):
        del self.request.session['useridx']