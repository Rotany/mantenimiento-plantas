from flask import Blueprint, request

image_bp = Blueprint('image', __name__)


@image_bp.route('/predict', methods=['POST'])
def image():
    try:
        print(request.files['planta_imagen'])
        return "hello"
    except Exception as e:
        return "chao"

