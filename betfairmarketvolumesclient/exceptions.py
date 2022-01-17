from typing import Optional


class BFError(Exception):
    """
    base exception class

    """

    pass


class APIError(BFError):
    """
    Exception raised if error is found.
    """

    def __init__(
            self,
            response: Optional[dict],
            uri: str = None,
            params: dict = None,
            exception: Exception = None,
    ):
        if response:
            error_data = response.get("error")
            message = (
                    "%s \nParams: %s \nException: %s \nError: %s \nFull Response: %s"
                    % (uri, params, exception, error_data, response)
            )
        else:
            message = "%s \nParams: %s \nException: %s" % (uri, params, exception)
        super(APIError, self).__init__(message)
