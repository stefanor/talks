from yoconfigurator.dicts import merge_dicts


def update(config):
    s_domain = config.common.domain.services
    add = {
        'common': {
            'graphite_carbon': {
                'host': 'graphite.%s' % s_domain,
                'text_port': 2003,
                'pickle_port': 2004,
            },
        },
    }
    return merge_dicts(config, add)
