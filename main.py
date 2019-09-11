#!/usr/bin/env python
import os

import tornado.web
import tornado.ioloop
from tornado.options import parse_command_line, define, options

from views import MainHandler, InfoHandler, AllHandler, ModifyHandler


def make_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    web_app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/info", InfoHandler),
            (r"/all", AllHandler),
            (r"/modify", ModifyHandler),

        ],
        template_path=os.path.join(base_dir, 'templates'),
        static_path=os.path.join(base_dir, 'statics')
    )
    return web_app


if __name__ == "__main__":
    define("host", default='localhost', help="主机地址", type=str)
    define("port", default=8001, help="主机端口", type=int)

    parse_command_line()

    app = make_app()
    app.listen(options.port, options.host)
    print('server running on %s:%s' % (options.host, options.port))

    loop = tornado.ioloop.IOLoop.current()
    loop.start()
