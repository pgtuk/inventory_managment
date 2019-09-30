import pytest

from src.Inventory import Inventory


@pytest.fixture(scope='function')
def inventory():
    """
    We don't have create/edit/delete methods yet, 
    but if we would we should refactor this fixture and add teardown() method
    to cleanup enviroment after running tests
    """

    return Inventory()


class TestInventory:
    
    def test_category_for_store_with_known_store(self, inventory):
        categories = inventory.get_categories_for_store(1)

        assert 1 in categories, 'Missing category 1'
        assert 10 in categories, 'Missing category 10'
        assert len(categories) == 2, 'Got some extra undesirable categories'

    def test_category_for_store_with_unknown_store(self, inventory):
        assert not len(inventory.get_categories_for_store(12)), 'Got some cathegories for nonexistent store'

    def test_get_item_inventory_with_existing_item(self, inventory):
        items = inventory.get_item_inventory('shorts')

        assert items, 'Found nothing'
        assert len(items) == 1, 'Found something extra'
        assert items[0]['item_name'] == 'shorts', 'Found wrong items'
        
    def test_get_item_inventory_with_nonexistent_item(self, inventory):
        items = inventory.get_item_inventory('time')

        assert not items, 'Found something'

    def test_get_median_for_category_for_existing_category(self, inventory):
        assert inventory.get_median_for_category(10) == 40, 'Wrong median calculated'

    def test_get_median_for_category_for_nonexisting_category(self, inventory):
        assert inventory.get_median_for_category(12) == None, 'Should return None for empty category'