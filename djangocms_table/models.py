from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from django.template.defaultfilters import slugify


class TableModel(CMSPlugin):
    """
    TableModel plugin
    """

    name = models.TextField(_("name"), blank=True, null=True)

    # Number of Header Rows: Top, Left and Footer Rows: bottom
    header_rows_top = models.PositiveSmallIntegerField(_("Top"), default=1)
    header_rows_left = models.PositiveSmallIntegerField(_("Left"), default=0)
    footer_rows = models.PositiveSmallIntegerField(_("Footer"), default=0)

    # Table Data and settings
    table_data = models.TextField(_("table data"))
    table_settings = models.TextField(_("Table Settings"), blank=True)

    # Table/Row/Cell Classes
    table_classes = models.TextField(_('Table Classes'), default='table table-hover', blank=True)
    header_row_classes = models.TextField(_('Header Row Classes'), blank=True)
    footer_row_classes = models.TextField(_('Footer Row Classes'), blank=True)
    body_row_classes = models.TextField(_('Body Row Classes'), blank=True)
    header_cell_classes = models.TextField(_('Header Cell Classes'), blank=True)
    cell_classes = models.TextField(_('Cell Classes'), blank=True)

    def table_id(self):
        get_name = self.name or "{}".format(self.id)
        get_name = slugify(get_name)
        get_name += '_id'

        return get_name

    def __str__(self):
        return self.name

    search_fields = ('name', 'table_data')
