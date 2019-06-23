import pathlib
from setuptools import find_packages, setup


def read(*args):
    file_path = pathlib.Path(__file__).parent.joinpath(*args)
    with file_path.open(encoding="utf-8") as f:
        return f.read()


setup(
    name="pytest-joke",
    version='0.1.0',
    license='MIT',

    description='Test failures are better served with humour.',
    long_description=read("README.md"),

    author='Alexander Afanasyev',
    author_email='me@alecxe.me',
    maintainer='Alexander Afanasyev',
    maintainer_email='me@alecxe.me',

    url='https://github.com/alecxe/pytest-joke',

    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.4",
    install_requires=[
        "pytest>=4.2.1",
        "pyjokes>=0.5.0"
    ],

    entry_points={"pytest11": ["joke = pytest_joke.plugin"]},

    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    keywords=["pytest", "joke", "humour"]
)
