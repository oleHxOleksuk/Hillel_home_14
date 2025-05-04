class TooManyStudentsError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        super().__init__(message)
