def dump_json(proto, host, port):
    url = proto + '://' + host + ':' + str(port) + '/json0'
    return url