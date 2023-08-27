from rest_framework.exceptions import APIException

class InvalidRequest(APIException):
    status_code = 400
    default_detail = "Invalid request data."
    default_code = "invalid_request"

class NotFound(APIException):
    status_code = 404
    default_detail = "Resource not found."
    default_code = "not_found"
