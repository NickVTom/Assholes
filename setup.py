from setuptools import setup, find_packages

setup(
    name='assholes',
    version='0.1.0',
    packages=find_packages(),
    description='A custom utility package for statistical analysis and visualization.',
    author='Nicklas',
    author_email='nicklasthomsenaau@gmail.com',
    url='https://github.com/NickVTom/assholes',
    install_requires=[
        'pandas',
        'matplotlib',
        'statsmodels',
        'matplotlib.pyplot'
        'scipy'
        'numpy'
        'sympy'
        'statistics'
        # Add other dependencies here
    ],
)
