import pandas as pd
import numpy as np

def num_using_2d():
    _2d_arr = np.array(np.random.randint(low=1, high=10, size=(3,3), dtype=np.int8))
    df = pd.DataFrame(data=_2d_arr, columns=list('ABC'), index=list('XYZ'), dtype=np.int8)
    print("Numpy Using 2d Array")
    print(df)
    print("#"*50)


def list_using_2d():
    _2d_arr = [['Dhivagar', 97, 98], ['Arun', 96, 97], ['Praveen', 94, 92], ['Vicky', 90, 89]]
    df = pd.DataFrame.from_records(_2d_arr, columns='Name,Mark1,Mark2'.split(','))
    print("List Using 2d Array")
    print(df)
    print("#"*50)


def from_dict_using_2d():
    _2d_arr = [['Dhivagar', 97, 98], ['Arun', 96, 97], ['Praveen', 94, 92], ['Vicky', 90, 89]]
    df = pd.DataFrame.from_dict(data=dict(zip(['Name', 'Mark1', 'Mark2'], zip(*_2d_arr))))
    print("Dict Using 2d Array")
    print(df)
    print("#"*50)


def dict_using_2d():
    _2d_arr = {'Name': ['Dhivagar', 'Arun', 'Praveen', 'Vicky'],
               'Mark1': [97, 96, 94, 90], 'Mark2': [98, 97, 92, 89]}
    df = pd.DataFrame(data=_2d_arr, dtype=object)
    print("Dict Using 2d Array")
    print(df)
    print("#"*50)


def series_using_2d():
    name_series = pd.Series(data=['Dhivagar', 'Arun', 'Praveen', 'Vicky'],
                            index=['CSE01', 'CSE02', 'CSE03', 'CSE04'],)
    m1_series = pd.Series(data=[97, 96, 94, 90], index=['CSE01', 'CSE02', 'CSE03', 'CSE04'],
                          dtype=np.int8, )
    m2_series = pd.Series(data=[98, 97, 92, 89], index=['CSE01', 'CSE02', 'CSE03', 'CSE04'],
                          dtype=np.int8,)
    df = pd.DataFrame(data={'Name': name_series, 'Mark1':m1_series, 'Mark2': m2_series}, columns=['Name', 'Mark1', 'Mark2'])
    print("Series Using 2d Array")
    print(df)
    print("#"*50)

num_using_2d()
list_using_2d()
from_dict_using_2d()
dict_using_2d()
series_using_2d()
