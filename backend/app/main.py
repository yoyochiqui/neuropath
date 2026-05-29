"""
FastAPI main application for NeuroPath
Infraestructura de Accesibilidad Cognitiva
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from contextlib import asynccontextmanager

from app.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events"""
    # Startup
    logger.info("Starting NeuroPath API Server...")
    yield
    # Shutdown
    logger.info("Shutting down NeuroPath API Server...")


# Initialize FastAPI app
app = FastAPI(
    title="NeuroPath API",
    description="Infraestructura de Accesibilidad Cognitiva - Motor Lumi IA Predictiva",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_CREDENTIALS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error": str(exc)},
    )


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to NeuroPath API",
        "version": "1.0.0",
        "docs": "/api/docs",
        "redoc": "/api/redoc",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "NeuroPath API",
        "version": "1.0.0",
    }


@app.get("/health/ready")
async def readiness_check():
    """Readiness check endpoint"""
    return {
        "ready": True,
        "service": "NeuroPath API",
    }


@app.get("/health/live")
async def liveness_check():
    """Liveness check endpoint"""
    return {
        "alive": True,
        "service": "NeuroPath API",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info",
    )
