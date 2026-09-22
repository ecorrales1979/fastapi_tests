from fastapi import FastAPI


def register_routes(app: FastAPI):
    @app.get("/")
    def read_root():
        return {"Hello": "World"}

def create_app():
    app = FastAPI(
        title="My FastAPI App",
        description="This is a sample FastAPI application",
        version="0.1.0"
    )
    register_routes(app)
    return app

app = create_app()
