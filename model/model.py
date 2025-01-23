class Result:
    def __init__(self, success, data=None, error=None):
        self.success = success
        self.data = data
        self.error = error

    def is_success(self):
        return self.success

    def get_data(self):
        if self.is_success():
            return self.data
        raise ValueError("Cannot retrieve data from a failed result.")

    def get_error(self):
        if not self.is_success():
            return self.error
        raise ValueError("Cannot retrieve error from a successful result.")
