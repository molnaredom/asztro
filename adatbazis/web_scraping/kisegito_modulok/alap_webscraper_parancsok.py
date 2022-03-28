from selenium.webdriver.support.select import Select


def szoveg_kitoltes(web, xpath, tartalom):
    select = web.find_element_by_xpath(xpath)
    select.clear()
    select.send_keys(tartalom)


def value_alapjan_kivalasztas(web, xpath, value):
    select = Select(web.find_element_by_xpath(xpath))
    select.select_by_value(value)


def raklikkeles(web, xpath):
    web.find_element_by_xpath(xpath).click()