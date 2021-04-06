# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import operator

TOP = 30
max_value_global = str(1000000)


def get_min_value(new_valus):
    min_value = max_value_global
    for i in range(len(new_valus)):
        new_value = new_valus[i]
        if new_value > '':
            if float(min_value) > float(new_value):
                min_value = new_valus[i]
    return float(min_value)

def get_index_and_value_of_most_importamt_in_a_vido(new_values):

    for index_row in range(len(new_values)):
        row_values = new_values[index_row]
        if row_values !=['XXX']:
          # for index_value in range(len(row_values)):
            max_value_in_row = float(max(row_values))
            min_value_in_row = get_min_value(row_values)
            max_values.append(max_value_in_row)
            min_values.append(min_value_in_row)
            importance = max_value_in_row - min_value_in_row
            dic[index_row] = importance
        return importance


def find_importance_in_batch(batch,importance_in_batch):
    for index_batch in range(len(batch)):
        row_batch = batch[index_batch]
        max_value_in_row = float(max(row_batch))
        min_value_in_row = get_min_value(row_batch)
        max_values.append(max_value_in_row)
        min_values.append(min_value_in_row)
        importance_in_batch.append(max_value_in_row - min_value_in_row)
    return importance_in_batch

def the_most_important_in_a_batch(importance_in_bath):
    most_important_value = max(importance_in_bath)
    most_important_index=importance_in_bath.index(most_important_value)
    sec = float(most_important_index/2)
    important = [most_important_value,sec]
    return important

def max_important_in_dic (dic):
    top_important=[]
    for i in range(TOP):
        all_imp_values = dic.values()
        max_value = max(all_imp_values)
        max_key = get_the_key_of_a_value(dic,max_value,all_imp_values)
        top_important.append([max_key,max_value])
        del dic[max_key]
    return top_important

def get_the_key_of_a_value(dic,max_value,all_imp_values):
    key_list = list(dic.keys())
    val_list = list(all_imp_values)
    ind = val_list.index(max_value)
    key = key_list[ind]
    return key


if __name__ == '__main__':
    # read the value file and add columns names
    df_value = pd.read_csv("value_file_06_04.csv", header=None)
    df_value.columns = ['index','value']
   # df_value = df_value.drop(df_value.index[0])
    new_values = []
    max_values = []
    min_values = []
    vido_number = 0
    dic = {}
    top=[]
    #organize the data
    for index,row in df_value.iterrows():
        params_list = df_value.at[index, "value"]
        params_list = params_list.replace('[', '')
        params_list = params_list.replace(']', '')
        first_value = list(params_list.split(" "))
        new_values.append(first_value)

    index_row = 0
    while index_row < len(new_values):
        row_values = new_values[index_row]
        batch = []
        importance_in_batch = []
        while row_values != ['XXX'] and index_row < len(new_values)-1:
            batch.append(row_values)
            index_row += 1
            row_values = new_values[index_row]
        importance_in_batch = find_importance_in_batch(batch,importance_in_batch)
        important = the_most_important_in_a_batch(importance_in_batch)
        dic[vido_number] = important
        index_row += 1
        vido_number += 1
    top = max_important_in_dic(dic)
    results = pd.DataFrame()
    results['top'] = top
    results['top'].to_csv('C:/Users/yael/Documents/GitHub/HIGHWAY_ALL/results_file_highlights.csv', mode='a', header=False)
    print("top:",top)





























  #  imp = get_index_and_value_of_most_importamt_in_a_vido(new_values)
    #find the min and max values in each vido
   # for index_row in range(len(new_values)):
#        row_values = new_values[index_row]
       # for index_value in range(len(row_values)):
 #       max_value_in_row = float(max(row_values))
  #      min_value_in_row = get_min_value(row_values)
   #     max_values.append(max_value_in_row)
    #    min_values.append(min_value_in_row)
     #   importance = max_value_in_row - min_value_in_row
      #  dic[index_row] = importance
    #
#    max_key = max(dic, key=dic.get)
 #   all_values = dic.values()
  #  max_value_dic = max(all_values)
   # print('max key:', max_key)
   # print('max value', max_value_dic)



   # diff = importance_diff(min_values,max_values)



    #max_diff = max(diff)
    #most_important = diff.index(max_diff)
    #print(most_important)









     #   dictionary_sample = {param: params_list[i] for i, param in enumerate(columns)}
      #  dictinary_data.append(dictionary_sample)
    #data = pd.DataFrame.from_dict(dictinary_data)


  #  for x in number_of_rows+1:
   #     params_list = foo(x)
    #    dictionary_sample = {param: params_list[i] for i, param in enumerate(columns)}
     #   dictinary_data.append(dictionary_sample)
    #data = pd.DataFrame.from_dict(dictinary_data)








