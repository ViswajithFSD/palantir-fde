def compute_status(delay_days: int) -> str:
    if delay_days <= 0:
        return "on_time"
    elif delay_days <= 2:
        return "minor_delay"
    else:
        return "major_delay"


class Shipment:
    def __init__(self, shipment_id: str, carrier: str, delay_days: int):
        self.shipment_id = shipment_id
        self.carrier = carrier
        self.delay_days = delay_days

    def status(self) -> str:
        return compute_status(self.delay_days)


s1 = Shipment("SHP-10234", "DHL", 2)
print(s1.status())  # -> "minor_delay"