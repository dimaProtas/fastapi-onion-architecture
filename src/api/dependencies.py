from typing import Annotated
from fastapi import Depends
from utils.unitofwork import UnitOfWork, IUnitOfWork


UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
