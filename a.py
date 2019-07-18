import dis


def func1(a: int, b: str):
    print(f'{a:10}')
    print(sum(20, 30))

dis.dis(func1)

