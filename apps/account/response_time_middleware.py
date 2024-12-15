# apps/account/response_time_middleware.py

import time
from django.utils.deprecation import MiddlewareMixin
import logging

# Configura el logger
logger = logging.getLogger('django')

class ResponseTimeMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        start_time = time.time()
        response_time = time.time() - start_time
        # Puedes registrar el tiempo de respuesta
        logger.info(f"Response time: {response_time:.4f} seconds")
        return response

