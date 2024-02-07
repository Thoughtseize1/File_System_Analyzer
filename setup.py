from setuptools import setup, find_namespace_packages

setup(
    name='File-System-Analyzer',
    version='0.1.1',
    description='Personal virtual assistant for files in system.',
    url='https://github.com/Thoughtseize1/File_System_Insight_Tool',
    packages=find_namespace_packages(),
    install_requires=[
        'Faker',
    ],
    entry_points={
        'console_scripts': [
            'hello_my=src.main:main',
        ],
    },
)
