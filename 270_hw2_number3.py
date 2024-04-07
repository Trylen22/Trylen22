#problem 3
import matplotlib.pyplot as plt
def problem_3():

    forget = ['You try to guess and you get it right', 'You try to guess and you get it wrong', 'You wait for someone else to say the name']

    answers = [2, 5, 93] 

    sector_colors = ['r','b','g']

    fig, ax = plt.subplots(1,1)

    fig.suptitle('When You Forget Someones Name')

    ax.pie(answers, labels = forget, colors= sector_colors, startangle=315,
           shadow= False, explode=[0.2, 0, 0], radius=1.0, )

    ax.legend(loc = 'upper center')

    plt.show()

problem_3()