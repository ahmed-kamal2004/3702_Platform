from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from datetime import timedelta


################################################################
################################    Notification
################################################################


class NotificationModel(BaseModel):
    id: int
    date: datetime
    text: str
    related_content_id: int


################################################################
################################################################
#                    Content Part
################################################################
################################################################


class ContentModel(BaseModel):
    id: int
    text: str
    title: str
    publishdate: datetime
    channel_id: int
    publisherUsername: str


################################
class homeworkModel(ContentModel):
    pass


class ArticleModel(ContentModel):
    video: str
    photo: str


class QuizModel(ContentModel):
    duration: timedelta
    starting_date: datetime


class ProblemSetModel(ContentModel):
    deadline: datetime


class PollModel(ContentModel):
    pass


###############################
################################################################
################################################################
#               Channel Part
################################################################
################################################################


class ChannelModel(BaseModel):
    id: int
    type: str
    is_active: bool
    description: str
    creationDate: datetime
    Rating: float
    title: str
    code: str


class QuestionModel(BaseModel):
    id: int
    text: str
    answer: str
    channel_id: int


class QuestionChoicesModel(BaseModel):
    question_id: int
    choice: str


class DiscussionModel(BaseModel):
    channel_id: int
    Discussion_id: int
    text: int
    publish_date: datetime


################################################################
################################################################
#               User Part
################################################################
################################################################


class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool
    DOB: datetime
    nickname: str
    phonenumber: str

    class Config:
        from_attribute = True
        populate_by_name = True


class StudentModel(UserModel):
    pass


class PublisherModel(UserModel):
    job: str
    linkedin_url: str


################################################################
################################################################
#               Admin Part
################################################################
################################################################


class AdminModel(BaseModel):
    username: str
    password: str
    email: EmailStr
    DOB: datetime
    phonenumber: str


################################################################

################################################################


################################################################
#                     MultiVariables
class PollChoice_MultiModel(BaseModel):
    poll_id: int
    choice: str


class Keywords_MluitModel(BaseModel):
    channel_id: int
    keyword: str


################################################################
#                     RELATIONS
class QuizQuestionModel(BaseModel):
    question_id: int
    quiz_id: int


class VoteModel(BaseModel):
    studentusername: str
    poll_id: int
    choice: str


class HomeWorkQuestion_RelationModel(BaseModel):
    question_id: int
    Homework_id: int


class SolveQuiz_RelationModel(BaseModel):
    studentusername: str
    content_id: int
    grade: int


class SolveHomeWork_RelationModel(BaseModel):
    studentusername: str
    homework_id: int


class SolveProblemSet_RelationModel(BaseModel):
    studentusername: str
    content_id: int
    grade: int


class Read_RelationModel(BaseModel):
    studentusername: str
    article_id: int


class ProblemSetQuestion_RelationModel(BaseModel):
    question_id: int
    problemset_id: int


class AdminUserBan_RelationalModel(BaseModel):
    adminusername: str
    username: str


class AdminChannelBan_RelationModel(BaseModel):
    adminusername: str
    channel_id: int


class PublisherManageChannel_RelationModel(BaseModel):
    publisherusername: str
    chanell_id: int


class GetNotification_RelationalModel(BaseModel):
    studentusername: str
    notification_id: int
    seen: bool


class DiscussionArticle_RelationModel(BaseModel):
    Discussion_id: int
    article_id: int


class JoinChannel_RelationModel(BaseModel):
    studentusername: str
    channel_id: int
    requestStatus: bool


class TokenModel(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True
        populate_by_name = True


## publisher models


########
