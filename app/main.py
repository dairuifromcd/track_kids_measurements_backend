from fastapi import FastAPI
from app.api.v1.children import router as child_router
from app.api.v1.measurements import router as measurement_router
from app.api.v1.stats import router as stats_router
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI(title="Track Kids Measurements API", version="0.1")

app.include_router(child_router, prefix="/api/v1/children", tags=["children"])
app.include_router(
    measurement_router,
    prefix="/api/v1/measurements",
    tags=["measurements"]
)
app.include_router(stats_router, prefix="/api/v1/stats", tags=["stats"])
