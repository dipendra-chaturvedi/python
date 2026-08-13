from flask import Flask, request

app = Flask(__name__)


@app.route("/header-test", methods=["GET"])
def header_test():

    # Predefined Header
    # user_agent = request.headers.get("User-Agent")

    # return {
    #     "user_agent": user_agent
    # }, 200


    # Custom Header
    developer_name = request.headers.get("X-Developer-Name")

    return {
        "developer_name": developer_name
    }, 200

# Authorization Header
@app.route("/secure", methods=["GET"])
def secure():

    token = request.headers.get("Authorization")
    if token != "secret123":
        return {
            "message": "Unauthorized"
        }, 401
    
    return {
        "message": "Access granted"
    }, 200

   


if __name__ == "__main__":
    app.run(debug=True)