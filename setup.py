from setuptools import setup, find_packages

setup(
    name="hello-python",
    version="0.1",
    packages=find_packages(),
    install_requires = [ 'hello_python_library' ],
    entry_points={
        'console_scripts': [
            'hello = hello:hello',
        ],
    }
)
