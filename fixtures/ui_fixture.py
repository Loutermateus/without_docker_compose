import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")   # Убери, если нужно окно браузера

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(options=options, service=service)

    driver.get("https://qa-windows-1.takeprofittech.com:8000")
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def add_users(request):
    user_count = request.param
    drivers = []

    for _ in range(user_count):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")

        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=options)
        drivers.append(driver)

    yield drivers

    for driver in drivers:
        driver.quit()