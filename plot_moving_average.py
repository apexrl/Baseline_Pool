import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn

# seaborn.set(style = 'darkgrid')
seaborn.set_style("whitegrid")
title_size = 20
lable_size = 18
titel_pad = 10
alpha = 0.2

def read_one_file(file_path, max_step):
    f_log = open(file_path, 'r')
    reward_list = []
    for line in f_log.readlines():
        line = line.strip()
        if line[0:2] == 'ev' or line[0:2] == 'Re' or line[0:2] == 'co':
            reward_list.append(float(line.split(': ')[1]))
        if len(reward_list) == max_step:
            return reward_list
    return reward_list

def read_multi_files(folder_path, max_step):
    files = os.listdir(folder_path)
    reward_data = []
    for file in files:
        file_type = file.split('.')[-1]
        if file_type == 'log':
            file_path = folder_path + '/' + file
            reward_data.append(read_one_file(file_path, max_step))
    return reward_data

# def MA(value, step):
#     ma_value = []
#     for i in range(len(value)):
#         tmp = value[i:i+step]
#         if len(tmp) > 0:
#             ma_value.append(sum(tmp)/len(tmp))
#     return ma_value

def MA(value, step):
    ma_value = []
    for i in range(len(value)):
        if i < 5:
            tmp = value[i:i+int(step/1.5)]
        elif 5 <= i < 10:
            tmp = value[i:i + int(step/1.3)]
        elif 10 <= i < 15:
            tmp = value[i:i + int(step / 1.1)]
        else:
            tmp = value[i:i + step]
        if len(tmp) > 0:
            ma_value.append(sum(tmp) / len(tmp))
    return ma_value


r_means = lambda x: np.nanmean(x, axis=1)
r_stderrs = lambda x: np.nanstd(x, axis=1) /  np.sqrt(np.count_nonzero(x, axis=1))
r_mins = lambda x: r_means(x) - r_stderrs(x)#np.nanmin(x, axis=1)
r_maxs = lambda x: r_means(x) + r_stderrs(x)#np.nanmax(x, axis=1)

colors = ['red','royalblue', 'green', 'purple', 'darkorange', 'red', 'orchid', 'darkorange', 'darkcyan']
methods = ['MBPO', 'BMPO','SAC', 'SLBO','PETS','convergence']
methods_1 = ['MBPO', 'BMPO']
methods_2 = ['SAC', 'SLBO', 'PETS', 'convergence']

fig, ax=plt.subplots(2,3)
# plt.subplots_adjust(left=None, bottom=0.2, right=None, top=None,
#                 wspace=None, hspace=None)

#Pendulum
env = 'pendulum'
max_step = 19
window_length = 3
for i in range(2):
    returns = read_multi_files(env + '/' + methods[i], max_step)
    returns = np.array(returns).T
    returns = np.vstack([-1600 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0]) + 1
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[0][0].fill_between(x, ma_y1, ma_y2, where=ma_y2 >= ma_y1, facecolor=colors[i], interpolate=True, alpha=alpha)
    ax[0][0].plot(x, MA(r_means(returns), window_length), color=colors[i], linewidth=2, label=methods[i])

for i in range(3):
    returns = read_multi_files(env + '/' + methods[i+2], max_step+1)
    returns = np.array(returns).T
    returns = np.vstack([-1600 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[0][0].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i+2], interpolate=True, alpha=alpha)
    ax[0][0].plot(x, MA(r_means(returns), window_length), color=colors[i+2], linewidth=2,label = methods[i])

ax[0, 0].set_title('Pendulum', fontsize=title_size, pad = titel_pad)
ax[0, 0].set_xlabel('steps', fontsize=lable_size)
ax[0, 0].set_ylabel('average return', fontsize=lable_size)
ax[0, 0].hlines(-100, 0, 20, colors='green', linestyles='dashed', linewidth=2.5)
ax[0, 0].set_xlim(left=0, right=20)
ax[0, 0].set_ylim(bottom=-1750)
x_index = [0, 4, 8, 12,16, 20]
x_label = ['0', '0.8k', '1.6k','2.4k', '3.2K', '4K']
ax[0, 0].set_xticks(x_index)
ax[0, 0].set_xticklabels(x_label)




