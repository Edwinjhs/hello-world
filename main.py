from fastapi import FastAPI

app = FastAPI()
a= 'hello'
b= 'world'
@app.get("/")
def read_root():
    return {a: b}