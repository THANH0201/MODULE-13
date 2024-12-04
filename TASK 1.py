import json
from flask import Flask, Response

app = Flask(__name__)
@app.route('/prime_number/<int:number>')
def prime_number(number):
    try:
        number = int(number)
        if number == 1:
            result = "true"
        else:
            for i in range(2, int(number ** 0.5) + 1):
             if number % i == 0:
                result = "False"
             else:result = "True"
        response = {
            "number" : number,
            "isPrime" : result
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)