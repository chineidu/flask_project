class StatusCode:
    """HTTP response status codes indicate whether a specific HTTP request
    has been successfully completed.

    Responses are grouped in five classes:
    --------------------------------------
    Informational responses: (100–199)
    Successful responses: (200–299)
    Redirection messages: (300–399)
    Client error responses: (400–499)
    Server error responses: (500–599)
    """

    CONTINUE_100 = 100
    OK_200 = 200
    CREATED_201 = 201
    NO_CONTENT_204 = 204
    FOUND_302 = 302  # (URI of the requested resource has been changed temporarily)
    BAD_REQUEST_400 = 400
    UNAUTHORIZED_401 = 401  # (It actually means 'Unauthenticated')
    FORBIDDEN_403 = 403  # (Client’s identity is known but client has no access)
    NOT_FOUND_404 = 404
    INTERNAL_SERVER_ERROR_500 = 500


status_code = StatusCode()
