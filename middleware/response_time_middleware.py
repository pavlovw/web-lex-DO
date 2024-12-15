import time
import logging

logger = logging.getLogger(__name__)

class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()  # Comienza a medir el tiempo
        response = self.get_response(request)
        end_time = time.time()  # Finaliza la medición

        # Calcula el tiempo de respuesta
        response_time = end_time - start_time

        # Registra el tiempo en los logs
        logger.info(f"Tiempo de respuesta para {request.path}: {response_time:.4f} segundos")

        return response
