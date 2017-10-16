def getFileContents(absFilePath):
    try:
        absFilePath=absFilePath.strip('"').strip("'")
        f1=open(absFilePath)
        f1Contents=f1.read()
        return f1Contents
    except Exception as e:
        print(e.args)
    else:
        f1.close()
if __name__=="__main__":
    print(getFileContents(input("Enter filename")))