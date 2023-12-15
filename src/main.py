import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.responses import JSONResponse

from .routes import planets, stations, systems

logger = logging.getLogger(__name__)


async def exception_handler(request: Request, exception: Exception):
    return JSONResponse(status_code=400, content={"error": str(exception)})


app = FastAPI(docs_url="/openapi", redoc_url=None, exception_handlers={RequestValidationError: exception_handler,
                                                                       ResponseValidationError: exception_handler})
app.include_router(planets.router)
app.include_router(stations.router)
app.include_router(systems.router)


@app.get("/health", include_in_schema=False)
def healthcheck():
    return {"status": "healthy"}
