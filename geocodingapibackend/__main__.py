from flasgger.utils import swag_from
from flask import Response, jsonify, request

from geocodingapibackend import create_app

from .geoCodedResponse import getGeoCodedRequest
from .schemaValidation import SchemaValidator

app = create_app()


@app.route("/", methods=["GET"])
def home_page():
    return "<h1>Verloop Hiring Assessment by Kumar Prateek<h1>"


@app.route("/getAddressDetails", methods=["POST"])
@swag_from("api_doc.yml")
def getAddressDetails():

    data = request.json
    schema = SchemaValidator(response=data)
    errorMessages = schema.isCorrect()

    if len(errorMessages) > 0:
        _ = {"status": "error", "message": errorMessages}

        return jsonify(_), 400

    address = data.get("address")
    output_format = data.get("output_format")

    response = getGeoCodedRequest(address)

    if output_format.lower() == "xml":
        from dicttoxml import dicttoxml

        data = dicttoxml(response)
        res = Response(data, mimetype="text/xml")
        res.status_code = 200
        return res

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1")
