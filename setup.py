from setuptools import setup, find_packages 
import codecs 
import os 

here = os.path.abspath(os.path.dirname(__file__)) 

# Get the long description from the relevant file 
def readme():
    with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    # Application name
    name="hello_travis",

    # Versions should comply with PEP440. For single-sourced versioning, see 
    # http://packaging.python.org/en/latest/tutorial.html#version 
    version=0.2,

    description="Continuous Integration with Travis CI",
    long_description=readme(),

    # The project URL
    url="http://github.com/jaingaurav001/hello-travis",

    # Author details
    author="Gaurav Jain",
    author_email="jaingaurav001@gmail.com",

    # Choose your license
    # license="LICENSE.txt",
    license='MIT', 

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Project maturity
        'Development Status :: 3 - Alpha',
        # Intended audience
        'Intended Audience :: Developers', 
        # Topic
        'Topic :: Text Processing :: Linguistic',
        # License should match "license" above
        'License :: OSI Approved :: MIT License',
        # Python versions supported
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='python travis-ci',

    # Packages
    packages=find_packages(),

    # Dependent packages (distributions)
    install_requires=[],

    setup_requires=["setuptools_scm", "wheel"],

    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],

    # Include additional files into the package.
    # MANIFEST.in included entries should be included as package data and 
    # installed into site-packages.
    include_package_data=True,

    # Default to False unless you specifically intend the package to be 
    # installed as an .egg
    zip_safe=False
)