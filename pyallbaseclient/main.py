from sgqlc.operation import Operation
from allbase_schema import Query
from sgqlc.endpoint.http import HTTPEndpoint


url = "http://localhost:8080/query"
headers = {"Authorization": "bearer TOKEN"}
endpoint = HTTPEndpoint(url, headers)


op = Operation(Query)

compounds = op.compounds()

data = endpoint(op)

print(data)
