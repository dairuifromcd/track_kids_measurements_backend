from fastapi import FastAPI
from app.api.v1.child import router as child_router

app = FastAPI(title="Track Kids Measurements API", version="0.1")

app.include_router(child_router, prefix="/api/v1/children", tags=["children"])