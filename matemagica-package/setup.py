from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="matemagica",
    version="0.0.1",
    author="Leonardo",
    author_email="",
    description="Used to perform some math operations more intuitively",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lborgatow/dio_bootcamps/tree/main/matemagica-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
