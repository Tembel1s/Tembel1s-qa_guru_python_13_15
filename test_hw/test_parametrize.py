from selene import browser, be
import pytest


desktop_only = pytest.mark.parametrize(
    "screen_resolution", ["1920x1080", "1280x720"], indirect=True
)

mobile_only = pytest.mark.parametrize(
    "screen_resolution", ["430x932", "428x926"], indirect=True
)


@desktop_only
def test_github_desktop_only(screen_resolution):
    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


@mobile_only
def test_github_mobile_only(screen_resolution):
    browser.open("https://github.com")
    browser.element('[aria-label="Toggle navigation"].Button--link ').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


@pytest.mark.parametrize("screen_resolution", ["1920x1080", "1280x720"], indirect=True)
def test_github_desktop(screen_resolution):
    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


@pytest.mark.parametrize("screen_resolution", ["430x932", "428x926"], indirect=True)
def test_github_mobile(screen_resolution):
    browser.open("https://github.com")
    browser.element('[aria-label="Toggle navigation"].Button--link ').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
