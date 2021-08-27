import matplotlib.pyplot as plt
import numpy as np

def question(count , c ):
    plt.scatter(count, c, marker='+')
    plt.xlabel("Memory address")
    plt.ylabel("cycle number")
    plt.xlim(0,257)
    plt.ylim(0,257)

    