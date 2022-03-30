from functools import wraps
from flask import  jsonify, request,abort
from loguru import logger

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # token = None
        # if "Authorization" in request.headers:
        #     token = request.headers["Authorization"].split(" ")[1]
        # if not token and not DEV_MODE :
        #     return handle_error.response_error("Access Token is missing", 401)
        # try:
        #     access_token = get_access_token()
           
        #     if access_token is None:
        #         return handle_error.response_error("Invalid Access Token", 401)
        # except Exception as e:
        #     return handle_error.response_error("Something went wrong", 500)
        logger.info("middleware processing..")
        return f(*args, **kwargs)
    return decorated