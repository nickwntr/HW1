def test_function():
    print("lorem ipsum")
    def inner_function():
        print("Внутри функции test_function")
    inner_function()
    return 0