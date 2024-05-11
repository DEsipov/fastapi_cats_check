from starlette.testclient import TestClient

from app.api.cats import WRONG_CAT_NAME
from app.main import app

client = TestClient(app)


def test_create_cat():
    """Тест создания кота."""
    data = dict(name='Barsik', age=3)

    response = client.post(f'/cats', json=data)

    assert response.status_code == 201
    data = response.json()
    print(data)


def test_create_cat_error_name():
    """Тест создания кота."""
    data = dict(name=WRONG_CAT_NAME, age=3)

    response = client.post(f'/cats', json=data)

    assert response.status_code == 422
    data = response.json()
    print(data)


def test_example_error():
    path_param = 'result'
    query_param, query_value = 'num', 11

    response = client.get(f'/example/{path_param}?{query_param}={query_value}')

    assert response.status_code == 422
    data = response.json()
    print(data)
