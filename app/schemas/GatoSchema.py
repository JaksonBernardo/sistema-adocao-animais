from app.schemas.AnimalSchema import AnimalBase, AnimalResponse

class GatoCreate(AnimalBase):
    necessidade_passeio: bool
    independencia: bool


class GatoResponse(AnimalResponse):
    necessidade_passeio: bool
    independencia: bool
