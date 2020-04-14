from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #открываем страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #считываем значение х
    img_element = browser.find_element_by_css_selector ("img#treasure")
    img_value=img_element.get_attribute("valuex")
    # print(img_value)
    # x = img_value.text
    y = calc(img_value)

    # Отправляем заполненную форму
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    #ставим галочки
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()


    # жмем кнопку submit
    button = browser.find_element_by_css_selector('button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()