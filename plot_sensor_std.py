#Show all features
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sensor_std(df_data):
    plt.subplot(641)
    sns.distplot(df_data['setting1'])
    plt.title('setting1')

    plt.subplot(642)
    sns.distplot(df_data['setting2'])
    plt.title('setting2')

    plt.subplot(643)
    sns.distplot(df_data['setting3'])
    plt.title('setting3')

    plt.subplot(644)
    sns.distplot(df_data['s1'])
    plt.title('Sensor 1')

    plt.subplot(645)
    sns.distplot(df_data['s2'])
    plt.title('Sensor 2')

    plt.subplot(646)
    sns.distplot(df_data['s3'])
    plt.title('Sensor 3')

    plt.subplot(647)
    sns.distplot(df_data['s4'])
    plt.title('Sensor 4')

    plt.subplot(648)
    sns.distplot(df_data['s5'])
    plt.title('Sensor 5')

    plt.subplot(649)
    sns.distplot(df_data['s6'])
    plt.title('Sensor 6')

    plt.subplot(6,4,10)
    sns.distplot(df_data['s7'])
    plt.title('Sensor 7')

    plt.subplot(6,4,11)
    sns.distplot(df_data['s8'])
    plt.title('Sensor 8')

    plt.subplot(6,4,12)
    sns.distplot(df_data['s9'])
    plt.title('Sensor 9')

    plt.subplot(6,4,13)
    sns.distplot(df_data['s10'])
    plt.title('Sensor 10')

    plt.subplot(6,4,14)
    sns.distplot(df_data['s11'])
    plt.title('Sensor 11')

    plt.subplot(6,4,15)
    sns.distplot(df_data['s12'])
    plt.title('Sensor 12')

    plt.subplot(6,4,16)
    sns.distplot(df_data['s13'])
    plt.title('Sensor 13')

    plt.subplot(6,4,17)
    sns.distplot(df_data['s14'])
    plt.title('Sensor 14')

    plt.subplot(6,4,18)
    sns.distplot(df_data['s15'])
    plt.title('Sensor 15')

    plt.subplot(6,4,19)
    sns.distplot(df_data['s16'])
    plt.title('Sensor 16')

    plt.subplot(6,4,20)
    sns.distplot(df_data['s17'])
    plt.title('Sensor 17')

    plt.subplot(6,4,21)
    sns.distplot(df_data['s18'])
    plt.title('Sensor 18')

    plt.subplot(6,4,22)
    sns.distplot(df_data['s19'])
    plt.title('Sensor 19')

    plt.subplot(6,4,23)
    sns.distplot(df_data['s20'])
    plt.title('Sensor 20')

    plt.subplot(6,4,24)
    sns.distplot(df_data['s21'])
    plt.title('Sensor 21')

    plt.tight_layout(pad=1, w_pad=1, h_pad=1)