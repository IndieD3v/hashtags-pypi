import setuptools

setuptools.setup(
    name="hashtags",
    version="1.9",
    author="In Dev",
    author_email="tanmaymakode76@gmail.com",
    description="A package to get best hashtags",
    long_description="""

# Installation

``` pip install hashtags```

# Hashtag Package

This is a hashtag package. You can use
to make your social account grow faster
by using this hashtag package.
It can provide you best hashtags,and also provide hashtags by location

# Usage

### Examples

- best_hashtags
- top_hashtags
- hashtag_by_location

```python
    import hashtags

    a = hashtags.best_hashtags('category')
    #                           ('code')

    b = hashtags.top_hashtags()

    c = hashtags.hashtag_by_location('country','category')
    #                                   ('us','food')

```
> All countries are available 
**use only short names eg  _in,us_**

<a href="https://www.patreon.com/bePatron?u=46563102"><img src='https://d33wubrfki0l68.cloudfront.net/d0ed447d8355bce531d091c60296ae2b823d9301/dfb24/assets/img/patron.png'/></a>

""",
    long_description_content_type="text/markdown",
    url="https://github.com/IndieD3v/hashtags-pypi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)