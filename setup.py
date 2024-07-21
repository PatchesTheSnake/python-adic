from setuptools import find_packages, setup

setup(
    name='adic python',
    packages=find_packages(include=['adic']),
    version='0.1.0',
    description="""provides support of the p-adicts numbers in python""",
    author='Dominic Boccabella',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='/tests',
)