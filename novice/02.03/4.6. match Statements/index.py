def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Somethings wrong with the internet" 
        case 401 | 403 | 404:  

print(http_error(404))

 