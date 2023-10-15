import pandas as pd
from typing import List

#   pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
#
#   data:       ndarray, Iterable, dict, or DataFrame
#   index:      (row labels) defaults to RangeIndex if not specified or included in `data`
#   columns:    (column labels) defaults to RangeIndex, selects columns if `data` contains column labels
#   dtype:      Datatype to force, will be infered if not given
#   copy:       Should input be copied, (defaults to True)

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])


student_data = [[1,15],[2,11],[3,11],[4,20]]
print(f"student_data=({student_data})")
result = createDataframe(student_data)
print(f"result=({result})")
 
