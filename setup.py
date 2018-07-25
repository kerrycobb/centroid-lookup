from setuptools import setup, find_packages

setup(
    name='Centroid-Lookup',
    version='1.0',
    description='Get centroids from global administrative boundary geometry data',
    url='http://github.com/kerrycobb/centroid-lookup',
    author='Kerry A. Cobb',
    author_email='cobbkerry@gmail.com',
    license='GNU',
    packages=find_packages(),
    install_requires=[
        'click',
        'pandas',
        'openpyxl',
    ],
    entry_points={
        'console_scripts':[
            'centroid-lookup=centroid_lookup.cli:cli',
        ]
    },
    package_data={
        'centroid_lookup': [
            'data/*.csv',
        ]
    },
)
