from flask import Flask
import importlib.util

app = Flask(__name__)


@app.route('/<path:path>')
def arbitrary_api(path):
    module_name = path.split('/')[-1]
    spec = importlib.util.spec_from_file_location(module_name, f"./modules/{path}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    api = module.Api()
    return api.run()


if __name__ == '__main__':
    app.run()
