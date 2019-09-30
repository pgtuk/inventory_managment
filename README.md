# inventory_managment

To run locally:
> $ make run

To run tests:
> $ make test


## Question 3

Main problem is in data storage model. 
  - We don't have create/edit/delete operation for now, but if we had them, we'd have all sorts of problems with data consistency for more then 1 user.
  - When inventory size grows up, we'll need more sophisticated `Inventory._load()` to handle it and still be able to search our data.
  - Time complexities: 
      - `get_categories_for_store()` - O(n). 
      - `get_item_inventory()` - O(n), because we have constant restriction on item_name size, otherwise it would be O(n*k)
      - `get_median_for_category()` - O(n).
      
All this problems could be addressed by using convinient relational database. It will guarantee ACID compliense, dataset growth would not result on perfomance so dramatically, time complexities of serach operations would go down to O(log(n)).
