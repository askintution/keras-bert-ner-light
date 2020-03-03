# -*- coding: utf-8 -*-

"""
@Author: Shaoweihua.Liu
@Contact: liushaoweihua@126.com
@Site: github.com/liushaoweihua
@File: setup.py
@Time: 2020/3/3 10:37 AM
"""


import setuptools
from setuptools.command.install import install
from subprocess import call


with open("README.md","r") as f:
    long_description = f.read()


class Installation(install):
    def run(self):
        call(["pip install -r requirements.txt --no-clean"], shell=True)
        install.run(self)


setuptools.setup(
    name="keras_bert_ner_light",
    version="1.0.0",
    author="liushaoweihua",
    author_email="liushaoweihua@126.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liushaoweihua/keras-bert-ner-light.git",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["flask", "keras", "numpy", "GPUtil", "loguru", "requests", "termcolor", "flask_cors", "flask_json", "tensorflow", "keras_contrib", "flask_compress"],
    cmdclass={'install':Installation})