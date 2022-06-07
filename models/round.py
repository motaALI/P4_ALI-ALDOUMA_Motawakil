class Round:

    def __init__(
        self,
        round_name: str,
        start_datetime: str,
        end_datetim: str
    ):
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetim = end_datetim
        self.matches = []
        