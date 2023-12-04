import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)
_logger = logging.getLogger(__name__)


