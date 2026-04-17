from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend ishlayapti"}

@app.get("/health")
def health():
    return {"status": "ok"}