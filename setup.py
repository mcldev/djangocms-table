from setuptools import setup
from djangocms_table import __version__

INSTALL_REQUIRES = [
    'django-cms>=3.11,<3.12',
    'django>=4.2,<5.0',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 4.2',
    'Framework :: Django CMS :: 3.11',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
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
    python_requires='>=3.9',
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False
)
