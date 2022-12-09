class Error(Exception):
    def __init__(self, message):
        self.response = {"data": message}


class WrongJsonFormat(Error):
    def __init__(self, message="Wrong JSON format"):
        super().__init__(message)


class WrongFactFormat(Error):
    def __init__(self, message="Wrong fact format"):
        super().__init__(message)


class WrongPrologFormat(Error):
    def __init__(self, message="Wrong PROLOG format"):
        super().__init__(message)


class WrongConditionFormat(Error):
    def __init__(self, message="Wrong format of condition"):
        super().__init__(message)


class ExecutionError(Error):
    def __init__(self, message="Error while executing code"):
        super().__init__(message)


class SingleArgument(Error):
    def __init__(self, message="One operation argument is expected"):
        super().__init__(message)


class WrongOption(Error):
    def __init__(self, message="Wrong option!"):
        super().__init__(message)
