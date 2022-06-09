from gendiff.formatter.stylish import to_str


def format_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"


# flake8: noqa: C901
def to_plain(source, level=''):
    result = ''
    for key, item in tuple(sorted(source.items())):
        flag = item[0]
        values = item[1:]
        value = values[0]
        if flag == 'nested':
            result += to_plain(value, level=level + key + '.')
        else:
            if flag != 'unchanged':
                result += f"Property '{level}{key}' was {flag}"
            if flag == 'added':
                if isinstance(value, dict):
                    result += " with value: [complex value]\n"
                else:
                    result += f" with value: {format_value(value)}\n"
            if flag == 'removed':
                result += '\n'
            if flag == 'updated':
                old, new = value[0], value[1]
                if isinstance(old, dict) and type(new) != dict:
                    result += f". From [complex value] to {format_value(new)}\n"
                elif isinstance(new, dict) and type(old) != dict:
                    result += f". From {format_value(old)} to [complex value]\n"
                elif isinstance(old, dict) and isinstance(new, dict):
                    result += ". From [complex value] to [complex value]\n"
                elif not isinstance(old, dict) and not isinstance(new, dict):
                    result += f". From {format_value(old)} to {format_value(new)}\n"
    return result