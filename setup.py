import setuptools

proj_name = 'proj_name'
description = "Import or export Excel."
install_requires = []
author = "Supplayer"
author_email = "x254724521@hotmail.com"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='-'.join(proj_name.split('_')),
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{author}/{proj_name}.git",
    packages=setuptools.find_packages(exclude=('tests', '.gitignore', 'requirements.txt')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,
    setup_requires=['setuptools_scm'],
    use_scm_version=True
)
