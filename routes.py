from new_model_manager import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"