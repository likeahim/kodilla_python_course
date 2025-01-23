def build_bridge(chunk,goal):
    connector = chunk / 2
    if chunk <= 0:
        return False
    elif goal <= 0:
        return False
    else:
        result = (goal + connector) / (chunk + connector)
        return result.is_integer()

print(build_bridge(2,2))