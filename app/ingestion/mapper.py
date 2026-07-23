from app.config.schema_config import CANONICAL_SCHEMA
from app.ingestion.exceptions import MissingRequiredColumnsError

class ColumnMapper:
    """
    Responsible for mapping uploaded column names
    to the RetailPulse canonical schema.
    """

    @staticmethod
    def normalize(name: str) -> str:
        """
        Normalize column names for comparison.
        """
        return (
            name.strip()
            .lower()
            .replace("_", "")
            .replace(" ", "")
        )

    @staticmethod
    def validate_required_columns(mapping):
        """
        Ensure all required canonical columns are present.
        """

        missing = []

        for canonical_name, config in CANONICAL_SCHEMA.items():

            if config["required"] and canonical_name not in mapping:
                missing.append(canonical_name)

        if missing:
            raise MissingRequiredColumnsError(
                f"Missing required columns: {', '.join(missing)}"
            )

    @staticmethod
    def rename_dataframe(df, mapping):
        """
        Rename DataFrame columns to the RetailPulse canonical schema.
        """

        rename_dict = {}

        for canonical_name, original_name in mapping.items():
            rename_dict[original_name] = canonical_name

        return df.rename(columns=rename_dict)

    @staticmethod
    def build_mapping(columns):
        """
        Match uploaded columns to the RetailPulse canonical schema.
        """

        mapping = {}

        normalized_columns = {
            ColumnMapper.normalize(col): col
            for col in columns
        }

        for canonical_name, config in CANONICAL_SCHEMA.items():

            aliases = config["aliases"]

            normalized_aliases = [
                ColumnMapper.normalize(alias)
                for alias in aliases
            ]

            for alias in normalized_aliases:

                if alias in normalized_columns:
                    mapping[canonical_name] = normalized_columns[alias]
                    break

        ColumnMapper.validate_required_columns(mapping)

        return mapping

    