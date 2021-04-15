def function(a, b, *args):
    print(a, b)
    print(args)


function(1, 2, 3, 4, 5)
# 1 2
# (3, 4, 5)


def function(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)


function(1, 2, 3, 4, 5, param = 42)
# 1 2
# (3, 4, 5)
# {param: 42}

def function(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

d = {"param_a": 43, "param": 44}
function(1, 2, *[3, 4, 5], **d)
# 1 2
# (3, 4, 5)
# {'param_a': 43, 'param': 44}