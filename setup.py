from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('VERSION', 'r') as ver:
    version = ver.readline()

setup(
        name='pollux',  # package name
        version=version,  # version
        description="pollux is the β Geminorum",
        author='gawainx',
        author_email='liangyi@bupt.edu.cn',
        install_requires=['typer'],
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        scripts=['bin/pollux', 'bin/pollux-pip'],
        packages=setuptools.find_packages(),
)
