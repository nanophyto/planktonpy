import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PlanktonPy", # Replace with your own username
    version="0.0.2",
    author="Joost de Vries",
    author_email="joost.devries@bristol.ac.uk",
    description="0D size structered ecosystem model in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://planktopy.readthedocs.io/en/latest/#",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
