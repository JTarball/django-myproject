from setuptools import setup

import myproject

setup(
    name="django-myproject",
    version="0.1.0",
    description="Reusable, generic project for Django",
    long_description="A basic default django project perfect for something.",
    keywords="django",
    author="James Tarball <james.tarball@gmail.com>",
    author_email="james.tarball@gmail.com",
    url="https://github.com/JTarball/django-myproject",
    license="MIT license",
    packages=["myproject"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
    ],
)
