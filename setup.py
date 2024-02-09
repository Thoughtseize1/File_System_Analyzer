from setuptools import setup, find_namespace_packages

setup(
    name='File-System-Analyzer',
    version='0.1.4',
    description="Personal virtual assistant for files in system.",
    url='https://github.com/Thoughtseize1/File_System_Insight_Tool',
    author="Mykyta Sherstianykh",
    author_email="mykyta.sherstianykh@gmail.com",
    packages=find_namespace_packages(),
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'file-analyzer=src.main:main',
        ],
    },
)
