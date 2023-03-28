import pytest
@pytest.fixture()
def setup():
    print("\n Start test")

def test_method2(setup):
    print("Mehtod 2")

def test_method1(setup):
    print("Mehtod 1")

def test_method3():
    print("Mehtod 3")
