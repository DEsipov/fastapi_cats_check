from starlette.testclient import TestClient

from app.core.const import WRONG_CAT_NAME
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


def test_get_cats():
    """Тест список котов."""
    response = client.get(f'/cats')

    assert response.status_code == 200
    data = response.json()
    print(data)

