import hug


@hug.get('/echo')
def echo(msg):
    return f"echo: {msg}"
