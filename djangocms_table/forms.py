import io

from django import forms
from django.forms.models import ModelForm
from .widgets import TableWidget
from .models import TableModel
from django.utils.translation import ugettext_lazy as _
import csv
import json


class TableForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TableForm, self).__init__(*args, **kwargs)
        # TODO there must be a more direct way to get this... no idea how.
        TableWidget.table_settings_id = self.auto_id % 'table_settings'

    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))

    table_settings = forms.CharField(widget=forms.HiddenInput())
    table_data = forms.CharField(widget=TableWidget, required=False)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("Upload a .csv file to populate the table."),
                                 required=False)

    def clean_table_data(self):
        if self.cleaned_data['table_data']:
            return self.cleaned_data['table_data'].replace("null", '""')

    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            # Make sure we decode the file to text
            encoding = self.cleaned_data['csv_upload'].charset if self.cleaned_data['csv_upload'].charset else 'utf-8-sig'
            f = io.TextIOWrapper(self.cleaned_data['csv_upload'].file, encoding=encoding)
            csv_reader = csv.reader(f, dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = json.dumps(data)
            self.csv_uploaded = True

    def clean_table_settings(self):
        if self.cleaned_data['table_settings']:
            # This is a cleanup for table settings outside the scope of the table_data - caused by faulty mergeCells
            table_settings = json.loads(self.cleaned_data['table_settings'])
            table_data = json.loads(self.cleaned_data['table_data'])
            max_rows = len(table_data)
            max_cols = max([len(row) for row in table_data])
            if table_settings['mergeCells']:
                clean_merge = []
                for merge in table_settings['mergeCells']:
                    if merge['row'] <= max_rows and merge['col'] <= max_cols:
                        clean_merge.append(merge)
                table_settings['mergeCells'] = clean_merge
            if table_settings['alignment']:
                clean_align = []
                for align in table_settings['alignment']:
                    if align['row'] <= max_rows and align['col'] <= max_cols:
                        clean_align.append(align)
                table_settings['alignment'] = clean_align
            return json.dumps(table_settings)

    class Meta:
        model = TableModel
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
