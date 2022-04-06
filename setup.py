from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'Algorithms to find similarity between HTML pages.'
LONG_DESCRIPTION = 'A package that allows to compare website/app HTML page structure. Contains algorithms that find a ' \
                   'similarity rate between two HTML structures.'

# Setting up
setup(
    name="html-matcher",
    version=VERSION,
    author="Pedro Carvalho",
    author_email="<pedrocarvalho812@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    url='https://github.com/officialpedrocarvalho/html-matcher',
    download_url='https://github.com/officialpedrocarvalho/html-matcher/releases/tag/version',
    install_requires=['XlsxWriter', 'parsel', 'lxml', 'apted'],
    keywords=['python', 'website', 'webapp', 'html', 'similarity', 'match', 'rate'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)
