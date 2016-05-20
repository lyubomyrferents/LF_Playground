try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LF Project',
    'author': 'Lyubomyr Ferents',
    'url': 'http://my.home.site',
    'download_url': 'http://my.home.site/download',
    'author_email': 'lyubomyrferents@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'project ex48'
}

setup(**config)