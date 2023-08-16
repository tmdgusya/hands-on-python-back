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
    # recommendation metadata (user data or json data)
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
    context_name: str
    # user id
    user_id: str
    # recommendation list for user in context
    recommendation_list: List[Recommendation]
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


class ChoiceRecommendationRequest(BaseModel):
    """
    Choice recommendation request for action
    """
    # user id
    user_id: str
    # recommendation id
    recommendation_id: str


class RejectRecommendationRequest(BaseModel):
    """
    Reject recommendation request for action
    """
    # user id
    user_id: str
    # recommendation id
    recommendation_id: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/join")
async def join(request: UserJoinRequest) -> UserJoinResponse:
    """
    User join action
    """
    return UserJoinResponse(user_id=1)


@app.get("/context")
async def get_contexts() -> List[Context]:
    return [
        Context(
            context_id=1,
            context_name="search_food",
            user_id=1,
            recommendation_list=[],
            created_at="2021-01-01 00:00:00"
        )
    ]


@app.get("/context/{context_id}/recommendation")
async def get_all_recommendation_list_by(
        context_id: int,
        recommendation_type: str,
        recommendation_content: str,
        user_id: int,
) -> List[Recommendation]:
    """
    Get recommendation list by context_id, recommendation_type, or recommendation_content

    user_id is used to logging
    """
    # do something for recommendation
    return [
        Recommendation(
            recommendation_id=1,
            recommendation_type="food",
            recommendation_content="food",
            recommendation_metadata={},
        )
    ]


@app.post("/context/{context_id}/reject")
async def accept_recommendation(context_id: int, request: ChoiceRecommendationRequest) -> bool:
    """
    Reject recommendation

    - recommendation_id is recommendation_id was rejected
    - This information will be used to retrain our model
    """
    # do something for recommendation
    return True


@app.post("/context/{context_id}/choice")
async def reject_recommendation(context_id: int, request: RejectRecommendationRequest) -> bool:
    """
    Accept recommendation

    - recommendation_id is recommendation_id was accepted
    - This information will be used to retrain our model
    """
    # do something for recommendation
    return True
