#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chifeng'
SITENAME = u"Chifeng's Blog"
SITEURL = 'http://blog.chifeng.name'
DISQUS_SITENAME = u"blogchifengname"

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M',
}
#DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
#DEFAULT_DATE = 'fs' # use filesystem's mtime

DEFAULT_LANG = u'zh_CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/chifeng'),
	 )

DEFAULT_PAGINATION = 9

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'
