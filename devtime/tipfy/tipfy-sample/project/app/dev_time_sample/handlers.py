# -*- coding: utf-8 -*-
"""
    dev_time_sample.handlers
    ~~~~~~~~~~~~~~~~~~~~

    Hello, World!: the simplest tipfy app.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime
from tipfy.app import Response
from tipfy.handler import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin
from models import DevTime

class HelloWorldHandler(RequestHandler):
    def get(self):
        """Simply returns a Response object with an enigmatic salutation."""
        return Response('Hello, World!')


class PrettyHelloWorldHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        """Simply returns a rendered template with an enigmatic salutation."""
        context = {
            'message': 'Hello, World!',
        }
        return self.render_response('hello_world.html', **context)

class AddSampleDataHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return  self.render_response('add.html')

    def post(self):
        devtime = DevTime()
        devtime.date=datetime.now()

        devtime.topics=['Python', 'tipfy']
        devtime.put()
        return Response('Done.')


class ViewSampleDataHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        data = DevTime.all()
        return  self.render_response('view.html', events=data)
