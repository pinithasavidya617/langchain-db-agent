from fastapi import FastAPI

from user_routes import router as user_router
app = FastAPI(title="C-Clarke ORM Implementation with DB Agent")

app.include_router(router=user_router)