import pytest
from selene import browser, be


def test_github_desktop(setup_screen_resolution):
    if setup_screen_resolution == "mobile":
        pytest.skip(reason="Пропускаем мобильный тест")

    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


def test_github_mobile(setup_screen_resolution):
    if setup_screen_resolution == "desktop":
        pytest.skip(reason="Пропускаем десктопный тест")

    browser.open("https://github.com")
    browser.element('[aria-label="Toggle navigation"].Button--link ').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
