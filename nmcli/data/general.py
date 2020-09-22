from dataclasses import dataclass
from .._const import NetworkConnectivity

@dataclass(frozen=True)
class General:
    state: str
    connectivity: NetworkConnectivity
    wifi_hw: bool
    wifi: bool
    wwan_hw: bool
    wwan: bool

    def to_json(self):
        return {
            'state': self.state,
            'connectivity': self.connectivity.value,
            'wifi_hw': self.wifi_hw,
            'wifi': self.wifi,
            'wwan_hw': self.wwan_hw,
            'wwan': self.wwan
        }
