import setuptools
import re


################################################################
description = ""
install_requires = []
packages_include = ('',)
author = "Supplayer"
author_email = "x254724521@hotmail.com"
python_requires = ">=3.6"
################################################################

with open("README.md", "r") as fh:
    long_description = fh.read()

pattern = r'^\#.*'
proj_name = re.search(pattern, long_description).group()[2:]

setuptools.setup(
    name='-'.join(proj_name.split('_')) if '_' in proj_name else proj_name,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{author}/{proj_name}.git",
    packages=setuptools.find_packages(include=packages_include),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=python_requires,
    install_requires=install_requires,
    setup_requires=['setuptools_scm'],
    use_scm_version=True
)
