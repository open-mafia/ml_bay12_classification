
from setuptools import setup, find_packages

import ml_bay12

setup(
    name="ml_bay12",
    description=ml_bay12.__doc__,
    version=ml_bay12.__version__,
    author="Open Mafia Team",
    author_email="openmafiateam@gmail.com",  
    packages=find_packages(),
    install_requires=[
        # Skipping, as we have our env already
    ],
)