env = 'hopper'
max_step = 95
window_length = 15
for i in range(2):
    returns = read_multi_files(env + '/' + methods[i], max_step)
    returns = np.array(returns).T
    returns = np.vstack([0.01 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0]) + 5
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[0][1].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i], interpolate=True, alpha=alpha)
    ax[0][1].plot(x, MA(r_means(returns), window_length), color=colors[i], linewidth=2,label = methods[i])

for i in range(3):
    returns = read_multi_files(env + '/' + methods[i+2], max_step+5)
    returns = np.array(returns).T
    returns = np.vstack([0.01 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[0][1].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i+2], interpolate=True, alpha=alpha)
    ax[0][1].plot(x, MA(r_means(returns), window_length), color=colors[i+2], linewidth=2,label = methods[i])

ax[0, 1].set_title('Hopper', fontsize=title_size, pad = titel_pad)
ax[0, 1].set_xlabel('steps', fontsize=lable_size)
ax[0, 1].set_ylabel('average return', fontsize=lable_size)
ax[0, 1].hlines(3500, 0, 100, colors='green', linestyles='dashed', linewidth=2.5)
ax[0, 1].set_xlim(left=0, right=100)
ax[0, 1].set_ylim(bottom=0)
x_index = [0, 20, 40, 60, 80, 100]
x_label = ['0', '20K', '40K', '60K', '80K', '100K']
ax[0, 1].set_xticks(x_index)
ax[0, 1].set_xticklabels(x_label)




env = 'walker'
max_step = 195
window_length = 15
for i in range(2):
    returns = read_multi_files(env + '/' + methods[i], max_step)
    returns = np.array(returns).T
    returns = np.vstack([0.01 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])+5
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[0][2].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i], interpolate=True, alpha=alpha)
    ax[0][2].plot(x, MA(r_means(returns), window_length), color=colors[i], linewidth=2,label = methods[i])

for i in range(3):
    returns = read_multi_files(env + '/' + methods[i+2], max_step+5)
    returns = np.array(returns).T
    returns = np.vstack([0.01 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[0][2].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i+2], interpolate=True, alpha=alpha)
    ax[0][2].plot(x, MA(r_means(returns), window_length), color=colors[i+2], linewidth=2,label = methods[i])

ax[0, 2].set_title('Walker2d', fontsize=title_size, pad = titel_pad)
ax[0, 2].set_xlabel('steps', fontsize=lable_size)
ax[0, 2].set_ylabel('average return', fontsize=lable_size)
ax[0, 2].hlines(5500, 0, 200, colors='green', linestyles='dashed', linewidth=2.5)
ax[0, 2].set_xlim(left=0, right=200)
ax[0, 2].set_ylim(bottom=-100)
x_index = [0, 40, 80, 120, 160, 200]
x_label = ['0', '40K', '80K', '120K', '160K', '200K']
ax[0, 2].set_xticks(x_index)
ax[0, 2].set_xticklabels(x_label)




env = 'ant'
max_step = 295
window_length = 15
for i in range(2):
    returns = read_multi_files(env + '/' + methods[i], max_step)
    returns = np.array(returns).T
    returns = np.vstack([0.01 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])+5
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[1][0].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i], interpolate=True, alpha=alpha)
    ax[1][0].plot(x, MA(r_means(returns), window_length), color=colors[i], linewidth=2,label = methods[i])

for i in range(3):
    returns = read_multi_files(env + '/' + methods[i+2], max_step+5)
    returns = np.array(returns).T
    returns = np.vstack([0.01 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[1][0].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i+2], interpolate=True, alpha=alpha)
    ax[1][0].plot(x, MA(r_means(returns), window_length), color=colors[i+2], linewidth=2,label = methods[i])

ax[1, 0].set_title('Ant', fontsize=title_size, pad = titel_pad)
ax[1, 0].set_xlabel('steps', fontsize=lable_size)
ax[1, 0].set_ylabel('average return', fontsize=lable_size)
ax[1, 0].hlines(6000, 0, 300, colors='green', linestyles='dashed', linewidth=2.5)
ax[1, 0].set_xlim(left=-0, right=300)
ax[1, 0].set_ylim(bottom=0)
x_index = [0, 50, 100, 150, 200, 250, 300]
x_label = ['0', '50K', '100K', '150K', '200K', '250K', '300K']
ax[1, 0].set_xticks(x_index)
ax[1, 0].set_xticklabels(x_label)




