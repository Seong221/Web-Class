from fastapi import FastAPI

import requests

app=FastAPI()


@app.get("/")
def root():
    URL="https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCD=12&apiKey=cu3z69qA0ce88cnS5wI8K0QJRoe3tTA3OVs641U5&returnType=json"
    

    contents=requests.get(URL).text

    return {"message":contents}

