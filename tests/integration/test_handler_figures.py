from .conftest import create_update_figure
import pytest


def check_figure(f1, f2):
    assert f1["id"] == f2["id"]
    assert f1["name"] == f2["name"]
    assert f1["description"] == f2["description"]
    assert f1["birthdate"] == f2["birthdate"]
    assert f1["date_death"] == f2["date_death"]
    for index, tag in enumerate(f1["tags"]):
        assert tag == f2["tags"][index]


def test_correct_create(client, figures):
    """Test correct post."""
    for figure in figures:
        response = client.post("/api/v1/figures",
                               json=figure)
        assert response.status_code == 201

        figure['id'] = response.json()['id']

        check_figure(figure, response.json())


def test_correct_list(client, figures):
    """Test correct post."""
    response = client.get("/api/v1/figures")
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body) == len(figures)

    for index, figure in enumerate(figures):
        check_figure(figure, response_body[index])


def test_correct_update(client, figures):
    """Test correct post."""
    update = create_update_figure()
    response = client.patch(f"/api/v1/figures/{figures[0]['id']}", json=update)
    assert response.status_code == 200
    figures[0].update(update)
    check_figure(figures[0], response.json())


def test_correct_get(client, figures):
    """Test correct post."""
    response = client.get(f"/api/v1/figures/{figures[0]['id']}")
    assert response.status_code == 200
    check_figure(figures[0], response.json())


def test_correct_delete(client, figures):
    """Test correct post."""
    response = client.delete(f"/api/v1/figures/{figures[0]['id']}")
    assert response.status_code == 204


@pytest.mark.parametrize("figure", [
    {
        "name": "Évariste Galois",
        "description": "Matemático francés, que murió muy joven",
        "birthdate": "1811-10-25",
        "date_death": "1802-05-31",
        "tags": [
            "Matemático",
            "joven"
        ]
    }, {
        "description": "Matemático francés, que murió muy joven",
        "birthdate": "1811-10-25",
        "date_death": "1832-05-31",
        "tags": [
            "Matemático",
            "joven"
        ]
    }, {
        "name": "Évariste Galois",
        "birthdate": "1811-10-25",
        "date_death": "1832-05-31",
        "tags": [
            "Matemático",
            "joven"
        ]
    }, {
        "name": "Évariste Galois",
        "description": "Matemático francés, que murió muy joven",
        "date_death": "1832-05-31",
        "tags": [
            "Matemático",
            "joven"
        ]
    }, {
        "name": "Évariste Galois",
        "description": "Matemático francés, que murió muy joven",
        "birthdate": "abc",
        "date_death": "1832-05-31",
        "tags": [
            "Matemático",
            "joven"
        ]
    }, {
        "name": "Évariste Galois",
        "description": "Matemático francés, que murió muy joven",
        "birthdate": "1811-10-25",
        "date_death": "1832-05-31",
        "tags": "abc"
    }, {
        "name": "Évariste Galois",
        "description": "Matemático francés, que murió muy joven",
        "birthdate": "1811-10-25",
        "date_death": "abc",
        "tags": [
            "Matemático",
            "joven"
        ]
    }])
def test_422_create(client, figure):
    """Test correct post."""
    response = client.post("/api/v1/figures",
                           json=figure)
    assert response.status_code == 422


@pytest.mark.parametrize("figure_id", [
    "abc",
    "zzzzzzzzzzzzzzzzzzzzzzzz"
])
def test_422_get(client, figure_id):
    """Test correct post."""
    response = client.get(f"/api/v1/figures/{figure_id}")
    assert response.status_code == 422


@pytest.mark.parametrize("figure_id", [
    "abc",
    "zzzzzzzzzzzzzzzzzzzzzzzz"
])
def test_422_id_patch(client, figure_id):
    """Test correct post."""
    response = client.patch(f"/api/v1/figures/{figure_id}", json={
        "name": "Évariste Galois",
        "description": "Matemático francés, que murió muy joven",
        "birthdate": "1811-10-25",
        "date_death": "1832-05-31"
    },)
    assert response.status_code == 422


@pytest.mark.parametrize("figure", [
    {
        "date_death": "abc"
    },
    {
        "birthdate": "abc"
    },
    {
        "tags": "abc"
    },
])
def test_422_body_patch(client, figure):
    """Test correct post."""
    figure_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
    response = client.patch(f"/api/v1/figures/{figure_id}", json=figure,)
    assert response.status_code == 422


@pytest.mark.parametrize("figure_id", [
    "abc",
    "zzzzzzzzzzzzzzzzzzzzzzzz"
])
def test_422_delete(client, figure_id):
    """Test correct post."""
    response = client.delete(f"/api/v1/figures/{figure_id}")
    assert response.status_code == 422


def test_404_get(client):
    """Test correct post."""
    figure_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
    response = client.get(f"/api/v1/figures/{figure_id}")
    assert response.status_code == 404


def test_404_patch(client):
    """Test correct post."""
    figure_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
    response = client.patch(f"/api/v1/figures/{figure_id}", json={
        "name": "Évariste Galois",
        "description": "Matemático francés, que murió muy joven",
        "birthdate": "1811-10-25",
        "date_death": "1832-05-31"
    },)
    assert response.status_code == 404


def test_404_delete(client):
    """Test correct post."""
    figure_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
    response = client.delete(f"/api/v1/figures/{figure_id}")
    assert response.status_code == 404
