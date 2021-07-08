#!/usr/bin/env python


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab_intake_data"

version = None
init_py = os.path.join(package_name.replace("-", "_"), "__init__.py")
for line in read(init_py).split("\n"):
    if line.startswith("__version__"):
        version = line.split("=")[-1].strip()[1:-1]
assert version


extras_require = {}

setuptools.setup(
    name=package_name,
    version=version,
    description="A dataset plugin for climetlab for the dataset intake-data/noaa-ersst.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Ashwin Samudre",
    author_email="capnoi8@gmail.com",
    url="https://github.com/kiryteo/climetlab-intake-data",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["climetlab>=0.5.6"],
    extras_require=extras_require,
    zip_safe=True,
    entry_points={
        "climetlab.datasets": [
            "intake-data-noaa-ersst = climetlab_intake_data.noaa_ersst:NoaaErsst",
            # "intake-data-other-dataset = climetlab_intake_data.other_dataset:OtherDatasetClass",
        ]
    },
    keywords="meteorology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
