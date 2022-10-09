from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="hello_world_ultimate",
    version="0.0.1",
    author="vicperry",
    author_email="vic.hugx@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vicperry/example_package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)