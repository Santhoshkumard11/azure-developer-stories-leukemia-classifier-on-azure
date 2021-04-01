import logging
import mimetypes
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Static page serving..')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    
    # your funcation name
    path = 'StaticPage'
    
    filename = f"{path}/{name}"
    if name:
        
        # open the file and load the html file
        with open(filename, 'rb') as f:
            mimetype = mimetypes.guess_type(filename)
            return func.HttpResponse(f.read(), mimetype=mimetype[0],status_code=200)    
    else:
        return func.HttpResponse(
             "Enter a valid file name",
             status_code=400
        )