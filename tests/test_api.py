import pytest

from app import app


class TestAPI:

    def test_get_categories_for_store_returns_200(self):
        request, response = app.test_client.get(
            app.url_for('inventory.get_categories_for_store', store=1)
        )
        assert response.status == 200
        assert isinstance(response.json, list), 'Wrong response format'

    def test_get_categories_for_store_returns_empty_response_when_no_store(self):
        request, response = app.test_client.get(
            app.url_for('inventory.get_categories_for_store', store=-1)
        )
        assert response.status == 200
        assert not response.json
        assert isinstance(response.json, list), 'Wrong response format'

    def test_get_categories_for_store_doesnt_accept_non_get_requests(self):
        request, response = app.test_client.post(
            app.url_for('inventory.get_categories_for_store', store=1)
        )
        assert response.status == 405

    def test_get_item_inventory_returns_200(self):
        request, response = app.test_client.get(
            app.url_for('inventory.get_item_inventory', item='shorts')
        )
        assert response.status == 200
        assert isinstance(response.json, list), 'Wrong response format'

    def test_get_item_inventory_returns_200(self):
        request, response = app.test_client.get(
            app.url_for('inventory.get_item_inventory', item='time')
        )
        assert response.status == 200
        assert not response.json
        assert isinstance(response.json, list), 'Wrong response format'

    def test_get_item_inventory_doesnt_accept_non_get_requests(self):
        request, response = app.test_client.post(
            app.url_for('inventory.get_item_inventory', item='shorts')
        )
        assert response.status == 405

    def test_get_median_for_category_returns_200(self):
        request, response = app.test_client.get(
            app.url_for('inventory.get_median_for_category', category=1)
        )
        assert response.status == 200
        assert isinstance(response.json, float) or isinstance(response.json, int), 'Wrong response format'

    def test_get_median_for_category_returns_null_for_empty_category(self):
        request, response = app.test_client.get(
            app.url_for('inventory.get_median_for_category', category=20)
        )
        assert response.status == 200
        assert response.json is None, 'Not null response'

    def test_get_median_for_category_doesnt_accept_non_get_requests(self):
        request, response = app.test_client.post(
            app.url_for('inventory.get_median_for_category', category=1)
        )
        assert response.status == 405
