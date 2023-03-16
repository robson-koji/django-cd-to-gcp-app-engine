from setuptools import find_packages, setup
import os

# Get more https://pypi.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

EXCLUDE_FROM_PACKAGES = ["project","project.*"]

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name="django-helloworld",
    version="0.1",
    description="CICD Continuous Integration Continuous Delivery of Django to GCP Google AppEngine",
    long_description=read('README.rst'),
    classifiers=CLASSIFIERS,
    keywords="example helloworld django program",
    author="Robson Koji",
    author_email="robson.koji@gmail.com",
    maintainer="Robson Koji",
    maintainer_email="robson.koji@gmail.com",
    url="https://github.com/robson-koji/django-helloworld",
    license="GPL",
    platforms="OS Independent",
    install_requires=["Django==3.2"],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    zip_safe=False,
)
