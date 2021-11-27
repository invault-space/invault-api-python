#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

setup(
    name="invaultapi",
    version="1.0.0-beta",
    packages=find_packages(exclude=["demos", "demos.*", "tests", "tests.*"]),
    description="""invault-api-python""",
    author="Daok Long",
    author_email="plysten@gmail.com",
    url="https://github.com/invault-space/invault-api-go",
    include_package_data=True,
    install_requires=[
        "aiohttp>=3.7.4.post0,<4",
        "pycryptodome>=3.11.0",
        "requests>=2.16.0,<3.0.0",
        "typing-extensions>=3.7.4.1,<4;python_version<'3.8'",
    ],
    python_requires=">=3.6,<4",
    py_modules=["invaultapi"],
    zip_safe=False,
    keywords='invault',
)
