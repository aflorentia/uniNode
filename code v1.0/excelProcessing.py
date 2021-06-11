import pandas as pd


def searchingByName(search, df ):

    coordinatesList = None
    coorL = None
    coorR = None

    for row in range(0, df.shape[0]):
        if search == df.loc[row][0]:
            coordinatesList = (df.loc[row][1]).split(',')

            coorL = float(coordinatesList[0])
            coorR = float(coordinatesList[1])

            #print("The coordinates of \""+search +"\" are "+ str(coorL) + " , "+ str(coorR))
            #print(type(coorL))

            return coorL, coorR

    if coordinatesList is None:
        print("The Classroom \""+ search +"\" you searched does not exists")
        return coorL, coorR


def getTheList(df):

    coordinatesList = []
    for row in range(0, df.shape[0]):

        name = df.loc[row][0]
        # name = coordinatesListTEMP1

        coordinatesListTEMP = (df.loc[row][1]).split(',')

        coorL = float(coordinatesListTEMP[0])
        coorR = float(coordinatesListTEMP[1])

        tempDataList = {'name': name, 'lat': coorL, 'lon': coorR}
        # print("The coordinates of \""+search +"\" are "+ str(coorL) + " , "+ str(coorR))
        coordinatesList.append(tempDataList)

    return coordinatesList


def initialize(which):
    if which == 0:
        df = pd.read_excel('classrooms.xlsx', index_col=None, header=None)
    if which == 1:
        df = pd.read_excel('busStations.xlsx', index_col=None, header=None)
    return df


