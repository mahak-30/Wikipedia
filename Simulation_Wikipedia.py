
# coding: utf-8

# In[1]:

#importing the libraries
import random
import numpy as np
import time
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

#defining the power law for the distribution of balls in the bins
def fillBallInBins(binCount, phi, alpha) :         
    bins = []
    total = 0
    for x in range(1, binCount+1) : 
        bins.append(round(phi * (x ** -alpha))+1) #assigning the balls into the bins and shifting the entire graph upwards by one unit
    return bins


# In[3]:

#defining the power low for the distribution of colors to balls
def distributeColorsToBalls(colorArray, bins) :
    totalBins = len(bins) #total number of bins used
    totalColors = len(colorArray) #number of distinct colors used
    binsArray = []
    for i in range(totalBins) :
        balls = bins[i]
        temp = []
        for _ in range(balls) :
            r = random.randint(0, totalColors-1) #assigning a random color from the color array to the ball
            color = colorArray[r]
            temp.append(color)
        binsArray.append(sorted(temp))
    return binsArray


# In[4]:


def drawGraph1(bins, index) :  #Graph1: distribution of balls into the bins
    fig, ax = plt.subplots(figsize=(8, 5.5)) #setting the size of the graph
    plt.grid(True, color="#93a1a1", alpha=0.2)
    #defining the axes of the graph
    ax.set_title("Distribution of balls in bins", fontsize=25)
    ax.set_xlabel("Index of bins", labelpad=15, fontsize=15, color="#333533")
    ax.set_ylabel("Number of balls in a bin", labelpad=15, fontsize=15, color="#333533")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(bins, color="#073642")
    plt.savefig('Graph'+str(index)+'.1.png') #downloading and saving the graph
    plt.close() #pevents the graph to be printed in the terminal


# In[5]:


def drawGraph2(colorArray, index):  #Graph2: distribution of colors among the balls
    hurray = []
    for i in range(1, 1001) :
        hurray.append(colorArray.count(i))
    fig, ax = plt.subplots(figsize=(8, 5.5))  #setting the size of the graph
    plt.grid(True, color="#93a1a1", alpha=0.2)
    #defining the axes for the graph
    ax.set_title("Distribution of colors in balls", fontsize=25)
    ax.set_xlabel("Index of balls", labelpad=15, fontsize=15, color="#333533")
    ax.set_ylabel("Number of balls of one color", labelpad=15, fontsize=15, color="#333533")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(hurray, color="#073642")
    plt.savefig('Graph'+str(index)+'.2.png') #downloading and saving the graph
    plt.close() #pevents the graph to be printed in the terminal


# In[6]:


def drawBinVsColor(binVsColor, index, label) : #graph 3 and graph 4: for bins used vs colors
    fig, ax = plt.subplots(figsize=(8, 5.5)) #setting the size of the graph
    plt.grid(True, color="#93a1a1", alpha=0.2)
    #defining the axes for the graph
    ax.set_title("Bins Vs Colors ("+label+")", fontsize=25)
    ax.set_xlabel("Bins used", labelpad=15, fontsize=15, color="#333533")
    ax.set_ylabel("Colors in box", labelpad=15, fontsize=15, color="#333533")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(binVsColor, color="#073642")
    #checking if the selection of bins is random or follows the power-law
    if label == "random" :
        plt.savefig('Graph'+str(index)+'.3.png')
    else :
        plt.savefig('Graph'+str(index)+'.4.png')
    plt.close() #pevents the graph to be printed in the terminal


# In[7]:


def drawTimeVsColor(timeVsColor, index, label) : #graph 5 and graph 6: for time taken vs colors
    fig, ax = plt.subplots(figsize=(8, 5.5)) #setting the size of the graph
    plt.grid(True, color="#93a1a1", alpha=0.2)
    #defining the axes for the graph
    ax.set_title("Time Vs Colors ("+label+")", fontsize=25)
    ax.set_xlabel("Time Taken", labelpad=15, fontsize=15, color="#333533")
    ax.set_ylabel("Colors in box", labelpad=15, fontsize=15, color="#333533")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(timeVsColor, color="#073642")
    #checking if the selection of bins is random or follows the power-law
    if label == "random" :
        plt.savefig('Graph'+str(index)+'.5.png')
    else :
        plt.savefig('Graph'+str(index)+'.6.png')
    plt.close() #pevents the graph to be printed in the terminal


# In[8]:

#storing the distribution of colors into the color array
def getColorDistribution(totalColors, phi, alpha) :
    colorArray = [] #defining th color array
    for x in range(1, totalColors+1) :
        temp = round((phi * (x ** -alpha))+1) #assigning the colors to the balls and shifting the entire graph upwards by one unit
        for _ in range(temp) :
            colorArray.append(x)
    return colorArray


# In[9]:


