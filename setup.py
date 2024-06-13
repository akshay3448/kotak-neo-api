from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "1.2.0"
# To install the library, run the following
#
# python setup.py install


setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API",
    author="ne API",
    author_email="",
    url="",
    keywords=["Neo-Trade API", "Neo Trade API's"],
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)
