
class Api:
    def __init__(self, **kwargs):
        self.return_string = kwargs.get('args').get('v') or 'Dog'
        pass


    def run(self):
        return self.return_string
