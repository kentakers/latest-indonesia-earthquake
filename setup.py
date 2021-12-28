import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LatestEarthQuake-Indonesia",
    version="0.1",
    author="Aditya Tariqh",
    author_email="aditya.tariqh@gmail.com",
    description="This package will get the latest earthquake from BMKG | Meteorology, Climatology, and Geophysical Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kentakers/latest-indonesia-earthquake",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.8.5",
)
