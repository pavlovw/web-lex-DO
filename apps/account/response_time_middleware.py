import time
import logging

logger = logging.getLogger(__name__)  # Usa el sistema de logs de Django

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Antes de procesar la solicitud
        start_time = time.time()
        
        response = self.get_response(request)  # Procesa la solicitud
        
        # Después de procesar la solicitud
        duration = time.time() - start_time
        logger.info(f"Request to {request.path} took {duration:.4f} seconds")
        
        return response


