class UnexpectedPriority(TypeError):
    def __init__(self):
        TypeError.__init__(self, "Priorities are disabled yet both a priority and value were supplied")


class DuplicatesEnabled(Exception):
    def __init__(self):
        Exception.__init__(self, "Duplicates are enabled so value tracking is disabled")


class BadData(Exception):
    def __init__(self):
        Exception.__init__(self, "Elements must be in format: (priority, value)")


class DuplicateInputs(Exception):
    def __init__(self):
        Exception.__init__(self, "Duplicates disabled yet duplicate elements exist in input data")
