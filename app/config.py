import os
from flask import Flask
from sql
################
#    config    #
################
def create_app() -> Flask:
    app = Flask(__name__)
    

    return app

# def register_blueprints(app: Flask):
#     app.register_blueprint(core_blueprint)
#     app.register_blueprint(task_bp)
#     app.register_blueprint(roll_order_bp)
#     app.register_blueprint(remarks_bp)
#     app.register_blueprint(product_blueprint)
#     app.register_blueprint(api_blueprint)
#     app.register_blueprint(api_v2_blueprint)
#     app.register_blueprint(equipments_blueprint)
#     app.register_blueprint(parts_blueprint)
#     app.register_blueprint(units_blueprint)
#     app.register_blueprint(sites_blueprint)
#     app.register_blueprint(laws_blueprint)
#     app.register_blueprint(classification_blueprint)
#     app.register_blueprint(components_parts_blueprint)
#     app.register_blueprint(process_blueprint)

