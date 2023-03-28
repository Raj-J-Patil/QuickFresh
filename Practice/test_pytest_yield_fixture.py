import pytest
@pytest.yield_fixture()
def setup():
    print("\n Test Start")
    yield
    print("\n Test End")

def test_method1(setup):
    print("Test Script 1")


def test_method2(setup):
    print("Test Script 2")


def test_method3():
    print("Test Script 3")

