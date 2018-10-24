import re

def parse(detail):
    lines = detail.split("\n")
    data = {}
    # rest_lines =
    rest_lines = "<br/>".join([format_line(x) for x in lines[1:]])

    data['title'] = format_line(lines[0])
    data['content'] = rest_lines
    data['meta'] = 'meta'

    return data

def html_format(content):
    # text = content.replace("\n", "<br/>")
    lines = content.split("\n")

    new_lines = []
    for line in lines:
        new_lines.append(format_line(line))

    if len(new_lines) > 0:
        new_lines[0] = "<h3>" + new_lines[0] + "</h3>"

    # if len(new_lines) > 1:
    #     new_lines[0] += "<br/>"

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
        return "<a onclick=openInNewTab('%s')>%s</a>" % (part, part)
        # "<a onclick=openInNewTab()/>" + part + ">" + part + "</a>"

    return part
