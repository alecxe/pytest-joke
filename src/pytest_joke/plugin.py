from pyjokes import pyjokes


def pytest_report_header():
    return u"Humor-powered output enabled 😃.\n"


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Print out a random joke on non-zero exit code."""
    if exitstatus > 0:
        random_joke = pyjokes.get_joke()

        print()
        print(random_joke)
        print()

    return terminalreporter, exitstatus, config
