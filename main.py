import uuid

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from pydantic import BaseModel
from typing import List

app = FastAPI()
engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/roach?charset=utf8mb4")
DBSession = sessionmaker(engine)
session = DBSession()

class Recommendation(BaseModel):
    # recommendation id
    recommendation_id: int
    # recommendation type
    recommendation_type: str
    # recommendation score
    recommendation_content: str
    # recommendation metadata
    recommendation_metadata: dict


class RecommendationList(BaseModel):
    # context id for recommendation type
    context_id: int
    # user id
    user_id: int
    # action id
    action_id: int
    # recommendation list for user in context
    recommendation_list: List[Recommendation]
    created_at: str


class Context(BaseModel):
    # context id for recommendation type
    context_id: int
    # action name
    action_name: str
    # user id
    user_id: str
    # created at
    created_at: str

class UserJoinRequest(BaseModel):
    """
    User join request for action
    """
    # action name
    email: str
    # user id
    password: str


class UserJoinResponse(BaseModel):
    """
    User join response
    """
    user_id: int

class CreateContextRequest(BaseModel):
    """
    Create context request for action
    """
    # action name
    action_id: str
    # user id
    user_id: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/join")
async def join(request: UserJoinRequest) -> UserJoinResponse:
    """
    User join action
    """
    return UserJoinResponse(user_id=1)

@app.get("/recommendation/context/search_action")
async def recommend(action_id: int, action_name: str, user_id: int) -> RecommendationList:
    """
    Get recommendation list by action_id or action_name
    action_name: search_food, search_bar, etc.
    action_id: 1, 2, 3, etc.
    """
    # do something for recommendation
    return RecommendationList(
        context_id=1,
        user_id=user_id,
        action_id=1,
        recommendation_list=[],
        created_at="2021-01-01 00:00:00"
    )


@app.get("/recommendation/context/{context_id}")
async def recommend(context_id: int, user_id: int) -> RecommendationList:
    """
    Get recommendation list for user in context
    """
    # do something for recommendation
    return RecommendationList(
        context_id=context_id,
        user_id=1,
        action_id=1,
        recommendation_list=[],
        created_at="2021-01-01 00:00:00"
    )

@app.post("/recommendation/context")
async def create_context(request: CreateContextRequest) -> Context:
    """
    Create context for action
    action is a group of user actions like search_food or searches something by the search bar, etc.
    """
    # create context
    return Context(
        # random uuid for context id
        context_id=uuid.uuid4(),
        action_name=request.action_id,
        user_id=request.user_id,
        created_at="2021-01-01 00:00:00"
    )

@app.post("/recommendation/{recommendation_id}/reject")
async def rejectRecommendation(recommendation_id: int, user_id: int) -> bool:
    """
    Reject recommendation
    """
    # do something for recommendation
    return True


@app.post("/recommendation/{recommendation_id}/accept")
async def rejectRecommendation(recommendation_id: int, user_id: int) -> bool:
    """
    Accept recommendation
    """
    # do something for recommendation
    return True