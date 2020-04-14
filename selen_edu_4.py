from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #открываем страницу
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #считываем значение х
    x_element = browser.find_element_by_css_selector ("span#input_value")
    print(x_element)
    x = x_element.text
    y = calc(x)

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