from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# @app.get("/user/{id}")
# def get_user(id:int):
#     if id == 1:
#         return {"name":"Vansh", "email":"vansh@gmail.com","age":23}
#     raise HTTPException(status_code=404, detail="User not found")

# Custom Error Handler(Global Error Handler)
class UserExceptionHandler(Exception):
    def __init__(self, email:str):
        self.email = email

@app.exception_handler(UserExceptionHandler)
def get_user_error_handler(request:Request, exception:UserExceptionHandler):
    return JSONResponse(status_code=404, content={"status":"error", "message":f"User with email: {exception.email} not exist"})


@app.get("/user/{email}")
def create(email:str):
    if email != "vansh@gmail.com":
        raise UserExceptionHandler(email)
    return {"email":email}