from setuptools import setup

def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data

setup(
    name = 'JustPot',
    version = '1.0.0',
    description = 'Simple TCP honeypot',
    long_description = readme_file_contents(),
    author = 'Saransh',
    author_email = 'jainsaransh09051999@gmail.com',
    license = 'MIT',
    packages = ['JustPot'],
    #scripts= ['bin/JustPot','bin/JustPot.bat']
    zip_safe = False,
    install_requires = ['docopt']
)