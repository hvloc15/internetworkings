# for m in re.finditer(r"\(\?P<[a-z]+>", "loc/api/(?P<id>[1-9]+)/kaka/(?P<id>[1-9]*)"):
#     print(m.start())
# try:
#     try:
#         a = 5/ 0
#     except Exception as e:
#         raise AuthenticationFailed("concard")
# except AuthenticationFailed as e:
#     print(str(e))

# print(re.fullmatch("[1-9]+","19a"))
# print("loc>fdas".find(">"))
# a= "loc>fadsf"
# print(a[4:len(a)])
# a = "loc/api/(?P<id>[1-9]+)/kaka/(?P<id>[1-9]*)"
# print(a.split("/"))
# print(re.search("<[a-zA-Z]+>",a).start())
# a = re.sub(r"\(\?P<[a-z]+>([1-9a-zA-Z\[\]]+)","a",a)
# print(a)
#
temp = {
    "loc":2
}
dict = {
    **temp,
    "b":1,
    "c":2,
    "a":30
}
print(dict)
def test(a=3,**kwargs):
    print(a,kwargs.get("b"))

test(**dict)
a = "user"
b = [1,2,3]
a,b,c = b
print(b)
# def match_url_regex(string, regex):
#     start_regex_index = regex.find(">") + 1
#     return re.fullmatch(regex[start_regex_index:len(regex)-1],string) is not None
#
#
# def match_url(url, pattern):
#     url_groups = url.split("/")
#     pattern_groups = pattern.split("/")
#
#     params = {}
#
#     if len(url_groups) != len(pattern_groups):
#         return None
#
#     for i in range(len(url_groups)):
#         if pattern_groups[i][0] == '(':
#             if not match_url_regex(url_groups[i], pattern_groups[i]):
#                 return None
#             param = re.search("<[a-zA-Z]+>", pattern_groups[i]).group()
#             params[param[1:len(param)-1]] = url_groups[i]
#         elif url_groups[i] != pattern_groups[i]:
#             return None
#
#     return params
#
# print(match_url("api/loc/123/haha/2312","api/loc/(?P<id>[0-9]+)/haha/(?P<bd>[0-9]+)"))