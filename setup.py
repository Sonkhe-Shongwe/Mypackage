from setuptools import setup, find_packages


setup(
    name='Mypackage',
    version='0.1',
    packages=find_packages(exclude=['Tests']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<Sonkhe-Shongwe>/<Mypackage>',
    author='<Sonkhe Shongwe>',
    author_email='<shongwesonkhe@gmail.com>'
)