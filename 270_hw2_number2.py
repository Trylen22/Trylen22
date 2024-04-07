import matplotlib.pyplot as plt

def problem_2():
    x1 = [2, 3, 4, 5]
    y1 = [9, 4, 3, 2]
    x2 = [11, 20, 30, 50]
    y2 = [20, 30, 50, 60]

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    fig.suptitle('2 plots on one figure')

    ax[0].plot(x1, y1, 's-', color='red', linestyle='dashdot', markerfacecolor='white', markeredgecolor='red')
    ax[0].set_ylabel('Problem 2 y1 data')
    ax[0].set_xlabel('Problem 2 x1 data')

    ax[1].plot(x2, y2, 'D-', color='red', fillstyle='none',  label='x2, y2')
    ax[1].plot(y1, y2, 'o-', color='orange', linestyle='dotted', markerfacecolor='white', markeredgecolor='orange', label='x1, y1')
    ax[1].set_ylabel('Problem 2 y2 data')
    ax[1].set_xlabel('Problem 2 x2 data')
    ax[1].legend(loc='lower right')

    plt.tight_layout()
    plt.show()

problem_2()