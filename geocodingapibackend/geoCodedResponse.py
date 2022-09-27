import requests  # type: ignore

from .settings import API_KEY


def replaceSpacesWithAdittionSign(address):

    address = address.replace("#", "")
    address = address.strip()
    address = address.replace(" ", "+")
    return address


def getGeoCodedRequest(address):

    cleanedAddress = replaceSpacesWithAdittionSign(address)
    # print(f"{cleanedAddress=}")
    # print(f"{API_KEY=}")
    try:
        response = requests.get(
            f"https://maps.googleapis.com/maps/api/geocode/json?address={cleanedAddress}&key={API_KEY}"
        )

        responseJson = response.json()

        results = responseJson.get("results")

        result = results[0]

        geometry = result.get("geometry")
        # print(f"{geometry=}")

        location = geometry.get("location")
        # print(f"{location=}")

        geocodedAddress = {"coordinates": location, "address": address}
        # print(f"{geocodedAddress=}")

        return geocodedAddress

    except KeyError as e:  # noqa: F841
        pass
