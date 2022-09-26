class SchemaValidator:
    """
    SchemaValidator class validates the request body passed by the user.
    """

    def __init__(self, response) -> None:
        self.response = response

    def isCorrect(self):
        errorMessages = []
        outputFormat = ["xml", "json", "JSON", "XML"]
        invalidArgumentType = False

        try:
            address = self.response.get("address", None)
            if address is None or len(address) <= 1:
                raise Exception("Error")
        except Exception as e:  # noqa: F841
            errorMessages.append("Field address is mandatory.")

        try:
            output_format = self.response.get("output_format", None)
            if output_format is None:
                raise Exception("Error")
            elif output_format not in outputFormat:
                invalidArgumentType = True
                raise Exception("Not a valid argument format")

        except Exception as e:  # noqa: F841
            if invalidArgumentType:
                errorMessages.append("Output format can be only xml or json")
            else:
                errorMessages.append("Output format is a mandatory field")

        return errorMessages
