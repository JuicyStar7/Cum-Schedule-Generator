from numpy import random
import numpy as np
import webbrowser
import sub_lists as subs


# function to open links


def open_link(link, sub_bool):
    if sub_bool:
        webbrowser.open(f"https://www.reddit.com/r/{link}", new=2)
    else:
        webbrowser.open(link, new=2)


# function to pick a random subreddit for other functions


def pick_sub(n):
    lists_num = np.array([subs.master_df.iloc[:, -1:]]).flatten()
    rand_sub = random.choice(subs.master_df.iloc[n, random.randint(lists_num[n])])
    return rand_sub


# function to open a random subreddit


def random_sub(n):
    rand_sub = pick_sub(n)
    open_link(rand_sub, True)


# function to open a random exposedtostrangers.com video


def random_ets():
    webbrowser.open("https://exposedtostrangers.com/?redirect_to=random&count=36&bias=01&each_once=rewind", new=2)


# sample un-needed atm function to make a list of random unrepeated integers

'''
def rand_nums(sample_size, upper):
    answer = set()
    answer_size = 0

    while answer_size < sample_size:
        r = random.randint(0, upper)
        if r not in answer:
            answer_size += 1
            answer.add(r)
    return answer
'''


# function to return a random subreddit without opening it


def random_sub_for_schedule(n):
    rand_sub = pick_sub(n)
    return rand_sub
