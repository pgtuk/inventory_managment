import json
import statistics

import config


class Inventory:
    """
    Inventory Management system 
    """

    def __init__(self):
        self.items = self._load()
    
    def _load(self):
        with open(config.INVENTORY_PATH) as f:
            json_data = json.loads(f.read())

        return json_data

    def get_categories_for_store(self, store):
        """
        Given a store id you should return all the categories ids in the inventory.
        :param store: store id
        :return: all the categories ids in the inventory
        """
        # use set generator to avoid duplicates and convert result to list
        return list({item['category'] for item in self.items if item['store'] == store})

    def get_item_inventory(self, item):
        """
        Given items name return all the items across all stores.
        :param item: item name
        :return: all the items across all stores
        """
        return [item_ for item_ in self.items if item_['item_name'] == item]

    def get_median_for_category(self, category):
        """
        Given category id return the median of the prices for all items in the category.
        :param category: category name
        :return: the median of the prices for all items in the category
        """
        category_items_prices = [item['price'] for item in self.items if item['category'] == category]

        if not category_items_prices:
            return None
        
        return statistics.median(category_items_prices)


inventory = Inventory()
