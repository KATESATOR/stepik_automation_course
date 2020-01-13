import math
from selenium import webdriver
import time
import pyperclip

# Менять линк здесь
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get (link)

    # Принятие алерта
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    alert0 = browser.switch_to.alert # новая форма, вместо browser.switch_to!_!alert
    alert0.accept()
    value = browser.find_element_by_id("input_value")
    x = value.text

    # Вычисление
    def calc(x):
        return str ( math.log ( abs ( 12 * math.sin ( int ( x ) ) ) ) )
    y = calc ( x )

    # Ввод ответа
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Считывание текста в алерте
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    time.sleep(0)
    answer = alert_text.split(': ')[-1] # возвращает всё, что правее :
    pyperclip.copy(answer)
    print(answer)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    # Нажать на кнопку
    # Принять confirm
    # На новой странице решить капчу для роботов, чтобы получить число с ответом

    # https://github.com/VitaliyYa/sendToStepik авто парсинг и отправка ответов на степик