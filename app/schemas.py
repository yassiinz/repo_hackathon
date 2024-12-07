from .extentions import ma
from .models import Cementeries


class CementeriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cementeries
        load_instance = True
