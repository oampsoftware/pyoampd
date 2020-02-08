import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyoampd_oampsoftware",
    version="0.0.1",
    author="Geoff Nichols",
    author_email="geoff.nichols@oampsoftware.com"
    description="OAMP Management System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oampsoftware/pyoamp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
