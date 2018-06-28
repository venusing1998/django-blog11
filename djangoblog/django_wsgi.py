#!/usr/bin/env python3
#coding: utf-8

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoblog.settings")#mysite替换为自己的项目�?
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()