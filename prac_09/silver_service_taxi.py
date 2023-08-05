from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel,)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()}, ${self.price_per_km:.2f}/km  plus flagfall of ${self.flagfall:.2f}"
