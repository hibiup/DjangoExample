from setuptools import setup, find_packages
# from examples import __version__

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    python_requires='>={}.{}'.format(*(3, 6)),
    name='DjangoExample',
    author='Jeff',

    version_command='git describe --always --long --dirty=-dev',
    packages=find_packages(
        exclude=['tests', '*.tests', '*.tests.*']
    ),
    package_data={
        '': ['config/*.properties', '*.md', 'requirements.txt'],
    },
    install_requires=requirements,
    test_suite='app1.tests.django_tests.run_tests'
)
