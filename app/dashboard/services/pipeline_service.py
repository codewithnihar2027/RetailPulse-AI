from pathlib import Path
import tempfile

from app.pipeline import RetailPipeline


class PipelineService:

    @staticmethod
    def process_uploaded_file(uploaded_file):

        suffix = Path(uploaded_file.name).suffix

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(uploaded_file.getbuffer())

            temp_path = temp_file.name

        pipeline = RetailPipeline()

        return pipeline.run(temp_path)