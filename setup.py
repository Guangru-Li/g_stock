from setuptools import setup, find_packages

setup(
    name='g_stock',
    version='0.1.1',
    author='G--R Li',
    author_email='grlee.pku@gmail.com',
    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    description='A short description of your package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
