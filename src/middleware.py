import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class LogStatsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        """Log all API requests."""
        start_time = time.time()
        response: Response = await call_next(request)
        endpoint = request.get("endpoint")
        end_time = time.time()
        stats = {
            "endpoint_name": endpoint.__name__ if endpoint else "unknown",
            "status_code": response.status_code,
            "wall_timing": str(end_time - start_time)[:6],
            "method": request.get("method"),
            "path": request.get("path"),
            "client_ip": request.client.host if request.client else "unknown",
        }

        log_message = " ".join([
            f"| {key}={stat_value}"
            for key, stat_value in stats.items()
        ])
        logging.info(f"Request Stats {log_message}")
        return response
