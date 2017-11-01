from setuptools import setup, find_packages
from codecs import open
from os import path
from sys import version_info

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = __import__('VERSION').__version__
IS_PY2 = version_info[0] < 3

if IS_PY2:
    saml_package = 'python-saml'
else:
    saml_package = 'python3-saml'

print(saml_package)

if __name__ == "__main__":

    setup(
        name='django-saml2-pro-auth',
        version=version,
        description="SAML2 authentication backend for Django wrapping OneLogin's python-saml package https://github.com/onelogin/python-saml",
        long_description=long_description,
        url='https://github.com/MindPointGroup/django-saml2-pro-auth',
        author='Jonathan I. Davila',
        author_email='jonathan@davila.io',
        license='MIT',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Framework :: Django :: 1.10',
            'Framework :: Django :: 1.11',
            'Topic :: Security',
            'Topic :: System :: Systems Administration :: Authentication/Directory',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
        ],

        keywords='authentication saml saml2 django development',
        packages=find_packages(where="src"),
        package_dir={
            '': 'src',
        },
        install_requires=[
            saml_package,
            'six'
        ],
        tests_require=[
            'django',
            'coverage',
            'pylint',
            'pep8',
            'pyflakes',
            'coveralls'
        ],
        extras_require={
            'dev': ['check-manifest'],
        },
        test_suite='tests',
        include_package_data=True,

    )
