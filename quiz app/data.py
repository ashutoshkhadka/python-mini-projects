import requests

PARAM = {
    "amount": "10",
    "difficulty": "medium",
    "type": "boolean"
}

res = requests.get("https://opentdb.com/api.php", params=PARAM)
question_data = res.json()['results']
