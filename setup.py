from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='gxdltk',  # package name
    version='0.4-alpha2-2',  # version
    description="DeepLearning Toolkit for pytorch",
    author='gawainx',
    author_email='liangyi@bupt.edu.cn',
    install_requires=['typer'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License", #https://pypi.org/pypi?%3Aaction=list_classifiers
            "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
)