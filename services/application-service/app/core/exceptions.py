from fastapi import HTTPException

class BadRequestException(HTTPException):
    def __init__(self, message):
        super().__init__(status_code=400, detail=message)


class NotFoundException(HTTPException):
    def __init__(self, message):
        super().__init__(status_code=404, detail=message)