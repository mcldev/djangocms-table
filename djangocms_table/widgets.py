from django.conf import settings
from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation.trans_real import get_language

class TableWidget(Textarea):

    table_settings_id = ''

    class Media:
        js = (
                'djangocms_table/ext-input/js/jquery.min.js',
                'djangocms_table/ext-input/handsontable/0.21.0/handsontable.full.min.js',
                # 'djangocms_table/ext-input/handsontable/0.31.1/handsontable.full.min.js',
                'djangocms_table/ext-input/js/jquery.contextMenu.js',
                'djangocms_table/ext-input/js/jquery-ui.position.js',
                'djangocms_table/ext-input/js/json2.js',
                'djangocms_table/ext-input/js/bootstrap3-typeahead.js',
            )
        css = {
            'all': (
                'djangocms_table/ext-input/css/handsontable.full.modified.min.css',
                'djangocms_table/ext-input/css/jquery.contextMenu.css',
                ),
        }

    def render_textarea(self, name, value, attrs=None):
        return super(TableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]
        context = {
            'name': name,
            'language': language,
            'data': value,
            'table_settings_id': self.table_settings_id,
            'STATIC_URL': settings.STATIC_URL,
        }
        return mark_safe(render_to_string('djangocms_table/input-widget/table-widget.html', context))

    def render(self, name, value, attrs=None, renderer=None):
        return self.render_textarea(name, value, attrs) + self.render_additions(name, value, attrs)

