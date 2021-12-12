import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Добавляем две опции в командную строку теста:
        --language - язык пользователя, по умолчанию - русский
        --browser_name - название браузера, по умолчанию - chrome
    """
    parser.addoption("--language", action="store", default="ru",
                     help="Choose language for web page.Example: pytest --language=es test_items.py")
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser for test: 'chrome' or 'firefox'")


@pytest.fixture(scope="function")
def browser(request):
    """
    Настраиваем браузер и язык пользователя
    """
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    print(f"User language: {user_language}")
    if user_language == "":
        # Пользователь использовал опцию --language, но не задал значение опции
        user_language = "ru"
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser...\n")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser...\n")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()
