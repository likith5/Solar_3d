from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request  # Import the Request class
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static/", StaticFiles(directory="static"), name="static")


@app.post("/login/")
async def login(
    request:Request,

    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    templates = Jinja2Templates("templates")
    print(password)
    print(username)
    # return username
    if password=="qwerty":
        return templates.TemplateResponse("index.html",context={"request":request})
    else:
        return {f"Wrong password bro" ,username}



@app.get('/')
async def home(request:Request):
     templates = Jinja2Templates("templates")
     return templates.TemplateResponse('log.html',context={"request":request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
