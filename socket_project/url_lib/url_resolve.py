import re


def match_url_regex(string, regex):
    start_regex_index = regex.find(">") + 1
    return re.fullmatch(regex[start_regex_index:len(regex)-1],string) is not None


def resolve_query_string(request, query_string):
    if query_string is None:
        return
    groups = query_string.split("&")
    for group in groups:
        parts = group.split("=")
        if len(parts) != 2:
            continue
        request[parts[0]] = parts[1]


def match_url(request, pattern):
    url = request["URL"]
    url_groups = url.split("/")
    pattern_groups = pattern.split("/")

    params = {}

    if len(url_groups) != len(pattern_groups):
        return None

    query_string = None
    end_group = url_groups.pop()
    end_group = end_group.split("?")
    if len(end_group) > 2:
        return None
    elif len(end_group) == 2:
        query_string = end_group[1]

    url_groups.append(end_group[0])
    for i in range(len(url_groups)):
        if pattern_groups[i][0] == '(':
            if not match_url_regex(url_groups[i], pattern_groups[i]):
                return None
            param = re.search("<[a-zA-Z]+>", pattern_groups[i]).group()
            params[param[1:len(param)-1]] = url_groups[i]
        elif url_groups[i] != pattern_groups[i]:
            return None

    resolve_query_string(request, query_string)
    return params




