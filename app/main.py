from fastapi import FastAPI
from app.api.v1.child import router as child_router
from app.api.v1.measurement import router as measurement_router
from app.api.v1.stats import router as stats_router

app = FastAPI(title="Track Kids Measurements API", version="0.1")

app.include_router(child_router, prefix="/api/v1/children", tags=["children"])
app.include_router(
    measurement_router,
    prefix="/api/v1/measurements",
    tags=["measurements"]
)
app.include_router(stats_router, prefix="/api/v1/stats", tags=["stats"])
