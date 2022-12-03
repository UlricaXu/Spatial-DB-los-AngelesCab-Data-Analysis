import pandas as pd
import geopandas as gpd
import numpy as np
import osmnx as ox
import networkx as nx
import warnings
from shapely.geometry import Point

warnings.simplefilter("ignore")

def gen_raw_data():
    # step. 获取id列表
    fp = open('C:/Users/86159/Desktop/Spatial-DB los Angeles Data Analysis/Python/cabspottingdata/_cabs.txt', 'r')
    lines = fp.readlines()
    id_list = [line.split("\"")[1] for line in lines]

    # step. 读所有txt，并处理为df
    raw_df = pd.DataFrame()
    s = 1
    for id in id_list:
        df = pd.read_csv(f"C:/Users/86159/Desktop/Spatial-DB los Angeles Data Analysis/Python/cabspottingdata/new_{id}.txt", header=None, sep=" ")
        df.columns = ['latitude', 'longitude', 'occupancy', 't']
        df.pop('occupancy')  # drop无关列occupancy
        df.insert(0, 'id', [id for _ in range(df.shape[0])])  # 插入新列：id
        raw_df = pd.concat([raw_df, df], axis=0)  # 拼接

        print('Finished merging {}/{}'.format(s, len(id_list)))
        s += 1

    raw_df = raw_df.sort_values(by=['id', 't'], ascending=[True, True])  # 按id和t升序排序
    raw_df = raw_df.set_index('t')  # 以t为index

    print('get raw_df, columns=[latitude, longitude, id], index=t')

    # step. 将包含所有车的原始数据写入./data/sf_tolerance/raw_data.csv
    raw_df.to_csv('C:/Users/86159/Desktop/raw_data.csv')

def main():

    gen_raw_data()
    raw_df = pd.read_csv('./data/sf_tolerance/raw_data.csv')
    print(raw_df)


