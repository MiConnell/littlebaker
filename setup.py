from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="littlebaker",
    version="0.0.1",
    packages=find_packages(),
    author="Michael Connell",
    author_email="connellmp@gmail.com",
    description="Package to auto-generate lists, dictionaries, arrays, matricies (list-of-lists), json, csv files, and Pandas Dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
