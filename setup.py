#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# ___  ___                       _____           _______
# |  \/  |                      |_   _|         | | ___ \
# | .  . |_   _ ___  ___  ___     | | ___   ___ | | |_/ / _____  __
# | |\/| | | | / __|/ _ \/ _ \    | |/ _ \ / _ \| | ___ \/ _ \ \/ /
# | |  | | |_| \__ \  __/ (_) |   | | (_) | (_) | | |_/ / (_) >  <
# \_|  |_/\__,_|___/\___|\___/    \_/\___/ \___/|_\____/ \___/_/\_\
#
# @author:  Nicolas Karasiak
# @site:    www.karasiak.net
# @git:     www.github.com/nkarasiak/MuseoToolBox
# =============================================================================
import re

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    open('museopheno/__init__.py').read()).group(1)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='museopheno',
    version=__version__,
    description='Time series and spectral indice management for Remote Sensing Sensors',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nkarasiak/MuseoPheno',
    author='Nicolas Karasiak',
    author_email='karasiak.nicolas@gmail.com',
    license='GPLv3',
    install_requires=["numpy","scipy","matplotlib","scikit-learn","joblib","museotoolbox"],
    packages=setuptools.find_packages(),
    classifiers=[
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: GIS",
            "Programming Language :: Python :: 3",
            "Intended Audience :: Science/Research"],
    zip_safe=False,
    package_data={
      'museopheno': ['datasets/2018_3A_Theia_Bouconne.tif']
   }
 )