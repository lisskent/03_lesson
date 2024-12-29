from address import Address


class Mailing:
    def __init__(self, to_ad: Address, from_ad: Address, cost: float, track):
        self.to_ad = to_ad
        self.from_ad = from_ad
        self.cost = cost
        self.track = track
