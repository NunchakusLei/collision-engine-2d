import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="collision_engine_2d",
    version="0.0.1",
    author="Chenrui Lei",
    author_email="chenrui@ualberta.ca",
    description="A collision engine in 2D space using ray tracing algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NunchakusLei/collision-engine-2d.git",
    packages=setuptools.find_packages(),
    license="Apache",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ),
)