from sanic import Blueprint
from sanic import response, exceptions

from src.Inventory import inventory

inventory_bp = Blueprint('inventory', url_prefix='/api/inventory')


@inventory_bp.route('/store/<store:int>/category/list', methods=['GET'])
async def get_categories_for_store(request, store):
    return response.json(inventory.get_categories_for_store(store))


@inventory_bp.route('/<item:[A-z0-9]{1,64}>', methods=['GET'])
async def get_item_inventory(request, item):
    return response.json(inventory.get_item_inventory(item))


@inventory_bp.route('/category/<category:int>/median', methods=['GET'])
async def get_median_for_category(request, category):
    return response.json(inventory.get_median_for_category(category))


### Common error handlers

@inventory_bp.exception(exceptions.NotFound)
async def handle_404(request, exception):
    return response.html('Not found', status=404)


@inventory_bp.exception(exceptions.MethodNotSupported)
async def handle_405(request, exception):
    return response.html('Not allowed', status=405)

@inventory_bp.exception(exceptions.ServerError)
async def handle_500(request, exception):
    return response.html('Server error', status=500)