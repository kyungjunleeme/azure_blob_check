from setuptools import setup, find_packages

setup(
    name='azure_blob_check',
    version='1.0',
    description='azure blob filelist check',
    author='Kyung Jun Lee',
    author_email='kyungjunlee.me@gmail.com',
    url='https://github.com/kyungjunleeme/azure_blob_check',
    download_url='https://github.com/kyungjunleeme/azure_blob_check/archive/main.zip',
    packages=find_packages(exclude=['docs', 'tests*']),
    long_description=open('README.md').read(),
    install_requires=[],
    keywords=['azure_blob', 'blob_list'],
    python_requires='>=3.6',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
