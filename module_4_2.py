def test_function():


    def inner_function():
        print("Я в области видимости функции test_function")


    print("    #")
    print("    Вызов функцию inner_function внутри функции test_function -  выдаёт пустой результат...")
    print("    #")
    inner_function()


print("Вызов функцию inner_function в основной программе")
print("Выдаёт ошибку: NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?")
# inner_function() # Выдаёт ошибку: "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?"
# Ошибка NameError: имя "внутренняя функция" не определено. Вы имели в виду "тестовая функция"?

test_function()
