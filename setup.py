from setuptools import setup
from djangocms_table import __version__

INSTALL_REQUIRES = [
    'transifex-client',
    'django-cms>=3.5',
    'django',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.2',
]

setup(
    name='djangocms-table',
    version=__version__,
    description='Table Plugin for django CMS',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/mcldev/djangocms-table',
    packages=['djangocms_table', 'djangocms_table.migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False
)
