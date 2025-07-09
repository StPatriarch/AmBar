from setuptools import setup, find_packages

setup(

    name='ambar',
    version='0.0.0725',
    packages=find_packages(),
    install_requires=[
        'colorama>=0.4.6',
        'openpyxl>=3.1.5',
        'setuptools>=80.9.0',
    ],
    author='Stpatrirach',
    description='Այս պարզ կսրիպտը նախատեսված է օգնելու կատարել իվենտարիզացիա',
    python_requires='>=3.7',

)
