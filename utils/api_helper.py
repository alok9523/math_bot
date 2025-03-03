import requests

def make_api_request(url, params=None, headers=None, method="GET"):
    try:
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        else:
            response = requests.post(url, json=params, headers=headers)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}