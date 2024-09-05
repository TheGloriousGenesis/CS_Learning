from fastapi import FastAPI

app = FastAPI()


@app.get("/status")
async def root():
    return {'status': 'it works!'}

@app.get("/save")
async def save():
    # write up depends on db and save some data to db
    ...