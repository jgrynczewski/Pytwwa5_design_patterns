class Director:
    def __init__(self, builder):
        self._builder = builder

    def build_computer(self):
        self._builder.new_computer()

        # fluent interface
        self._builder\
            .get_case()\
            .get_mainboard()\
            .install_hard_disk()

    def get_computer(self):
        return self._builder.get_computer()