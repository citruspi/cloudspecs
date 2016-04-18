from setuptools import setup, find_packages
import os


def load_data_files():
    data_files = []

    for root, _, files in os.walk('data'):
        data_files.extend(['{r}/{f}'.format(r=root, f=f) for f in files])

    return [('data', data_files)]


setup(
    name='cloudspecs',
    version='0.0.1',
    author='Mihir Singh (@citruspi)',
    author_email='hello@mihirsingh.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    data_files=load_data_files()
)
