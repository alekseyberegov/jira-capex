from setuptools import setup, find_packages

setup(
    name='jiracapex',
    version='0.1.0',
    packages=find_packages(include=['jiracapex', 'jiracapex.*']),
    description='Jira Analytics',
    author='Aleksey Beregov',
    install_requires=[
        'attrs==21.4.0',
        'certifi==2021.10.8',
        'charset-normalizer==2.0.12',
        'click==8.0.4',
        'idna==3.3',
        'iniconfig==1.1.1',
        'packaging==21.3',
        'pluggy==1.0.0',
        'py==1.11.0',
        'pyparsing==3.0.7',
        'pytest==7.0.1',
        'requests==2.27.1',
        'tomli==2.0.1',
        'urllib3==1.26.8',
        'pandas==1.4.1',
        'numpy==1.22.2',
        'python-dateutil==2.8.2',
        'pytz==2021.3',
        'six==1.16.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)



