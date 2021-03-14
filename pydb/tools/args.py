class Args:
    @staticmethod
    def guard(key: str, parameters: dict, default=None):
        if key not in parameters.keys() and default is None:
            raise Exception(f"The field {key} is required.")
        return parameters[key] if key in list(parameters) else default
