
from yoconfigurator.dicts import merge_dicts


def update(config):
    add = {
        'common': {
            'wild_ssl_certs': {
                'services': {
                    'cert': '/etc/ssl/wildcard.example.net.pem',
                    'private': '/etc/ssl/wildcard.example.net.key',
                },
            },
        },
    }
    return merge_dicts(config, add)
