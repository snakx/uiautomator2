def dump_route(proto, host, port=4726):
    url = proto + '://' + host + ':' + str(port) + '/'
    return url