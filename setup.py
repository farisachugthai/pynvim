import os
import platform
import sys

from setuptools import find_packages, setup

install_requires = [
    'msgpack>=0.5.0',
    'setuptools'
]

tests_require = [
    'pytest>=3.4.0',
    'tox',
]

dev_require = [
        'flake8',
        'flake8-import-order',
        'isort',
        'flake8-isort',
        'wheel',
        'twine'
    ]

extras_require = {
    'pyuv': ['pyuv>=1.0.0'],
    'docs': ['sphinx', 'sphinx-rtd-theme'],
    'test': tests_require,
    'dev': dev_require,
}

if sys.version_info < (3, 4):
    if os.name == 'nt':
        install_requires.append('pyuv>=1.0.0')
    else:
        # trollius is just a backport of 3.4 asyncio module
        install_requires.append('trollius')

if platform.python_implementation() != 'PyPy':
    # pypy already includes an implementation of the greenlet module
    install_requires.append('greenlet')

setup(name='pynvim',
      version='0.4.1',
      description='Python client to neovim',
      url='http://github.com/neovim/pynvim',
      download_url='https://github.com/neovim/pynvim/archive/0.4.1.tar.gz',
      author='Thiago de Arruda',
      author_email='tpadilha84@gmail.com',
      license='Apache',
      packages=find_packages(include=["pynvim", "neovim"], exclude=["test"]),
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require=extras_require,
      zip_safe=False,

    test_suite="test",
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX:: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        ],
    )
