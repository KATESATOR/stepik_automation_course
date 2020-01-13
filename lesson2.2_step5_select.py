import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

# Менять линк здесь
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get (link)

    # Считывание значений числе
    number1 = browser.find_element_by_id ( "num1" )
    number2 = browser.find_element_by_id ( "num2" )
    num1 = number1.text
    num2 = number2.text

    # Вычисление
    sum = str(int(num1) + int(num2))

    # Выбор значения в списке
    select = Select( browser.find_element_by_id ( "dropdown" ) )
    select.select_by_visible_text (sum)  # ищем элемент равный сумме чисел

    # Нажатие submit
    submit = browser.find_element_by_css_selector(".btn.btn-default")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()




    # Открыть страницу http://suninjuly.github.io/selects1.html
    # Посчитать сумму заданных чисел
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    # Нажать кнопку "Submit"
