from flask import Flask, request, abort
import importlib.util

app = Flask(__name__)


@app.route('/<path:path>')
def arbitrary_api(path):
    module_name = path.split('/')[-1]
    try:
        spec = importlib.util.spec_from_file_location(module_name, f"./modules/{path}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except FileNotFoundError:
        abort(404, f"Module {module_name} not found at ./modules/{path}.py")
        return

    api = module.Api(args=request.args, form_body=request.form, json_body=request.json)
    return api.run()


if __name__ == '__main__':
    app.run()
