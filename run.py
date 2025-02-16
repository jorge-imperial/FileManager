#!/usr/bin/python3

import sys
import tornado.ioloop
from tornado.options import define, options
from sources.app import make_application

define('rootpath', help = 'Root directory for server', type = str)
define('address', default = '127.0.0.1', help = 'Bound IP address', type = str)
define('port', default = '9000', help = 'Bound TCP port', type = int)

if __name__ == '__main__':
    options.parse_command_line()
    application = make_application(options.rootpath)
    application.listen(options.port, address = options.address)
    tornado.ioloop.IOLoop.instance().start()
