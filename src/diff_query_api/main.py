from diff_query_api.diff_query_models import DiffQueryGetDiffRequest, DiffQueryCallModelRequest
from diff_query_api.diff_query_functions import DiffQueryExecutor
from fastapi import FastAPI


app = FastAPI()
diff_query_executor = DiffQueryExecutor()

@app.get("/")
def index():
    return "Hello world"

@app.post("/get-diff/")
def get_diff(diffQueryRequest: DiffQueryGetDiffRequest):
    return diff_query_executor.get_diff(diffQueryRequest)

@app.post("/call-model")
def call_model(diffQueryRequest: DiffQueryCallModelRequest):
    return diff_query_executor.call_model(diffQueryRequest)

# TODO: Add below method when a query is added with initial get-diff submission
# @app.post("/get-diff-call-model/")
# def get_diff(diffQueryRequest: DiffQueryGetDiffRequest):
#     return DiffQueryExecutor.get_diff(diffQueryRequest)
