from cobbler import Cobbler


class CobblerSystemsData(object):

    def __init__(self):
        cobbler = Cobbler()
        self.data = cobbler.get_all_systems()

    def get_all_systems_data(self):
        return self.data
