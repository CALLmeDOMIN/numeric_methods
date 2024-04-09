from setuptools import setup, find_packages

setup(
    name='numeric_methods',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    author="Dominik Sieroń",
    author_email="contact@dsieron.pl",
    description="Package with some numerical methods",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
