# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='azure_blob_check',
    version='2.0',
    description='azure blob filelist check',
    author='Kyung Jun Lee',
    author_email='kyungjunlee.me@gmail.com',
    url='https://github.com/kyungjunleeme/azure_blob_check',
    download_url='https://github.com/kyungjunleeme/azure_blob_check/archive/main.zip',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['azure-storage-blob', 'pytz', 'pandas', 'openpyxl'],
    entry_points={'console_scripts': [
        'blob_check=azure_blob_check.blob_check:main']},
    keywords=['azure_blob', 'blob_list'],
    python_requires='>=3.6',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
