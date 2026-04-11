import logging

request_logger = logging.getLogger("request_logger")
error_logger = logging.getLogger("error_logger")

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        log_message = f"{request.build_absolute_uri()}"

        if response.status_code >= 400:
            error_logger.warning(log_message)
        else:
            request_logger.info(log_message)

        return response