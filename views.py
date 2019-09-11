import tornado.web

from models import session, User


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        q = session.query(User)
        users = q.limit(10)
        self.render('base.html', users=users)


class AllHandler(tornado.web.RequestHandler):
    def get(self):
        q = session.query(User)
        all_users = q.all()
        users = q.limit(10)
        self.render('all.html', all_users=all_users, users=users)


class InfoHandler(tornado.web.RequestHandler):
    def get(self):
        q = session.query(User)
        uid = int(self.get_argument('id'))
        user = q.get(uid)
        users = q.limit(10)
        self.render('info.html', user=user, users=users)


class ModifyHandler(tornado.web.RequestHandler):
    def get(self):
        q = session.query(User)
        uid = int(self.get_argument('id'))
        user = q.get(uid)
        users = q.limit(10)
        self.render('modify.html', user=user, users=users)

    def post(self):
        q = session.query(User)
        uid = int(self.get_argument('id'))
        user = q.get(uid)

        user.name = self.get_argument('name')
        user.birthday = self.get_argument('birthday')
        user.city = self.get_argument('city')
        user.money = float(self.get_argument('money'))
        session.commit()

        self.redirect('/info?id=%s' % uid)  # 通过重定向，跳转到用户信息页