def results(binDistribution, totalColors, phi, alpha, distribution) : 
    BinsArray = []
    totalBins = len(binDistribution)
    
    if distribution == "power" : 
        for x in range(1, totalBins+1) :
            temp = (round(phi * (x ** -alpha))+1) #selecting the bins as per the power law and shifting the entire graph upwards by one unit
            for _ in range(temp) :
                BinsArray.append(x)
    
    elif distribution == "random" :
        BinsArray = binDistribution #selecting the bins randomly
                
    finalBox = set()
    binsUsed = set()
    ballsDrawn = 0
    binVsColor = [0]
    timeVsColor = []
    colors80 = int(0.8 * totalColors) #variable to store 80 percent of the total colors
    done80 = False #variable to check if 80 percent of the box is filled
    while len(finalBox) != totalColors : #loop that will continue until the box ix completely filled
        r1 = random.randint(0, len(BinsArray)-1)
        randomBin = binDistribution[BinsArray[r1]-1] if distribution == "power" else binDistribution[r1]
        binsUsed.add(r1)
        r2 = random.randint(0, len(randomBin)-1)
        randomBall = randomBin[r2]
        ballsDrawn += 1
        finalBox.add(randomBall)
        timeVsColor.append(len(finalBox))
        if len(finalBox) == colors80 and not done80:
            done80 = True
#             print("Upto 80% mark : Balls in box =",colors80,"\t Bins Used =",len(binsUsed))
        try :
            binVsColor[len(binsUsed)] = len(finalBox)
        except :
            binVsColor.append(len(finalBox))
#     print("arrayIndex = ",ballsDrawn, "\tDistinct Balls =", len(finalBox),"\tBins Used =", len(binsUsed))
    return binVsColor, timeVsColor, len(binsUsed)


# In[10]:


def doAll(index):
    binsUsed = {}
    binCount = 100000  #defining the total number of bins used
    totalColors = 5000  #defining the total number of colors`
    colorArray = getColorDistribution(totalColors, phi = 200, alpha = 2.4)  #function call to store the distribution of colors
    bins = fillBallInBins(binCount, phi = 500, alpha = 2.4)  #function call to store the number of balls into the bins
    drawGraph1(bins, index)  #function call to draw graph 1
    drawGraph2(colorArray, index) #function call to draw graph 2
    binDistribution = distributeColorsToBalls(colorArray, bins) #function call to distribute to colors among the balls
    binVsColor, timeVsColor, binsUsed["power"] = results(binDistribution, 5000, 200, 3.0, distribution = "power") #function call to select bins as per the power-law
    drawBinVsColor(binVsColor, index, label = "power") #function call to draw graph 3: bins used vs color for power-law selection
    drawTimeVsColor(timeVsColor, index, label = "power") #function call to draw graph 4: time taken vs color for power-law selection
    binVsColor, timeVsColor, binsUsed["random"]= results(binDistribution, 5000, 200, 3.0, distribution = "random") #function call to select the bins randomly
    drawBinVsColor(binVsColor, index, label = "random") #function call to draw graph 3: bins used vs color for power-law selection
    drawTimeVsColor(timeVsColor, index, label = "random") #function call to draw graph 4: time taken vs color for power-law selection
    return binsUsed


# In[11]:


def iterate(times) :  #defining the number of times the following code should iterate
    t = time.time()
    powerArray = []
    randomArray = []
    for i in range(times) :
        powerArray.append(doAll(i+1)["power"])  #storing the number of bins used in an array
        randomArray.append(doAll(i+1)["random"]) #storing the number of bins used in an array
        if i%10 == 0 :
            print("Iteration ",i+1,"\t time taken = ","{:.2f}".format(time.time()-t), "seconds") #saves the time taken per 10 iterations
    fig, ax = plt.subplots(figsize=(8, 5.5)) #defining the size of the graph
    #defining the axes for the graph
    ax.set_title("Frequency histogram of number of bins used following power-law", fontsize=25)
    ax.set_xlabel("Number of bins used", labelpad=15, fontsize=15, color="#333533")
    ax.set_ylabel("Frequency", labelpad=15, fontsize=15, color="#333533")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.hist(powerArray, align = 'mid', rwidth = 0.8)
    plt.savefig('Histogram1') #plotting the histogram for power-law selection of bins
    fig, ax = plt.subplots(figsize=(8, 5.5)) #defining the size of the graph
    #defining the axes for the graph
    ax.set_title("Frequency histogram of number of bins used following random selection", fontsize=25)
    ax.set_xlabel("Number of bins used", labelpad=15, fontsize=15, color="#333533")
    ax.set_ylabel("Frequency", labelpad=15, fontsize=15, color="#333533")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.hist(randomArray, align = 'mid', rwidth = 0.8)
    plt.savefig('Histogram2') #Plotting the histogram for random selection of bins
    
    print("Average number of bins picked using power law :",np.mean(powerArray))  #calculating the average number of bins used in all the iterations for power-law
    print("Average number of bins picked using random selection :",np.mean(randomArray))   #calculating the average number of bins used in all the iterations following random selection of bins


# In[12]:


iterate(100)  #passing the total number of iterations to be done

