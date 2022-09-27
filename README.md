# Verloop hiring assignment

 Python based web api built using [Flask](https://github.com/pallets/flask). Poetry is used for dependency management. Pre-commit hook is used for linting, formatting and static type checking of the code. The api documentation is hosted using the Swagger UI.
 
 ## Project Setup
     git clone https://github.com/nerdishhomosapein/verloop-hiring-assessment.git
     poetry init
     poetry shell
     poetry run python -m geocodingApiBackend
     
     
### Query the Api using Curl.

##### Curl
    curl http://localhost:5000/getAddressDetails -H '{"Content-Type":"application/json"}' -d '{"address": "nehru museum, new delhi 110011", "output_format": "json"}'
    
    
### Accessing Api Documentation using the Swagger UI link.
    http://localhost:5000/apidocs/#/default/post_getAddressDetails
    
### TODOs
    - Adding Caching to the api response.
    - Contenarizing the app using docker.
    - Adding Auth to the API.
    - Deploying the app to AWS.
