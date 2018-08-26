import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="onboard", help="my option: onboard or cc"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")