from src.models.category import CategoryModel
from src.utils.repository import SQLAlchemyRepository


class CategoryRepository(SQLAlchemyRepository):
    model = CategoryModel
