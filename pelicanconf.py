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
LINKS = (('Python', 'http://python.org'),
         ('Pelican', "http://http://blog.getpelican.com"),
         ('社区大妈', "http://zoomquiet.io"),)

SOCIAL = (('Twitter', 'http://twitter.com/chifeng'),
          ('Github', 'http://github.com/chifeng'),)

#PLUGINS=['_plugins.sitemap'
#    #, '_plugins.extract_toc'
#    ]
PLUGIN_PATH = '_plugins'
PLUGINS=['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_PAGINATION = 9

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'
DISQUS_SITENAME = 'chifeng'
GITHUB_URL = 'http://github.com/chifeng'
GOOGLE_ANALYTICS = 'UA-52310651-1'
TWITTER_USERNAME = 'chifeng'
