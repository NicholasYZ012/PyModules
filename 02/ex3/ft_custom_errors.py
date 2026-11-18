class GardenError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class PlantError(GardenError):
    pass