import os
from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="series",
    version=f"{os.getenv('BUILD_MAJOR', 0)}.{os.getenv('BUILD_MINOR', 0)}.{os.getenv('BUILD_PATCH', 0)}",
    author="tester",
    description="Project Testing >_",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dummy.io/",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
    ],
    python_requires='>=3.9',
)
