import pandas as pd

class DataFrameOperator:
    """
    Knows how to work with a DataFrame
    """

    def __init__(self, working_dataframe: pd.DataFrame):
        self._working_dataframe = working_dataframe

    def keep_only_values(self, column_name: str, values_to_keep: list[str]) -> "DataFrameOperator":
        """
        :param column_name: target column.
        :param values_to_keep: values in the target column that should be kept.
        :return: DataFrameOperator.
        """
        self._working_dataframe = self._working_dataframe[self._working_dataframe[column_name].isin(values_to_keep)]
        return self

    def keep_only_columns(self, columns_to_keep: list[str]) -> "DataFrameOperator":
        """
        :param columns_to_keep: the columns that should be kept.
        :return: DataFrameOperator.
        """
        self._working_dataframe = self._working_dataframe[columns_to_keep]
        return self

    def sort_by(self, column_name, increasing_order: False) -> "DataFrameOperator":
        """
        :param column_name: target column that will be used for sorting.
        :param increasing_order: the order of the sorted result
        :return: DataFrameOperator.
        """
        self._working_dataframe = self._working_dataframe.sort_values(by=column_name, ascending=increasing_order)
        return self

    @property
    def operate(self) -> pd.DataFrame:
        """
        :return: the operated DataFrame.
        """
        return self._working_dataframe


if __name__ == '__main__':
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e'],
        'C': [10, 20, 30, 40, 50]
    })

    operator = DataFrameOperator(df)
    result = (operator
              .keep_only_values('B', ['a', 'c', 'e'])
              .keep_only_columns(['A', 'B'])
              .sort_by('A', increasing_order=True)
              .operate)

    print(result)