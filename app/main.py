from fastapi import FastAPI

from app.api import router


def create_app():
    app = FastAPI(
        title="My FastAPI App",
        description="This is a sample FastAPI application",
        version="0.1.0"
    )

    app.include_router(router)

    return app

app = create_app()
