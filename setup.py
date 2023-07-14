import os

from setuptools import find_packages, setup

with open("README.md", encoding="utf8") as file:
    long_description = file.read()

setup(
    author="Maximilian Mekiska",
    author_email="maxmekiska@gmail.com",
    url="https://github.com/maxmekiska/llmnet",
    description="A solution for the Lost in the Middle phenomenon.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="llmnet",
    version="0.0.1",
    packages=find_packages(include=["llmnet", "llmnet.*"]),
    install_requires=[
        "setuptools >= 41.0.0",
        "openai >= 0.27.5, <= 0.28",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=["machinelearning", "llm", "bots", "context", "optimization"],
    python_rquieres=">= 3.7.0, <= 3.11.0",
)
