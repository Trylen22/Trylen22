
import matplotlib.pyplot as plt 
import numpy as np


def problem_4():



    x = [0 ,1 ,2 ,3 ,4]
    excuses_data= [14 ,5 ,26 ,8 ,12]
    bar_labels = [
                    'I got stuck in traffic',
                    'I went to my other class',
                    'I forgot to set my alarm',
                    'I thought it was saturday',
                    'I had no clean pants to wear',]
    fig, ax = plt.subplots(1 ,1)

    ax.bar(x, excuses_data, tick_label = bar_labels, width = 0.8, color = ['gray', 'black', 'r','g','b'] )
    ax.set_ylabel('Times Excuse Is Used')
    ax.set_title('Missing Class Excuses')
    ax.set_xticks(np.arange(len(bar_labels)), labels = bar_labels)

    plt.setp(ax.get_xticklabels(), rotation = 45, ha = 'right' , rotation_mode = 'anchor')
    fig.tight_layout()
    plt.show()

problem_4()