from setuptools import find_packages, setup

setup(
    name="datastructures",
    version="0.0.1",
    description="""
    This repository contains a collection of Python code examples demonstrating various data structures and algorithms.
    It serves as a reference and learning resource for developers interested in understanding and implementing these concepts in Python.
    """,
    author="Valdemar Landberg",
    author_email="valdemar.landberg@live.dk",
    license="MIT",
    url="https://github.com/valdemarmtl/datastructures",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operatisng System :: OS Independent",
        "Programming Language :: Python :: 3.10",
    ],

    python_requires=">=3.10",

    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,

    bdist_wheel={"universal": 1},
)
