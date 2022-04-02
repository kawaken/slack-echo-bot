import functions_framework
import json


@functions_framework.http
def verify(request):
    headers = {"Content-Type": "application/json"}
    body = request.get_json()
    if body.get("type") == "url_verification":
        res = json.dumps({"challenge": body["challenge"]})
        return (res, 200, headers)

    return ("{}", 400, headers)
