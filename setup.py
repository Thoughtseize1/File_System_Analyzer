from setuptools import setup, find_namespace_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='File-System-Analyzer',
    version='0.1.6',
    description="Personal virtual assistant for files in system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
