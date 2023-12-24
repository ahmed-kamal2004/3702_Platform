create database platform;
use platform;
create table Admin(
username varchar(200) not null,
email varchar(200) not null,
password varchar(200) not null,
DOB date ,
phonenumber varchar(200) ,
primary key (username),
unique (email) 
);
create table user(
username varchar(200) not null,
email varchar(200) not null,
password varchar(200) not null,
is_active bool ,
photo varchar(200),
DOB date,
nickname varchar(200),
phonenumber varchar(200),
primary key(username),
unique (email)
);
create table Publisher(
username varchar(200),
Linked_URL varchar(200),
Job varchar(200),
primary key (username),
foreign key (username) references user(username)
on delete cascade
on update cascade 
);
create table Student(
username varchar(200) not null,
primary key (username),
foreign key (username) references user(username)
on delete cascade
on update cascade 
);
create table channel(
id integer not null,
type varchar(200),
is_active bool,
description varchar(1000),
creationDate date,
Rating float,
title varchar(200),
code varchar(200),
primary key (id) 
);
create table channel_keywords(
channel_id integer not null,
keyword varchar(200) not null,
primary key (channel_id,keyword),
foreign key (channel_id) references channel(id)
on delete cascade
on update cascade
);
create table Discussion(
channel_id integer not null,
Discussion_id integer not null,
text varchar(10000),
publish_date date,
primary key (channel_id,Discussion_id),
foreign key (channel_id) references channel(id)
on delete cascade
on update cascade
);
create table content(
id integer not null,
text varchar(10000),
title varchar(200),
publishdate date,
channel_id integer not null,
publisherUsername varchar(200) not null,
primary key (id),
foreign key (channel_id) references channel (id)
on delete cascade
on update cascade,
foreign key (publisherUsername) references Publisher (username)
on delete cascade
on update cascade 
);
create table Notification(
id integer not null,
date date,
text varchar(10000),
related_content_id integer not null,
primary key (id),
foreign key (related_content_id) references content (id)
on delete cascade
on update cascade
);
create table question(
id integer not null,
text varchar(10000),
answer varchar(200),
channel_id integer,
primary key (id),
foreign key (channel_id) references channel (id)
on delete cascade
on update cascade
);
create table ProblemSet(
content_id integer not null,
deadline datetime,
primary key (content_id),
foreign key (content_id) references content(id)
on delete cascade
on update cascade
);
create table question_choices(
question_id integer not null,
choice varchar(200),
primary key (question_id,choice),
foreign key (question_id) references question(id)
on delete cascade
on update cascade
);
create table homework(
content_id integer not null,
primary key (content_id),
foreign key (content_id) references content (id)
on delete cascade
on update cascade
);
create table poll(
content_id integer not null,
primary key (content_id),
foreign key (content_id) references content(id)
on delete cascade
on update cascade
);
create table article (
content_id integer not null,
video varchar(1000),
photo varchar(1000),
primary key (content_id),
foreign key (content_id) references content(id)
on delete cascade
on update cascade
);
create table quiz (
content_id integer not null,
duration BIGINT,
starting_date datetime,
primary key (content_id),
foreign key (content_id) references content(id)
on delete cascade
on update cascade
);
create table poll_choices(
poll_id integer not null,
choice varchar(200) not null,
primary key(poll_id,choice),
foreign key(poll_id) references poll(content_id)
on delete cascade
on update cascade
);
create table admin_ban_user(
AdminUsername varchar(200) not null,
Username varchar(200) not null,
primary key (AdminUsername,Username),
foreign key (AdminUsername) references Admin(username)
on update cascade,
foreign key (Username) references user(username)
on delete cascade
on update cascade
);
create table admin_ban_channel(
AdminUsername varchar(200) not null,
channel_id integer not null,
primary key (AdminUsername,channel_id),
foreign key (AdminUsername) references Admin(username)
on update cascade,
foreign key (channel_id) references channel(id)
on delete cascade
on update cascade
);
create table publisher_manage_channel(
publisher_username varchar(200) not null,
channel_id integer not null,
primary key (publisher_username,channel_id),
foreign key (publisher_username) references Publisher (username)
on delete cascade
on update cascade,
foreign key (channel_id) references channel (id)
on delete cascade
on update cascade 
);
create table Discussion_about_article(
Discussion_id integer not null,
channel_id integer not null,
Article_id integer not null,
primary key (Discussion_id,channel_id,Article_id),
foreign key (channel_id,Discussion_id) references Discussion (channel_id,Discussion_id)
on delete cascade
on update cascade,
 foreign key (Article_id) references article (content_id)
on delete cascade
on update cascade
);
create table join_channel(
studentUsername varchar(200) not null,
channel_id integer not null,
requestStatus bool ,
primary key (studentUsername,channel_id),
foreign key (studentUsername) references Student (username)
on delete cascade
on update cascade,
foreign key (channel_id) references channel (id)
on delete cascade
on update cascade
);
create table get_notification(
studentUsername varchar(200) not null,
notification_id integer not null,
seen bool,
primary key (studentUsername,notification_id),
foreign key (studentUsername) references Student(username)
on delete cascade
on update cascade,
foreign key (notification_id) references Notification(id)
on delete cascade
on update cascade
);
create table solve_HW(
studentUsername varchar(200) not null,
HW_id integer not null,
primary key(studentUsername,HW_id),
foreign key (studentUsername) references Student(username)
on delete cascade
on update cascade,
foreign key (HW_id) references homework(content_id)
on delete cascade
on update cascade
);
create table solve_problem_set(
studentUsername varchar(200) not null,
content_id integer not null,
grade integer ,
primary key(studentUsername,content_id),
foreign key (studentUsername) references Student(username)
on delete cascade
on update cascade,
foreign key (content_id) references ProblemSet(content_id)
on delete cascade
on update cascade
);
create table solve_quiz(
studentUsername varchar(200) not null,
content_id integer not null,
grade integer ,
primary key(studentUsername,content_id),
foreign key (studentUsername) references Student(username)
on delete cascade
on update cascade,
foreign key (content_id) references quiz(content_id)
on delete cascade
on update cascade
);
create table Read_article(
studentUsername varchar(200) not null,
Article_id integer not null,
primary key(studentUsername,Article_id),
foreign key (studentUsername) references Student(username)
on delete cascade
on update cascade,
foreign key (Article_id) references article(content_id)
on delete cascade
on update cascade 
);
create table vote(
studentUsername varchar(200) not null,
poll_id integer not null,
chosen varchar(200),
primary key(studentUsername,poll_id),
foreign key (studentUsername) references Student(username)
on delete cascade
on update cascade,
foreign key (poll_id) references poll_choices(poll_id)
on delete cascade
on update cascade
);
create table HW_question(
question_id integer not null,
HW_id integer not null,
primary key(question_id,HW_id),
foreign key (question_id) references question(id)
on delete cascade
on update cascade,
foreign key (HW_id) references homework(content_id)
on delete cascade
on update cascade
);
create table PS_question(
question_id integer not null,
PS_id integer not null,
primary key(question_id,PS_id),
foreign key (question_id) references question(id)
on delete cascade
on update cascade,
foreign key (PS_id) references ProblemSet(content_id)
on delete cascade
on update cascade
);
create table quiz_question(
question_id integer not null,
quiz_id integer not null,
primary key(question_id,quiz_id),
foreign key (question_id) references question(id)
on delete cascade
on update cascade,
foreign key (quiz_id) references quiz(content_id)
on delete cascade
on update cascade
);