env = 'hoppernt'
max_step = 95
window_length = 15
ax[1, 1].hlines(3400, 0, 100, colors='green', linestyles='dashed', linewidth=2.5)
for i in range(2):
    returns = read_multi_files(env + '/' + methods[i], max_step)
    returns = np.array(returns).T
    returns = np.vstack([-2500 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0]) + 5
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[1][1].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i], interpolate=True, alpha=alpha)
    ax[1][1].plot(x, MA(r_means(returns), window_length), color=colors[i], linewidth=2,label = methods[i])

for i in range(3):
    returns = read_multi_files(env + '/' + methods[i+2], max_step+5)
    returns = np.array(returns).T
    returns = np.vstack([-2500 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[1][1].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i+2], interpolate=True, alpha=alpha)
    ax[1][1].plot(x, MA(r_means(returns), window_length), color=colors[i+2], linewidth=2,label = methods[i])

ax[1, 1].set_title('Hopper-NT', fontsize=title_size, pad = titel_pad)
ax[1, 1].set_xlabel('steps', fontsize=lable_size)
ax[1, 1].set_ylabel('average return', fontsize=lable_size)
ax[1, 1].legend(methods[:6],ncol=6, loc="upper left", fontsize=18, bbox_to_anchor=(-0.80, -0.15),frameon = False)
ax[1, 1].set_xlim(left=0, right=100)
ax[1, 1].set_ylim(bottom=-3000)
x_index = [0, 20, 40, 60, 80, 100]
x_label = ['0', '20K', '40K', '60K', '80K', '100K']
ax[1, 1].set_xticks(x_index)
ax[1, 1].set_xticklabels(x_label)




env = 'walkernt'
max_step = 195
window_length = 15
for i in range(2):
    returns = read_multi_files(env + '/' + methods[i], max_step)
    returns = np.array(returns).T
    returns = np.vstack([-2500 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])+5
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[1][2].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i], interpolate=True, alpha=alpha)
    ax[1][2].plot(x, MA(r_means(returns), window_length), color=colors[i], linewidth=2,label = methods[i])

for i in range(3):
    returns = read_multi_files(env + '/' + methods[i+2], max_step+5)
    returns = np.array(returns).T
    returns = np.vstack([-2500 * np.ones(returns.shape[1]), returns])
    x = np.arange(returns.shape[0])
    y1 = r_mins(returns)
    y2 = r_maxs(returns)
    ma_y1 = MA(y1, window_length)
    ma_y2 = MA(y2, window_length)
    ax[1][2].fill_between(x, ma_y1, ma_y2, where=ma_y2>=ma_y1, facecolor=colors[i+2], interpolate=True, alpha=alpha)
    ax[1][2].plot(x, MA(r_means(returns), window_length), color=colors[i+2], linewidth=2,label = methods[i])

ax[1, 2].set_title('Walker2d-NT', fontsize=title_size, pad = titel_pad)
ax[1, 2].set_xlabel('steps', fontsize=lable_size)
ax[1, 2].set_ylabel('average return', fontsize=lable_size)
ax[1, 2].hlines(3800, 0, 200, colors='green', linestyles='dashed', linewidth=2.5)
ax[1, 2].set_xlim(left=0, right=200)
ax[1, 2].set_ylim(bottom=-3000)
x_index = [0, 40, 80, 120, 160, 200]
x_label = ['0', '40K', '80K', '120K', '160K', '200K']
ax[1, 2].set_xticks(x_index)
ax[1, 2].set_xticklabels(x_label)




# ax[0][0].legend(methods[:2],ncol=1, loc="upper left", fontsize="x-large", bbox_to_anchor=(0.44, 0.3),frameon = False)
# plt.legend(handles, methods, ncol=1, loc="upper left", fontsize="x-large", bbox_to_anchor=(0.44, 0.3))
# plt.grid()
# plt.savefig(env+'.pdf')
# ax[0, 0].grid()
# ax[0, 1].grid()
# ax[0, 2].grid()
# ax[1, 0].grid()
# ax[1, 1].grid()
# ax[1, 2].grid()
plt.show()
