# pytest-joke

[![Build Status](https://travis-ci.org/alecxe/pytest-joke.svg?branch=master)](https://travis-ci.org/alecxe/pytest-joke)
[![Requirements Status](https://requires.io/github/alecxe/pytest-joke/requirements.svg?branch=master)](https://requires.io/github/alecxe/pytest-joke/requirements/?branch=master)
[![Pyversions](https://img.shields.io/pypi/pyversions/pytest-joke.svg)](https://pypi.python.org/pypi/pytest-joke)
[![PyPI](https://img.shields.io/pypi/v/pytest-joke.svg)](https://pypi.python.org/pypi/pytest-joke)

Running tests is better with some healthy (or not) amount or humor! 😃

This is a completely useless plugin created to get some practice in creating plugins for Pytest.

Powered by [pyjokes][pyjokes].

[pyjokes]: https://pyjok.es/

## Installation 🐍

You can install **pytest-joke** via [pip][pip] from [PyPI][PyPI]:

```bash
$ pip install pytest-joke
```

[pip]: https://pypi.python.org/pypi/pip/
[PyPI]: https://pypi.org/project/pytest-joke/

## Usage

When the plugin is installed, every time a test run results in a failure, the terminal would output a random joke in an attempt to cheer you up.

```bash
Humor-powered output enabled 😃.

plugins: mock-1.10.4, joke-0.1.0
collected 2 items

test_joke.py .F                                                          [100%]

=================================== FAILURES ===================================
_________________________________ test_failed __________________________________

    def test_failed():
>       assert 1 == 2
E       assert 1 == 2

test_joke.py:7: AssertionError
====================== 1 failed, 1 passed in 0.03 seconds ======================

There are two ways to write error-free programs; only the third one works.
```

## TODO

 * make the plugin configurable: turn on/off, language, joke category, number of jokes

## License

Distributed under the terms of the [MIT][mit] license, **pytest-joke** is
free and open source software.

[mit]: http://opensource.org/licenses/MIT
