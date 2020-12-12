import matplotlib.pyplot as plt
import numpy as np

def plot_sensor_signal(df, signal_name):

    
    plt.figure(figsize=(13,5))
    for i in df['id'].unique():
        if (i % 20 == 0):  
            plt.plot('RUL', signal_name, 
                     data=df[df['id']==i])
    plt.xlim(250, 0)  # reverse the x-axis so RUL counts down to zero
    plt.xticks(np.arange(0, 300, 25))
    plt.ylabel(signal_name)
    plt.xlabel('Remaining Use fulLife')
    plt.show()