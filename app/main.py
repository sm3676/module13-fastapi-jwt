from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.routes import user, calculation, math

app = FastAPI()

# ✅ CORS (frontend connect avadaniki)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # temporary open
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ DB tables create
Base.metadata.create_all(bind=engine)

# ✅ Routes include
app.include_router(user.router)
app.include_router(calculation.router)
app.include_router(math.router)

# ✅ Root test
@app.get("/")
def read_root():
    return {"message": "SHARVANI APP WORKING"}