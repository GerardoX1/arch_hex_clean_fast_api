from fastapi import FastAPI, Request

from app.adapters.api.routers.user_router import router as user_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user_router, prefix="/users", tags=["Users"])
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
