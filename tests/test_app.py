import pytest
from app import app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_resultados_nba(client):
    rv = client.get('/v1/resultados_nba')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert isinstance(json_data, list)
    assert len(json_data) == 3
    assert json_data[0]["time_casa"] == "Los Angeles Lakers"
    assert json_data[1]["pontos_visitante"] == 120
    assert json_data[2]["data"] == "2024-04-24"


esteira_nba-api_cicd
