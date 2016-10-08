from setuptools import setup

import myapp

setup(
    name="django-myapp",
    version="0.1.0",
    description="Reusable, generic app for Django",
    long_description="A basic app perfect for something.",
    keywords="django",
    author="James Tarball <james.tarball@gmail.com>",
    author_email="james.tarball@gmail.com",
    url="https://github.com/JTarball/django-myapp",
    license="MIT license",
    packages=["myapp"],
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
