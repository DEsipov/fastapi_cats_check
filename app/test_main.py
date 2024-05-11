from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_example():
    path_param = 'result'
    query_param, query_value = 'num', 9

    response = client.get(f'/example/{path_param}?{query_param}={query_value}')

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert path_param in data
    assert query_value in data


def test_example_error():
    path_param = 'result'
    query_param, query_value = 'num', 11

    response = client.get(f'/example/{path_param}?{query_param}={query_value}')

    assert response.status_code == 422
    data = response.json()
    print(data)


