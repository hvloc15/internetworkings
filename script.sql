create database socket_db;

use socket_db;
#drop table user;

CREATE TABLE user(
id integer auto_increment,
username varchar(256) UNIQUE,
password varchar(256),
dateofbirth bigint,
avatar varchar(1024),
isonline tinyint(1) default 0,
primary key(id)
) ENGINE= INNODB, auto_increment=1, CHARACTER SET utf8mb4;
select * from user;
update user set isonline=0 where username like "vinhloc1"
drop table friendship;

CREATE TABLE friendship(
userid integer not null,
friendid integer not null,
status varchar(8) not null,
primary key(userid, friendid)
)ENGINE= INNODB, auto_increment=1, CHARACTER SET utf8mb4;

INSERT INTO friendship (userid, friendid, status)
VALUES (1,2,'active');

INSERT INTO friendship (userid, friendid, status)
VALUES (2,1, 'active');

INSERT INTO friendship (userid, friendid, status)
VALUES (1,3, 'active');

INSERT INTO friendship (userid, friendid, status)
VALUES (3,1, 'active');

INSERT INTO friendship (userid, friendid, status)
VALUES (1,4, 'request');

INSERT INTO friendship (userid, friendid, status)
VALUES (4,1, 'accept');

select * from friendship;

delete from friendship where (friendid = 1 and userid=4) or (friendid = 4 and userid=1) 
delete from friendship where friendid = 5 or userid=5

delete from message where senderid = receiverid

drop table blog;
CREATE TABLE blog (
id integer not null auto_increment,
userid integer not null,
content varchar(2048) default '',
date bigint,
primary key(id),
index blog_userid_idx (userid)
)ENGINE= INNODB, auto_increment=1, CHARACTER SET utf8mb4;

select * from blog
insert into blog(userid, content, date)
values (1, "Tinh nhu giac mong tan 1", 123456789);
insert into blog(userid, content, date)
values (2, "Tinh nhu giac mong tan 2", 123456790);
insert into blog(userid, content, date)
values (2, "Tinh nhu giac mong tan 3", 123456792);
insert into blog(userid, content, date)
values (5, "Tinh nhu giac mong tan 4", 123456795);
insert into blog(userid, content, date)
values (5, "Tinh nhu giac mong tan 5", 123456795);

drop table message;
select * from message;
delete from message where content like " %"
CREATE TABLE message(
id integer not null auto_increment,
senderid integer not null,
receiverid integer not null,
content varchar(2048) default '',
date bigint default 0,
primary key(id),
index senderid_idx (senderid, date),
index receiverid_idx (receiverid, date)
)ENGINE= INNODB, auto_increment=1, CHARACTER SET utf8mb4;


INSERT INTO message (senderid, receiverid, content, date)
VALUES (1,2,'Thang cho Thien', 10230123);

INSERT INTO message (senderid, receiverid, content, date)
VALUES (2,1,'Loc dep Trai', 10230124);

INSERT INTO message (senderid, receiverid, content, date)
VALUES (2,1,'Thien Da lat', 10230125);

INSERT INTO message (senderid, receiverid, content, date)
VALUES (1,2,'Loc Ben Tre', 10230126);

SELECT * from message;

SELECT * from message 
WHERE senderid =1 or receiverid = 1
ORDER BY date DESC
LIMIT 2

SELECT senderid, receiverid, content, date from message 
             WHERE (senderid =1 and receiverid= 2) or (senderid =2 and receiverid = 1)
             ORDER BY date DESC
             LIMIT 0,100


select * from message;
update user set isonline=0 where id=1;
INSERT INTO user (username, password, dateofbirth)
VALUES ("vinhloc", "123456789", 1000013231);
INSERT INTO user (username, password, dateofbirth)
VALUES ("vinhloc1", "123456789", 1000013231);

INSERT INTO user (username, password, dateofbirth)
VALUES ("vinhloc3", "123456789", 1000013231);



INSERT INTO friendship (userid, friendid)
VALUES (1,15);

INSERT INTO friendship (userid, friendid)
VALUES (15,1);


SELECT user.username, user.dateofbirth, user.avatar
FROM friendship join user on (friendship.friendid = user.id)
WHERE friendship.userid = 1

UPDATE friendship
SET status='inactive'
WHERE userid = 4 and friendid=1;


UPDATE friendship
SET status='inactive'
WHERE userid = 4 and friendid=1;

SELECT * FROM user where not exists(select * from friendship where userid=1 and friendid= user.id )

SELECT user.username, user.avatar FROM user 
             WHERE user.id != 1 AND NOT EXISTS(SELECT * FROM friendship WHERE userid= 1 AND friendid= user.id)
       