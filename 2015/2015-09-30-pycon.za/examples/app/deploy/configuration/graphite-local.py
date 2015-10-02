import os

from yoconfigurator.dicts import merge_dicts


def update(config):
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '..', '..', 'data'))
    new = {
        'graphite': {
            'path': {
                'data': data_path,
                'log_dir': '%s/logs/' % data_path,
            },
            'db': {
                'name': os.path.join(data_path, 'graphite.sqlite'),
                'engine': 'django.db.backends.sqlite3',
            },
        },
    }
    return merge_dicts(config, new)
