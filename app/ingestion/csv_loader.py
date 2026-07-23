from pathlib import Path
import pandas as pd


class CSVLoader:
    """
    Responsible for loading CSV datasets.
    """

    @staticmethod
    def load_csv(file_path: str) -> pd.DataFrame:
        """
        Load a CSV file and return a pandas DataFrame.

        Parameters
        ----------
        file_path : str
            Path to the CSV file.

        Returns
        -------
        pd.DataFrame
            Loaded dataset.

        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        ValueError
            If the file is not a CSV.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if path.suffix.lower() != ".csv":
            raise ValueError("Only CSV files are supported.")

        df = pd.read_csv(path)

        return df