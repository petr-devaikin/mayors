#!/usr/bin/python
 # -*- coding: utf-8 -*-

from models import *
import wikipedia

wikipedia.set_lang('ru')

heads = open('data/heads.txt', 'w')
not_found = open('data/nf.txt', 'w')

try:
    cities = list(City.select())
    for c in cities:
        print c.name
        try:
            html = wikipedia.page(c.name).html()

            start_pos = html.find(u'Мэр</td>')
            if start_pos == -1:
                start_pos = html.find(u'Глава</td>')
            if start_pos == -1:
                start_pos = html.find(u'Глава администрации</td>')
            if start_pos == -1:
                start_pos = html.find(u'Глава города</td>')
            if start_pos == -1:
                start_pos = html.find(u'Руководство города</td>')

            if start_pos >= 0:
                start_pos = html.find('<div>', start_pos + 24)
                stop_pos = html.find('</div>', start_pos)
                area = html[start_pos+5:stop_pos].encode('utf-8')
                title_pos = area.find('title="')
                if title_pos != -1:
                    name = area[title_pos+7:area.find('"', title_pos+8)]
                else:
                    name = area
                heads.write('%d\t%s\n' % (c.id, name))
            else:
                not_found.write('%d\t%s\n' % (c.id, c.name.encode('utf-8')))
        except wikipedia.exceptions.DisambiguationError:
            not_found.write('%d\t%s\n' % (c.id, c.name.encode('utf-8')))

finally:
    heads.close()
    not_found.close()