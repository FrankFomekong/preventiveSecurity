from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'Service Unavailable'

class BadGatewayAuthentification(APIException):
    status_code = 401
    default_detail = 'The request has been sent to a server where authentication has failed. Try again later, if the problem persists contact the manager.'
    default_code = 'Bad Gateway Authentification'

class BadGatewayRequest(APIException):
    status_code = 502
    default_detail = 'The request has been sent to a server which indicates that the request is bad, contact the manager.'
    default_code = 'Bad Gateway'

class BadGateway(APIException):   
    status_code = 502
    default_detail = 'The request was sent to a server that returned an unexpected response, contact the manager.'
    default_code = 'Bad Gateway'

class BadMapping(APIException):
    status_code = 421
    default_detail = 'The request was directed at a server that is not able to produce a response, try again later.'
    default_code = 'Bad mapping'
    
class ProtectedErrorAPIException(APIException):
    status_code = 423
    default_detail = 'You cannot delete this resource because it is linked to another resource.'
    default_code = 'Locked'
        
class IntegrityErrorAPIException(APIException):
    status_code = 424
    default_detail = 'One method of the transaction failed.'
    default_code = 'Method Failure'

class PreconditionRequiredAPIException(APIException):
    status_code = 428
    default_detail = 'Precondition Required.'
    default_code = 'Precondition Required'

class NotFoundAPIException(APIException):
    status_code = 404
    default_detail = 'Resource not found.'
    default_code = 'Not found'

class BadRequestAPIException(APIException):
    status_code = 400
    default_detail = 'The query syntax is incorrect.'
    default_code = 'Bad request'
