import re
from urls import URL
from exceptions import NotFoundError
def match_url_regex(string, regex):
    start_regex_index = regex.find(">") + 1
    return re.fullmatch(regex[start_regex_index:len(regex)-1],string) is not None


def match_url(url, pattern):
    url_groups = url.split("/")
    pattern_groups = pattern.split("/")

    params = {}

    if len(url_groups) != len(pattern_groups):
        return None

    for i in range(len(url_groups)):
        if pattern_groups[i][0] == '(':
            if not match_url_regex(url_groups[i], pattern_groups[i]):
                return None
            param = re.search("<[a-zA-Z]+>", pattern_groups[i]).group()
            params[param[1:len(param)-1]] = url_groups[i]
        elif url_groups[i] != pattern_groups[i]:
            return None

    return params


def get_view(url):
    for url_pattern in URL.keys():
        if match_url(url, url_pattern) is not None:
            return URL[url_pattern]

    raise NotFoundError

