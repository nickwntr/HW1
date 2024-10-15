from .db import currSession

async def get_db():
    db = currSession()
    try:
        yield db
    finally:
        db.close()