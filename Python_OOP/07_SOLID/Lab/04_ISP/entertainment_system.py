class HdmiConnectable:
    def connect_via_hdmi_cable(self, device):
        return f"{device} connected via HDMI cable"


class RcaConnectable:
    def connect_via_rca_cable(self, device):
        return f"{device} connected via RCA cable"


class EthernetConnectable:
    def connect_via_ethernet_cable(self, device):
        return f"{device} connected via ethernet cable"


class PowerConnectable:
    def connect_to_power_outlet(self, device):
        return f"{device} connected via power cable"


class EntertainmentDevice:
    pass


class Television(EntertainmentDevice, RcaConnectable, HdmiConnectable, PowerConnectable):
    def connect_to_dvd(self, dvd_player):
        self.connect_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)


class DvdPlayer(EntertainmentDevice, HdmiConnectable, PowerConnectable):
    def connect_to_tv(self, television):
        self.connect_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HdmiConnectable, EthernetConnectable, PowerConnectable):
    def connect_to_tv(self, television):
        self.connect_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetConnectable, PowerConnectable):
    def connect_to_tv(self, television):
        self.connect_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)


tv = Television()
print(tv.connect_via_hdmi_cable("dvd"))
