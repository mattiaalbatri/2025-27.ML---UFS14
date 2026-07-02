def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def main():
    print(func(3))


if __name__ == "__main__":
    main()