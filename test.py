import requests

def test_example():
    assert 2 + 2 == 4

def test_network():
    response = requests.get("https://httpbin.org/get", timeout=10)
    assert response.status_code == 200


if __name__ == "__main__":
    test_example()
    test_network()
    print("Barcha testlar muvaffaqiyatli o'tdi!")
