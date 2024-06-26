
import json

import uvicorn

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import ORJSONResponse, Response
from rich import print


app = FastAPI(
    title="test graph api",
    docs_url="/docs",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    version="0.1.0",
)

emails_counter = 0

@app.post("/test-emails", status_code=202)
async def test_emails(request: Request):
    global emails_counter
    print(f"emails {emails_counter}")
    emails_counter += 1
    
    if validation_token := request.query_params.get("validationToken"):
        return Response(
            content=validation_token,
            media_type="text/plain",
            status_code=200,
        )
        
    body = await request.json()
    print("headers")
    print(request.headers)
    print("data")
    print(json.dumps(body, indent=4))
    
    print("done")
    return 

@app.post("/lifecycle-notifications", status_code=202)
async def test_lifecycle(request: Request):
    print("lifecycle")
    if validation_token := request.query_params.get("validationToken"):
        return Response(
            content=validation_token,
            media_type="text/plain",
            status_code=200,
        )
        
    body = await request.json()
    print("headers")
    print(request.headers)
    print("data")
    print(json.dumps(body, indent=4))
    
    return 


@app.post("/test-folders", status_code=200)
async def test_folders(request: Request):
    print("folders")
    
    if validation_token := request.query_params.get("validationToken"):
        return Response(
            content=validation_token,
            media_type="text/plain",
            status_code=200,
        )
    
    body = await request.json()
    print(json.dumps(body, indent=4))
    
    return 


if __name__ == "__main__":
    uvicorn.run(
        "graph_api_notifications.main:app",
        host="127.0.0.1",
        port=8080,
        reload=True,
    )