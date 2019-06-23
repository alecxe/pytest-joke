import pyjokes


def test_header_passing(passing_test):
    result = passing_test.runpytest()

    result.stdout.fnmatch_lines(["Humor-powered output enabled 😃."])


def test_header_failing(failing_test):
    result = failing_test.runpytest()

    result.stdout.fnmatch_lines(["Humor-powered output enabled 😃."])


def test_joke(failing_test, mocker):
    mocker.patch.object(pyjokes.pyjokes,
                        'get_joke',
                        return_value='This is supposed to be funny.')

    result = failing_test.runpytest()

    result.stdout.fnmatch_lines(["This is supposed to be funny."])


def test_no_joke(passing_test, mocker):
    mocker.patch.object(pyjokes.pyjokes,
                        'get_joke',
                        return_value='This is supposed to be funny.')

    result = passing_test.runpytest()

    assert 'This is supposed to be funny.' not in result.stdout.str()
