def dump_route(proto, host, port):
    url = proto + '://' + host + ':' + str(port) + '/json0'
    return url