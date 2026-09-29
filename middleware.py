from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
def test_middleware(request:Request, call_next):
    print("Before Response")

    response = call_next(request)

    print("After Response")

    return response

@app.get("/")
def home():
    return {"message":"Everything working fine"}