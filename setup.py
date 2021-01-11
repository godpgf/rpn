#coding=utf-8
#author=godpgf

from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

try:
    requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]
except:
    requirements = [str(ir.requirement) for ir in parse_requirements("requirements.txt", session=False)]


setup(
    name='rpn',
    version='0.0.1',
    description='Reverse Polish Notation',
    packages=find_packages(exclude=[]),
    author='godpgf',
    author_email='godpgf@qq.com',
    package_data={'': ['*.*']},
    url='',
    install_requires=requirements,
    zip_safe=False,
    #entry_points={
    #    "console_scripts": [
    #        "rqalpha = rqalpha.__main__:entry_point",
    #    ]
    #},
)