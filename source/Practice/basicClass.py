class Microwave:
    def __init__(self, pType: str, rating: int) -> None:
        self.pType = pType
        self.rating = rating
        self.isOn = False


sems = Microwave("sems", 1)

print(sems)
print(sems.pType)
print(sems.rating)
print(sems.isOn)





