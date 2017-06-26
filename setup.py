from setuptools import setup, find_packages

with open("./README.rst") as f:
    LONG_DESCRIPTION = f.read()

with open("./VERSION") as f:
    VERSION = f.read().strip()

setup(
    name='caduceus',
    description='Monitor your requests',
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    author='David Daniel',
    author_email='davydany@aeroxis.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='http://github.com/davydany/caduceus',
    install_requires=['requests>=2.15', 'Django>1.10'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Unix Shell",
        "License :: OSI Approved :: MIT License"]
)
