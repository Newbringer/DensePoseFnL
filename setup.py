#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

def get_version():
    init_py_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "densepose_fnl", "__init__.py")
    if not os.path.exists(init_py_path):
        return "0.1.0"  # default version
    with open(init_py_path, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"\'')
    return "0.1.0"  # default version

if __name__ == "__main__":
    setup(
        name="densepose_fnl",
        version=get_version(),
        author="Emil Bogomolov",
        author_email="",  # Add author email if available
        url="https://github.com/zetyquickly/DensePoseFnL",
        description="Making DensePose fast and light",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        packages=find_packages(),
        python_requires=">=3.6",
        install_requires=[
            "torch>=1.10.1",
            "timm==0.4.12",
            # Detectron2 and DensePose should be installed separately as per README instructions
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
        scripts=[
            "densepose_fnl/train_net.py",
            "densepose_fnl/apply_net.py",
        ],
    )