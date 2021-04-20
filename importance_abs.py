import pandas as pd
import statistics
TOP = 30
def two_standard_deviation(max_values, max_values_index):
    avg = sum(max_values) / len(max_values)
    smaller = float(avg - 2*devistion)
    min_max = []
    for i in range(len(max_values)):
        if max_values[i]<= smaller:
            min_max.append([max_values_index[i], max_values[i]])
    return min_max


def dic_of_videos(new_values):
    dic = {}
    index_new_value = 0
    vido_number = 0
    beginning_batch = 0
    ending_batch = 0
    while index_new_value < len(new_values):
        row_values = new_values[index_new_value]
        while row_values != ['XXX']:
            if index_new_value < len(new_values) - 1:
                index_new_value += 1
                row_values = new_values[index_new_value]
            else:
                index_new_value += 2
                break
        ending_batch = index_new_value-1
        dic[vido_number] = [beginning_batch,ending_batch]
        index_new_value += 1
        beginning_batch = index_new_value
        vido_number += 1
    return dic

#this functhion returns a list os lists with the values of: key = the number of video,
#sec = the second of the value and the value
def find_the_videos_with_duplicates(min_max,dic):
    i_min_max = 0
    video_num=[]
    for key in dic:
        time= min_max[i_min_max][0]
        while time >= dic[key][0] and time <= dic[key][1]:
            if i_min_max < len(min_max)-1:
                value = min_max[i_min_max][1]
                sec = (time - dic[key][0])/2
                video_num.append([key, sec, value])
                i_min_max += 1
                time = min_max[i_min_max][0]
            else:
                value = min_max[i_min_max][1]
                video_num.append([key, (time - dic[key][0])/2,value ])
                break
    return video_num


def find_the_videos_with_out_duplicates(video_num_duplicates):
    video_num_no_duplicates = []
    key = 0
    i_dup = 0
    while i_dup in range(len(video_num_duplicates)-1):
        if video_num_duplicates[i_dup][key]==video_num_duplicates[i_dup+1][key]:
            best_from_dup = get_the_min_from_duplicates(i_dup,video_num_duplicates)
            best_value = best_from_dup[1]
            i_dup = best_from_dup[0]
        else:
            best_value=video_num_duplicates[i_dup]
            i_dup+=1
        video_num_no_duplicates.append(best_value)
    return video_num_no_duplicates

def get_the_min_from_duplicates(i_dup,video_num_duplicates):
    key = 0
    val = 2
    value_of_dup_key = []
    first = i_dup
    value_of_dup_key.append(video_num_duplicates[i_dup][val])
    while video_num_duplicates[i_dup][key]==video_num_duplicates[i_dup+1][key]and i_dup< len(video_num_duplicates)-2:
        i_dup += 1
        value_of_dup_key.append(video_num_duplicates[i_dup][val])
        flag =1
    min_value = min(value_of_dup_key)
    index_of_min = value_of_dup_key.index(min_value)+first
    best_value = video_num_duplicates[index_of_min]

    return [i_dup+1, best_value]

def find_num_of_video(min_value,video_num_no_duplicates):
    for i_value in range(len(video_num_no_duplicates)):
        if min_value == video_num_no_duplicates[i_value][2]:
            return video_num_no_duplicates[i_value]

def get_top_no_duplicates(video_num_no_duplicates):
    all_values = []
    top=[]
    for i_value in range (len(video_num_no_duplicates)):
        all_values.append(video_num_no_duplicates[i_value][2])

    for i_TOP in range(TOP):
        min_value = min(all_values)
        #index_of_min_value = all_values.index(min_value)
        #best_value = video_num_no_duplicates[index_of_min_value]
        best_value = find_num_of_video(min_value,video_num_no_duplicates)
        top.append(best_value)
        all_values.remove(min_value)
    print(top)
    return top


if __name__ == '__main__':
    # read the value file and add columns names
    df_value = pd.read_csv("value_file_20_04.csv", header=None)
    df_value.columns = ['index','value']
    #df_value = df_value.drop(df_value.index[0])
    new_values = []
    max_values = []
    max_values_index=[]
    min_values = []
    vido_number = 0
    top=[]
    #organize the data
    for index,row in df_value.iterrows():
        params_list = df_value.at[index, "value"]
        params_list = params_list.replace('[', '')
        params_list = params_list.replace(']', '')
        first_value = list(params_list.split(" "))
        new_values.append(first_value)

    for index_new_value in range(len(new_values)):
        row_values = new_values [index_new_value]
        if row_values != ['XXX']:
            value = max(row_values)
            max_values.append(float(value))
            max_values_index.append(index_new_value)

    devistion = statistics.stdev(max_values)
    min_max = two_standard_deviation(max_values,max_values_index)
    dic = dic_of_videos(new_values)
    video_num_duplicates = find_the_videos_with_duplicates(min_max, dic)
    video_num_no_duplicates = find_the_videos_with_out_duplicates(video_num_duplicates)
    top = get_top_no_duplicates(video_num_no_duplicates)
    results = pd.DataFrame()
    results['top'] = top
    results['top'].to_csv('C:/Users/yael/Documents/GitHub/HIGHWAY_ALL/results_file.csv', mode='a', header=False)



