from socket_project.views.auth import Auth
from socket_project.views.user import User
from socket_project.views.friend import Friend
URL = {
"users/login" : Auth.as_view(),
"users/signup" : Auth.as_view(),
"users/(?P<id>[0-9]+)" : User.as_view(),

"friend" : Friend.as_view(),
"friend/add" : Friend.as_view(),
"friend/accept" : Friend.as_view(),
}
