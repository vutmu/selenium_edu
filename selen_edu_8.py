from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))
try:
    #открываем страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #жмем кнопку
    button=browser.find_element_by_css_selector("button.btn")
    button.click()
    #жмем ок в конфирме
    confirm = browser.switch_to.alert
    confirm.accept()
    #вычисляем и подставляем ответ
    x=int(browser.find_element_by_css_selector("#input_value").text)
    input1=browser.find_element_by_css_selector("input.form-control")
    input1.send_keys(calc(x))
    #нажимаем сабмит
    browser.find_element_by_tag_name("button").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
