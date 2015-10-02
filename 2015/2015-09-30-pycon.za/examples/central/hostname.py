from yoconfigurator.dicts import merge_dicts


def update(config):
    add = {
        'common': {
            'domain': {
                'services': 'example.net',
            },
        },
        'deploy': {
            'root': '/srv/'
        },
    }
    return merge_dicts(config, add)
