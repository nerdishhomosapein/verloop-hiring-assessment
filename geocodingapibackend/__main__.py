from flasgger.utils import swag_from
from flask import Response, jsonify, request

from geocodingapibackend import create_app

from .geoCodedResponse import getGeoCodedRequest

app = create_app()


@app.route("/", methods=["GET"])
def home_page():
    return "<h1>Verloop Hiring Assessment by Kumar Prateek<h1>"


@app.route("/getAddressDetails", methods=["POST"])
@swag_from("api_doc.yml")
def getAddressDetails():

    data = request.json
    address = data.get("address", "")
    output_format = data.get("output_format", None)

    response = getGeoCodedRequest(address)
    print(f"{response=}")

    if output_format == "xml":
        from dicttoxml import dicttoxml

        data = dicttoxml(response)
        res = Response(data, mimetype="text/xml")
        res.status_code = 200
        return res

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
