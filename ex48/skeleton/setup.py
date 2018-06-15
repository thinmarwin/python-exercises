try:
    from setuptools import setup
except ImportError:
    form distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'My Name',
        'url': 'URL to get it at.',
        'download_url': 'Where to download if',
        'author_email': 'My emaul',
        'version': '0.1',
        'install_requires':['nose'],
        'packages': ['lexicon'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)
