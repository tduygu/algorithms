try:
    raise Exception
except Exception as e:
    print(type(e.args))