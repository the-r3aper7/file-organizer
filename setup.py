from setuptools import setup, find_packages

setup(
    name="fileorganizer",
    version="0.1.0",
    packages=find_packages(),
    scripts=['bin/fileorganizer'],
    author="Sai Srikar Dumpeti",
    author_email="saisrikardumpeti@gmail.com",
    description="A tool to organize files from Downloads folder",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/the-r3aper7/file-organizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)