from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas

router = APIRouter()


@router.post("/add_friend/")
def add_friend(friend_pair: schemas.FriendsByTelegramID):
    return crud.create_friend_pair(friend_pair)


@router.post("/delete_friend/")
def delete_friend_friend(friend_pair: schemas.FriendsByTelegramID):
    return crud.delete_friend_pair(friend_pair)


@router.post("/get_friends_status/", response_model=schemas.PeersDict)
def get_friends_status(tg_id: schemas.TelegramID):
    return crud.get_friends_status(tg_id)


# @router.post("/get_peer_status/")
# def get_peer_status():
#     pass


@router.post("/update_peers/")
def update_peers(peers: schemas.PeersDict):
    return crud.update_peers(peers)
