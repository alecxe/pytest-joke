from pyjokes import pyjokes


def pytest_report_header():
    return "Humor-powered output enabled."


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Print out a random joke on non-zero exit code."""
    if exitstatus > 0:
        random_joke = pyjokes.get_joke()
        print(random_joke)

    return terminalreporter, exitstatus, config
