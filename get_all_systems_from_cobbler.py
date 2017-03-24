from modules.cobbler import Cobbler

if __name__ == "__main__":

    def main():
        cobbler = Cobbler()
        data = cobbler.get_all_systems()
        return data
