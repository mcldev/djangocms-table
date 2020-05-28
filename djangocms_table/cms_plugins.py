from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .forms import TableForm
from .models import TableModel
from .views import *

class TablePlugin(CMSPluginBase):
    model = TableModel
    form = TableForm
    name = _("Table")
    render_template = "djangocms_table/output-render/table.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('header_rows_top', 'header_rows_left', 'footer_rows'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload', 'table_settings')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('table_classes', 'header_row_classes', 'footer_row_classes', 'body_row_classes', 'header_cell_classes', 'cell_classes')
        })
    )

    def render(self, context, instance, placeholder):

        table_view = TableView(table_instance=instance)

        context.update({
            'name': instance.name,
            'table_view': table_view,
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + "djangocms_table/img/table.png"

    def response_change(self, request, obj):
        response = super(TablePlugin, self).response_change(request, obj)
        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response

plugin_pool.register_plugin(TablePlugin)
