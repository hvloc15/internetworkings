from socket_project.views.auth import Auth
from socket_project.views.user import User
from socket_project.views.friend import Friend
from socket_project.views.blog import Blog
from socket_project.views.chat import Chat
from socket_project.views.connection import Connection


URL = {
"connect": Connection.as_view(),

"users/login" : Auth.as_view(),
"users/signup" : Auth.as_view(),
"users/(?P<id>[0-9]+)" : User.as_view(),

"friend" : Friend.as_view(),
"friend/add" : Friend.as_view(),
"friend/accept" : Friend.as_view(),
"friend/cancle" : Friend.as_view(),

"blog/create": Blog.as_view(),

"chat/(?P<friendid>[0-9]+)" : Chat.as_view(),
"chat/istyping" : Chat.as_view(),
"chat/send" : Chat.as_view(),
}
