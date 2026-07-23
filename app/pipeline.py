from app.ingestion.csv_loader import CSVLoader
from app.ingestion.validator import DatasetValidator
from app.ingestion.schema import SchemaDetector
from app.ingestion.profiler import DataProfiler

from app.ingestion.mapper import ColumnMapper
from app.preprocessing.cleaning.cleaner import DataCleaner

class RetailPipeline:
    """
    Main orchestration pipeline for RetailPulse.

    Responsible for coordinating the ingestion workflow.
    """

    def run(self, file_path: str) -> dict:

        # Step 1
        df = CSVLoader.load_csv(file_path)

        original_columns = list(df.columns)

        # Step 2
        DatasetValidator.validate_not_empty(df)

        # Step 3
        schema_report = SchemaDetector.generate_report(df)

        # Step 4
        profile_report = DataProfiler.generate_profile(df)

        # Step 5
        mapping = ColumnMapper.build_mapping(df.columns)

        df = ColumnMapper.rename_dataframe(df, mapping)

        df = DataCleaner.clean(df)

        return {

            "dataframe": df,

            "mapping": mapping,

            "original_columns": original_columns,

            "schema": schema_report,

            "profile": profile_report

        }