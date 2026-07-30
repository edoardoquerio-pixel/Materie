import azure.functions as func
import logging
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"Hello, {name}! Function deployed via Azure DevOps pipeline.",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Hello! Function deployed via Azure DevOps pipeline. Pass a name parameter for a personalized greeting.",
            status_code=200
        )

@app.route(route="health")
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        "OK",
        status_code=200
    )