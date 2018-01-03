#!/usr/bin/env python
# -*- encoding: utf-8
"""
Just enough Python/Django to build the pages from Markdown.
"""

import os

from django.conf import settings
from django.template import Template, Context
from django.template.engine import Engine
import markdown


if __name__ == '__main__':
    settings.configure()

    template = Template(open('_template.html').read(), engine=Engine())

    for f in os.listdir('pages'):
        if not f.endswith('.md'):
            continue

        print(f'Building {f}')

        path = os.path.join('pages', f)
        title, content = open(path).read().split('---', 1)

        title = title.strip()
        context = Context({
            'title': title,
            'content': markdown.markdown(content)
        })

        out_name = f.replace('.md', '.html')
        if out_name != 'index.html':
            out_name = f.replace('.md', '') + '/index.html'
            os.makedirs(os.path.dirname(out_name), exist_ok=True)

        with open(out_name, 'w') as outfile:
            outfile.write(template.render(context))
