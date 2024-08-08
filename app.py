from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, Semgrep Evening!"}

user_input = "print('Hello, World!')"
eval(user_input)