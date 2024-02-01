from setuptools import find_packages, setup

with open('README.md', encoding='utf8') as file:
    long_description = file.read()

setup(
    author='Maximilian Mekiska',
    author_email='maxmekiska@gmail.com',
    url='https://github.com/maxmekiska/llmnet',
    description='A library designed to harness the diversity of thought by combining multiple LLMs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='llmnet',
    version='0.1.1',
    packages=find_packages(include=['llmnet', 'llmnet.*']),
    install_requires=[
        'openai >= 0.27.5, <= 0.28',
        'google-generativeai >= 0.3.1, <= 0.4.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords=['machinelearning', 'llm', 'bots', 'network'],
    python_rquieres='>= 3.9.0, < 3.12.0',
)
