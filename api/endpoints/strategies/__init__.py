from fastapi import APIRouter
from .technical import router as technical_router
from .marketing import router as marketing_router
from .financial import router as financial_router
from .legal import router as legal_router
from .hr import router as hr_router
from .sales import router as sales_router
from .market import router as market_router

router = APIRouter(prefix="/strategies")

router.include_router(technical_router)
router.include_router(marketing_router)
router.include_router(financial_router)
router.include_router(legal_router)
router.include_router(hr_router)
router.include_router(sales_router)
router.include_router(market_router)