from fastapi import FastAPI
from api.tasks import router as tasrs_router
from api.users import router as users_router
from api.cars import router as cars_router


app = FastAPI(
    title="Упрощенный аналог Jira/Asana"
)


@app.get("/")
def main():
    return {'succec': 'ok'}


app.include_router(tasrs_router)
app.include_router(users_router)
app.include_router(cars_router)
