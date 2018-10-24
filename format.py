import re

# compiled = re.compile(
#     r'^(?:http|ftp)s?://' # http:// or https://
#     r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
#     r'localhost|' # localhost...
#     r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
#     r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
#     r'(?::\d+)?' # optional port
#     r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def html_format(content):
    # text = content.replace("\n", "<br/>")
    lines = content.split("\n")

    new_lines = []
    for line in lines:
        new_lines.append(format_line(line))

    if len(new_lines) > 0:
        new_lines[0] = "<h3>" + new_lines[0] + "</h3>"

    if len(new_lines) > 1:
        new_lines[0] += "<br/>"

    result = "<br/>".join(new_lines)
    print(result)
    return result

def format_line(line):
    parts = line.split(" ")

    new_parts = []
    for part in parts:
        new_parts.append(format_part(part))

    return " ".join(new_parts)

def format_part(part):
    # res = compiled.match(part)

    # if res is not None:
    #     return "<a href={0}>{0}</a>".format(part)

    if part.startswith("http://") or part.startswith("https://"):
        return "<a href=" + part + ">" + part + "</a>"

    return part
