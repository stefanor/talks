from yoconfigurator.dicts import merge_dicts


def update(config):
    add = {
        'graphite': {
            'htpasswd': {
                'users': {
                    'yola': 'super secret password',
                },
            },
        },
    }

    return merge_dicts(config, add)
