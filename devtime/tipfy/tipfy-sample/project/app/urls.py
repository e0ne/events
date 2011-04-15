# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    Rule('/', name='hello-world', handler='dev_time_sample.handlers.HelloWorldHandler'),
    Rule('/pretty', name='hello-world-pretty', handler='dev_time_sample.handlers.PrettyHelloWorldHandler'),
    Rule('/add', name='add-sample-data', handler='dev_time_sample.handlers.AddSampleDataHandler'),
    Rule('/view', name='view-sample-data', handler='dev_time_sample.handlers.ViewSampleDataHandler'),
]
