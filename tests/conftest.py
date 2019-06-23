import pytest


pytest_plugins = "pytester"


@pytest.fixture()
def passing_test(testdir):
    testdir.makepyfile(
        """\
        import pytest

        def test_passed():
            assert 1 == 1
        """
    )
    return testdir


@pytest.fixture()
def failing_test(testdir):
    testdir.makepyfile(
        """\
        import pytest

        def test_failed():
            assert 1 == 2
        """
    )
    return testdir
