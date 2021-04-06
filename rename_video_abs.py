import os
import pandas as pd
from tkinter import Tcl

def create_clean_data(df_value,video_num,list_sec,list_val,list_index):
    for index, row in df_value.iterrows():
        temp = df_value[1][index]
        if "[" in temp:
            unnec,temp = temp.split("[")
        if "]" in temp:
            temp,unnec = temp.split("]")
        if "," in temp:
            vid, sec,value = temp.split(",")
            video_num.append(vid)
            list_sec.append(sec)
            list_val.append(value)
            list_index.append(index)

def convert_to_int (video_num):
    int_video_num =[]
    for i in range (len(video_num)):
        temp = video_num[i]
        int_video_num.append(int(temp))
    return int_video_num

def sort_all_parameters_by_video_number(video_num, list_sec, list_val,list_index, sorted_video_num, sorted_list_sec,
                                        sorted_list_val,sorted_index):
    int_video_num = convert_to_int (video_num)
    i = 0
    while i in range(len(int_video_num)):
        min_value = min(int_video_num)
        min_index = int_video_num.index(min_value)
        sorted_video_num.append(min_value)
        sorted_list_sec.append(list_sec[min_index])
        sorted_list_val.append(list_val[min_index])
        sorted_index.append(list_index[min_index])
        del int_video_num[min_index]
        del list_sec[min_index]
        del list_val[min_index]
        del list_index[min_index]


if __name__ == '__main__':

    #path = 'C:/Users/yael/PycharmProjects/importance/ABS_IMPORTANT TOP 30'
    #path = 'C:/Users/yael/Documents/GitHub/HIGHWAY_ALL/try'
    path = 'C:/Users/yael/Documents/GitHub/HIGHWAY_ALL/TOP 30_ABS'
    files = os.listdir(path)
    df_value = pd.read_csv('results_file.csv', header =None)
    video_num = []
    list_sec = []
    list_val = []
    list_index = []
    create_clean_data(df_value,video_num,list_sec,list_val,list_index)
    sorted_video_num = []
    sorted_list_sec = []
    sorted_list_val = []
    sorted_index = []
    sort_all_parameters_by_video_number(video_num, list_sec, list_val,list_index, sorted_video_num, sorted_list_sec,
                                        sorted_list_val,sorted_index)
    for index,file in enumerate(files):
        original_name = file
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(sorted_index[index]),'_',str(sorted_video_num[index]),'_',str(sorted_list_sec[index]),'.mp4'])))