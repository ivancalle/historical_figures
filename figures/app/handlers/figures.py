from ... import logging
from fastapi import APIRouter, Request, HTTPException, Response
from typing import List
from bson import ObjectId
from pymongo import ReturnDocument

from ..schemas import figures
from .. import schemas
from .. import doc_responses
router = APIRouter()


logger = logging.getLogger(__name__)


@router.post("", response_model=figures.FigureResponse, status_code=201)
async def create_figure(figure: figures.Figure, request: Request):

    logger.debug(
        'Creating figure',
        extra={"id": request.state.id})

    result = await request.app.state.db.figures.insert_one(figure.to_mongo())

    logger.debug(
        'Figure created',
        extra={"id": request.state.id})

    return figures.FigureResponse(id=str(result.inserted_id), **figure.dict())


@router.get("", response_model=List[figures.FigureResponse])
async def list_figures(request: Request):
    cursor = request.app.state.db.figures.find()
    return [figures.FigureResponse.from_mongo(f) async for f in cursor]


@router.get("/{figure_id}", response_model=figures.FigureResponse,
            responses={404: doc_responses.HTTP404})
async def get_figure(figure_id: schemas.IdType, request: Request):
    doc = await request.app.state.db.figures.find_one(
        {"_id": ObjectId(figure_id)}
    )

    if doc is None:
        raise HTTPException(404)

    return figures.FigureResponse.from_mongo(doc)


@router.patch("/{figure_id}", response_model=figures.FigureResponse,
              responses={404: doc_responses.HTTP404})
async def update_figure(figure_id: schemas.IdType,
                        figure: figures.FigureUpdate, request: Request):

    logger.debug(
        'Updating figure',
        extra={"id": request.state.id})

    doc = await request.app.state.db.figures.find_one_and_update(
        {"_id": ObjectId(figure_id)},
        {"$set": {k: v for k, v in figure.to_mongo().items() if v is not None}},  # noqa E501
        return_document=ReturnDocument.AFTER
    )

    logger.debug(
        'Figure updated',
        extra={"id": request.state.id})

    if doc is None:
        raise HTTPException(404)

    return figures.FigureResponse.from_mongo(doc)


@router.delete("/{figure_id}", status_code=204,
               responses={404: doc_responses.HTTP404})
async def delete_figure(figure_id: schemas.IdType, request: Request):
    logger.debug(
        'Deleting figure',
        extra={"id": request.state.id})

    result = await request.app.state.db.figures.delete_one(
        {"_id": ObjectId(figure_id)}
    )

    logger.debug(
        'Figure deleted',
        extra={"id": request.state.id})

    if result.deleted_count == 0:
        raise HTTPException(404)

    return Response(status_code=204)
