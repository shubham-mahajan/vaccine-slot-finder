import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="vaccine-slot-finder",
    version="0.0.1",
    description="The Project to find the vaccine on the basis of age, location, district, pincode, available slot and notified via email, slack or google chat",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/shubham-mahajan/vaccine-slot-finder",
    author="Shubham Mahajan",
    author_email="contact@binarybugs.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[
        "requests", "python-dotenv"
    ]
)