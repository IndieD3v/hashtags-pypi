# from setuptools import setup

# setup(
#     name="All Hashtags",
#     version="1.4", 
#     description="",
#     author="In Dev",
#     packages=["hashtags"],
#     install_requires=[]
# )

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hashtags",
    version="1.4",
    author="In Dev",
    author_email="tanmaymakode76@gmail.com",
    description="A small example package",
    long_description="""
# Install
windows ``` pip install hashtags```
linux   ``` pip3 install hashtags```

# Hashtag Package

This is a hashtag package. You can use
to make your social account grow faster.
by using this hashtag package.

# Examples

- best_hashtags
- top_hashtags
- hashtag_by_location

## Using the package

```python
    import hashtags

    a = hashtags.best_hashtags('category')#eg ('code')('cars')

    b = hashtags.top_hashtags()

    c = hashtags.hashtag_by_location('country','category')
    #eg                         ('us','food')('in','games')

```
> All countries are available **use only short names eg _in,us_**
""",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)