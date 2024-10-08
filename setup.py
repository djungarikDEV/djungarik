from setuptools import setup, find_packages

setup(
    name="djungarik",
    version="0.1.4a1",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    author="djungarik_DEV",
    author_email="arnispprt@gmail.com",
    description="Djungarik — A simple Tkinter-based UI package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/djungarikDEV/djungarik",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
