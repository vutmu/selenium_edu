from selenium import webdriver
import time
import os

try:
    #открываем страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #заполняем поля
    input1 = browser.find_element_by_css_selector("input[name=firstname]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input[name=lastname]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input[name=email]")
    input3.send_keys("ya@mail.ru")
    #загружаем файл
    upload=browser.find_element_by_css_selector("input[type=file]")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'dict.txt')
    upload.send_keys(file_path)
    #нажимаем submit
    browser.find_element_by_tag_name('button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
