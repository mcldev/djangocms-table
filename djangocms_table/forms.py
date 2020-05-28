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

    class Meta:
        model = TableModel
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
