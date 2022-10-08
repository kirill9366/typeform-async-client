from setuptools import find_packages, setup

setup(
    name="atypeform",
    packages=find_packages(),
    version="0.1.0",
    description="Python Library for Async Requests to TypeForm",
    author="kirill9366",
    license="MIT",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
