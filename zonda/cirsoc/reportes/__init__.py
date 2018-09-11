import os
import gettext
from jinja2 import Environment, FileSystemLoader

current_dir = os.path.dirname(os.path.realpath(__file__))
templates_dir = os.path.join(current_dir, 'plantillas')
file_loader = FileSystemLoader(templates_dir)
env = Environment(loader=file_loader, extensions=['jinja2.ext.i18n'])
env.globals.update(zip=zip)
env.install_gettext_callables(gettext.gettext, gettext.ngettext)

env.globals['SemanticCSS'] = os.path.join(templates_dir, 'css', 'semantic.min.css')
env.globals['CustomCSS'] = os.path.join(templates_dir, 'css', 'custom.css')


class Reporte:
    def __init__(self, template, **kwargs):
        template = env.get_template(template)
        self._html_str = template.render(**kwargs)

    def html(self):
        return self._html_str

    def escribir(self, output):
        with open(output, 'w', encoding='utf-8') as ou:
            ou.write(self._html_str)

