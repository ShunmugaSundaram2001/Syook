from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException
from .exceptions import InvalidRequest, NotFound

class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            return NotFound()

        if isinstance(exception, APIException):
            return exception

        return InvalidRequest()
