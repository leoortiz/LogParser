def print_obj(obj):
    attrs = vars(obj)
    print ', '.join("%s: %s" % item for item in attrs.items())