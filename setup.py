from setuptools import setup, find_packages

setup(
    name = 'PyPokerEngine',
    version = '1.0.1',
    author = 'bigben-dev777',
    author_email = 'bigben-dev777086@gmail.com',
    description = 'Poker engine for poker AI development in Python ',
    license = 'MIT',
    keywords = 'python poker emgine ai',
    url = 'https://github.com/bigben-dev777/PyPokerEngine',
    packages = [pkg for pkg in find_packages() if pkg != "tests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    )

