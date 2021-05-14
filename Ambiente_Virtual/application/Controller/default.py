from application import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello World"

