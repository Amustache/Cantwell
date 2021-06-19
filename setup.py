import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soundletter",
    version="0.3",
    author="Stache",
    author_email="stache@stache.cat",
    description="Visual sound waves letters generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Amustache/Cantwell/",
    project_urls={
        "Bug Tracker": "https://github.com/Amustache/Cantwell/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["matplotlib<3.5",
                      "gtts<2.3",
                      "pydub<0.26",
                      "pillow<8.3"],
)
