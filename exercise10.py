import requests
import pickle

def iris(url):
    res = requests.get(url)
    with open("iris.txt",'a') as f:
        f.write(str(res.text))
    
    lst = []
    with open("iris.txt") as f:
        fileObj = f.read().split()
        for content in fileObj:
            lst.append([content])
    
    # Pickle the fetch data in a file
    file = "mypickle.pkl"
    fObj = open(file,"wb")
    pickle.dump(lst,fObj)
    fObj.close()

    # Unpickle the data from a file
    lst2 = []
    file = "mypickle.pkl"
    myfileObj = open(file,"rb")
    depickling = pickle.load(myfileObj)
    for data in depickling:
        lst2.append(data)
    print(lst2)
    f.close()
    
if __name__ == "__main__":
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    iris(url)
