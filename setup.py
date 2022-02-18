from setuptools import setup, find_packages

setup(
    name='jiracapex',
    version='0.1.0',
    packages=find_packages(include=['jiracapex', 'jiracapex.*']),
    description='Jira Analytics',
    author='Aleksey Beregov',
    install_requires=[
        'certifi==2021.10.8',
        'charset-normalizer==2.0.12',
        'idna==3.3',
        'requests==2.27.1',
        'urllib3==1.26.8'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)


