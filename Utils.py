import json


class JSONEncoder(json.JSONEncoder):
    def toJsonStr(self, obj):
        # convert object to a dict
        d = {}
        # d['__class__'] = obj.__class__.__name__
        # d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return json.dumps(d, sort_keys=True)
