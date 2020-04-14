from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    #открываем страницу
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #считываем значение х
    x_element = browser.find_element_by_css_selector ("#input_value")
    x=int(x_element.text)
    # print(img_value)
    # x = img_value.text
    y = calc(x)

    # Отправляем заполненную форму
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    #скроллим страницу до чекбокса и жмем
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()


    #скроллим страницу до радиокнопки и жмем
    rbutton = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rbutton)
    rbutton.click()

    # жмем кнопку submit
    button = browser.find_element_by_css_selector('button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()