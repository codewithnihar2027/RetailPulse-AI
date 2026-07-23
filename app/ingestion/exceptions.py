class DatasetValidationError(Exception):
    """Raised when dataset validation fails."""
    pass


class UnsupportedDatasetError(Exception):
    """Raised when the uploaded dataset is not supported."""
    pass


class SchemaMappingError(Exception):
    """Raised when schema mapping fails."""
    pass