import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import statistics

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_of_population = statistics.mean(data)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.show()

mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)
show_fig(mean_list)

std_deviation = statistics.stdev(mean_list)
mean_of_sample_data = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean_of_sample_data)
print("Standard deviation of sampling distribution:- ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean_of_population-std_deviation, mean_of_population+std_deviation
second_std_deviation_start, second_std_deviation_end = mean_of_population-(2*std_deviation), mean_of_population+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean_of_population-(3*std_deviation), mean_of_population+(3*std_deviation)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_population, mean_of_population], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample_data, mean_of_sample_data], y=[0, 0.17], mode="lines"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean_of_population - mean_of_sample_data)/std_deviation
print("The z score is = ",z_score)
