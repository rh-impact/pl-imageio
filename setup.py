from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'imageio',
    version          = '0.1',
    description      = 'Create Animated Images Using Python',
    long_description = readme,
    author           = 'ElenaKarolinaSemanova',
    author_email     = 'semanova.elena@gmail.com',
    url              = 'http://wiki',
    packages         = ['imageio'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'imageio = imageio.__main__:main'
            ]
        }
)
