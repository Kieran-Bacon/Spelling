import os
import setuptools

# Read in the readme information for the long description
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as handler:
    README = handler.read()

setuptools.setup(
    name="spelling",
    version="0.0.1",
    description="Efficient spelling implementation",
    long_description=README,
    long_description_content_type="text/markdown",

    author="Kieran Bacon",
    author_email="Kieran.Bacon@outlook.com",
    url="https://github.com/Kieran-Bacon/Spelling",

    packages=setuptools.find_packages(),
    package_data={"": ["*.model"]},
    include_package_data=True
)