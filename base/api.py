from ninja import NinjaAPI
from access.api import router as access_router

api = NinjaAPI()

api.add_router("/access/", access_router, tags=["Access"])
