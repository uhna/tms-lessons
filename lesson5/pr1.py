def hello_world_1():
    print("Hello world!")

hello_world_1()


def hello_world_2():
    return "Hello world!"

print(hello_world_2())


def hello_1():
    input_name = input(f"Введите свое имя: ")
    print(f"Hello {input_name}")

hello_1()

def hello_2():
    input_name = input(f"Введите свое имя: ")
    return f"Hello {input_name}"

print(hello_2())