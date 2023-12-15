import logging
from datetime import datetime
from uuid import uuid4

import requests
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from .. import entities, models
from ..database import get_db

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/systems", tags=["Systems"])


async def get_name_from_email(email: str):
    res = requests.get(f"https://jsonplaceholder.typicode.com/users?email={email}")
    for commander in res.json():
        if commander.get('email') == email:
            return commander.get('name')


@router.post("", response_model=models.System)
async def create_system(request: models.CreateSystem, db: AsyncSession = Depends(get_db)):
    system = entities.System()
    system.id = uuid4()
    system.name = request.name
    system.supreme_commander = request.supreme_commander
    system.supreme_commander_name = await get_name_from_email(request.supreme_commander)
    system.date_created = datetime.now()

    db.add(system)
    await db.commit()

    return system


@router.get("/population")
async def get_system_population(db: AsyncSession = Depends(get_db)):
    stmt = text(
        "select s.id as id, sum(p.population_millions) as population  from interview.systems s join interview.planets p on p.system_id = s.id group by s.id")
    res = await db.execute(stmt)
    result = {str(row.id): row.population for row in res.fetchall()}
    return result
