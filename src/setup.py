from setuptools import setup, find_packages

setup(
    name="pankaj_core",
    version="0.0.1",
    author="Pankaj Pratap Singh",
    author_email="pankajsys.engg@gmail.com",
    description="An example package for testing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
