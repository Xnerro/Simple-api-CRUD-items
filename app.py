from init import *

Base.metadata.create_all(engine)
app.include_router(route)

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=3000, log_level="info", reload=True)
    print("running")