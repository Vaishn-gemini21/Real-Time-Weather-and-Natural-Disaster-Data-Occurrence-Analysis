def run_old_code():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    #Temperature Data
    W=pd.read_csv('Weather Data.csv', header=None, names=[2006,2023], skiprows=1)
    M=W.index

    #Precipitation Data
    a=pd.read_csv('Rainfall Data.csv', header=None, names=[2006,2023],skiprows=1)
    x=a.index
    val=np.arange(len(x))
    width=0.3

    #Humidity Data
    H=pd.read_csv('Humidity Data.csv', header=None, skiprows=1, names=[2006,2023])
    v1=H[2006]
    v2=H[2023]
    i=H.index

    #Natural Disaster Occurrences Data
    N = pd.read_csv('Natural Disasters.csv', header=None, skiprows=1, names=['Floods', 'Cyclones', 'Landslides', 'Tsunamis', 'Earthquakes'])
    T = N.columns
    n = np.arange(len(T))
    N1=N.loc[2006,:]
    N2=N.loc[2023,:]

    #Choice Menu
    print('The following choices of data are available:')
    print('1. Temperature Data')
    print('2. Precipitation Data')
    print('3. Humidity Data')
    print('4. Natural Disaster History')
    c=eval(input('Enter your choice'))

    #Choice 1
    if c==1:
        print('You have chosen Temperature data, a line plot is available for data visualisation')
        print(W)
        plt.plot(M,W[2006],color='teal', marker='*', markeredgecolor='black', 
                linewidth=6, label=2006)
        plt.plot(M,W[2023], color='red', marker='^', markeredgecolor='blue', markersize=5,
                linewidth=4, label=2023)
        plt.xlabel('Month Names')
        plt.ylabel('Average Temperature in Fahrenheit')
        plt.title('Comparison of average Temperatures in 2006 and 2023 in          Mumbai, Maharashtra')
        plt.legend()
        plt.show()
        plt.savefig('Temperature Data.pdf')
        
    #Choice 2
    elif c==2:
        print('You have chosen Precipitation Data, a multibar chart is available for visualisation')
        print(a)
        plt.bar(val,a[2006],width,label='2006')
        plt.bar(val+width,a[2023],width,label='2023')
        plt.xticks(val,x)
        plt.xlabel('Month')
        plt.ylabel('Average Precipitation in Inches')
        plt.title('Precipitation Data for the Years 2006, 2023 ')
        plt.legend()
        plt.show()
        plt.savefig('Rainfall Data.pdf')
        
    #Choice 3
    elif c==3:
        print('You have chosen Humidity Data, please chose between 2006 and 2023 data. Pie chart is available for visualisation')
        c3= eval(input('2006 or 2023'))
        if c3==2006:
            print('You have chosen 2006.')
            print(v1)       
            col=['b','orange','green','red','violet','brown','pink','grey','lightgreen', 'lightblue','teal','magenta']
            plt.pie(v1, labels=i, rotatelabels=30, counterclock=False, startangle=20, colors=col)
            plt.legend(v1, bbox_to_anchor=(2,1))
            plt.title('Humidity Data for 2006')
            plt.show()
        elif c3==2023:
            print('You have chosen 2023.')
            print(v2)
            plt.pie(v2, labels=i, rotatelabels=30, counterclock=False, startangle=20)
            plt.legend(v2, bbox_to_anchor=(2,1))
            plt.title('Humidity Data for 2023')
            plt.show()
            
    #Choice 4
    elif c==4:
        print('YOu have chosen Natural Disaster History. Please choose between 2006 and 2023 data.')
        c4=eval(input('2006 or 2023'))
        if c4==2006:
            print(N1)
            plt.hist(n, bins=np.arange(len(T)+1), weights=N.loc[2006], color='teal', edgecolor='black')
            plt.xticks(n, T)
            plt.xlabel('Disaster Type')
            plt.ylabel('Frequency of occurrence throughout the year')
            plt.title('Frequency of occurrence of Natural Disasters in the world in 2006')
            plt.savefig('Natural_Disasters_2006.pdf')
            plt.show()

        elif c4==2023:
            print(N2)
            plt.hist(n, bins=np.arange(len(T)+1), weights=N.loc[2023], color='red', edgecolor='purple')
            plt.xticks(n, T)
            plt.xlabel('Disaster Type')
            plt.ylabel('Frequency of occurrence throughout the year')
            plt.title('Frequency of occurrence of Natural Disasters in the world in 2023')
            plt.savefig('Natural_Disasters_2023.pdf')
            plt.show()
    else:
        print('Error, please try again')