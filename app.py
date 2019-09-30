from sanic import Sanic
from sanic.exceptions import NotFound 

import config
from src.api import inventory_bp

app = Sanic(__name__)
app.config.from_object(config)

app.blueprint(inventory_bp)


if __name__== '__main__':
    app.run(host='127.0.0.1', port='8000')