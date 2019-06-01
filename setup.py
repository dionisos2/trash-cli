import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='trash-cli',
    version='0.18.1',
    scripts=['trash', 'trash-put', 'trash-list', 'trash-rm', 'trash-empty', 'trash-restore'],
    author="andreafrancia + diverses",
    author_email="",
    description="dionisos version of trash-cli",
    long_description=long_description,
    url="https://github.com/dionisos2/trash-cli.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: linux",
    ],
)
