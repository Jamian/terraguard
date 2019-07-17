import os
from setuptools import setup, find_packages

package_name = "terraguard"
_locals = {}
with open(os.path.join(package_name, "_version.py")) as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]


setup(
    name='terraguard',
    version=version,
    description='Safe guard your Terraformed Environment with simple config driven rulesets.',
    url='https://github.com/jamian/terraguard',
    author='Jamie West',
    author_email='jamieianwest@hotmail.com',
    license='BSD',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Software Development :: Quality Assurance"
    ],
    keywords='terraform python policyenforcement testing qa operations iac',
    packages=find_packages(exclude=['tests',]),
    entry_points={
        'console_scripts': ['terraguard=terraguard.terraguard:main']
    },
    install_requires=[
        'pyyaml',
        'click',
        'crayons'
    ]
)
