# djangocms-table

A Table Plugin for django CMS.

## Updates
The original `djangocms-table` by Divio is now archived?! The spin-off `djangocms-table-changer` has also not been updated since 2015.

We will keep this version up to date as long as we need it, contributions and pull-request fixes are welcome! 

## Installation

Use pip install from git, replace `[TAG_OR_VERSION]` with a release e.g. `v2.0.0` or leave blank for master:
```shell script
pip install -e git+https://github.com/mcldev/djangocms-table@[TAG_OR_VERSION]#egg=djangocms-table
```

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-table``.
* Add ``'djangocms_table'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_table``.

## Compatibility

Version 2.+ is compatible with `Django 2.2` and `Django CMS 3.5+`

## Kudos

This plugin contains the handsontable.com jquery library.
Thanks to notch-interactive.com as well for some code examples.


## Translations

*Not being updated* - If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-table/

