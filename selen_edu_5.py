from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
try:
    #открываем страницу
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # находим элемент с вопросом
    x=browser.find_element_by_css_selector ("#num1")
    x_value = int(x.text)
    y=browser.find_element_by_css_selector ("#num2")
    y_value=int(y.text)
    z=str(x_value+y_value)
    #находим выпадающий список
    dropdown = Select(browser.find_element_by_css_selector ("#dropdown"))
    #находим правильный ответ
    dropdown.select_by_visible_text(z)
    # жмем кнопку submit
    button = browser.find_element_by_css_selector('button')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()