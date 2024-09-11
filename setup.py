from setuptools import setup, find_packages

setup(
    name="<PKG-NAME>",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "<PKG-DENPENDENCY>",
    ],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description="<SHORT-PKG-DESCRIPTION>",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/<PKG-NAME>",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
