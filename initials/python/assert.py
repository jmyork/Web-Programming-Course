def square(x):
    return x + x

try:
    for index in range(100,1):
        assert square(10)==100
        print(f"{index} passed away")
except AssertionError:
    print("There is an assetion error!")