import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Conductor",
    version = "0.0.0",
    author = "Nandan Tumu",
    author_email = "renukanandan.tumu@uconn.edu",
    description = ("Conductor is an orchestration platform for robots"),
    license = "CC-BY-NC-SA",
    keywords = "example documentation tutorial",
    url = "https://github.com/nandantumu/conductor",
    packages=['conductor'],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
    ],
)