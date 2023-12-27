from src.models import CategoryModel
from src.utils.repository import SQLAlchemyRepository


class CategoryRepository(SQLAlchemyRepository):
    model = CategoryModel
