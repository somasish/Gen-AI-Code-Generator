from app.main.com.company.controller.AppRouteController import app

@app.route('/')
def run_server():
    app.run(host='127.0.0.1',port=8080)