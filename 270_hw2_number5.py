import matplotlib.pyplot as plt

def problem_5():
    score = [115, 155]
    x = 8
    vals = [127, 124, 133, 142, 138, 125, 154, 130, 123, 118, 130, 136, 128, 150, 141, 149, 129]

    fig, ax = plt.subplots(1, 1)  # Use plt.subplots() instead of plt.subplot()
    ax.hist(vals, bins=x, range=score, color='purple', histtype='bar', rwidth=0.8)
    ax.set_ylabel('Frequency')
    ax.set_xlabel('IQ Score')
    ax.set_title('IQ Score of an Imaginary Group of People')
    fig.tight_layout()
    plt.show()

problem_5()