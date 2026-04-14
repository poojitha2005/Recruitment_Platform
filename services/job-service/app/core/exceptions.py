from fastapi import HTTPException


# Base Exception
class AppException(HTTPException):
    def __init__(self, code: str, message: str, status_code: int = 400):
        super().__init__(
            status_code=status_code,
            detail={
                "code": code,
                "message": message,
                "details": {}
            }
        )


#  Authentication Errors
class UnauthorizedException(AppException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(
            code="UNAUTHORIZED",
            message=message,
            status_code=401
        )


#  Permission Errors
class ForbiddenException(AppException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(
            code="FORBIDDEN",
            message=message,
            status_code=403
        )


#  Not Found
class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(
            code="NOT_FOUND",
            message=message,
            status_code=404
        )


#  Bad Request
class BadRequestException(AppException):
    def __init__(self, message: str = "Bad request"):
        super().__init__(
            code="BAD_REQUEST",
            message=message,
            status_code=400
        )