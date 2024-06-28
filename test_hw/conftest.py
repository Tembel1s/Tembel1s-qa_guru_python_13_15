import pytest
from selene import browser


@pytest.fixture(params=["1920x1080", "1280x720"])
def desktop_screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=["430x932", "428x926"])
def mobile_screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=["1920x1080", "1280x720", "430x932", "428x926"])
def screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=["1920x1080", "1280x720", "430x932", "428x926"])
def setup_screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param in ["1920x1080", "1280x720"]:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
