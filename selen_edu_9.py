from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    #открываем страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #жмем по летающей кнопке
    browser.find_element_by_css_selector("button").click()
    #переходим на вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #вычисляем и подставляем ответ
    x=int(browser.find_element_by_css_selector("#input_value").text)
    input1=browser.find_element_by_css_selector("input.form-control")
    input1.send_keys(calc(x))
    # нажимаем сабмит
    browser.find_element_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
