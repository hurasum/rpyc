import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    long_license = fh.read()

setuptools.setup(
    name="rpyc_custom",
    version="5.3.0",
    author="Tomer Filiba, Fork by Daniel Kriwitz",
    author_email="",
    description="Package to create custom rpyc",
    long_description=long_description,
    long_license=long_license,
    long_description_content_type="text/reStructuredText",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
