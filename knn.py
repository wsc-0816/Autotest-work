from numpy import *
import operator
''' 
KNN algorithm 



'''
def createDataSet():
	''' Create the Data set and the labels. This is the way to define the training set 
	    Please pay attention to the order''' 
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group ,labels 
def calssfiy0(inX,dataSet,lables ,k):
	'''By using the euclidean metric 
	   According to the euclidean metric:
	   eg :(in the three-dimensional space)
	       d = sqrt ((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
	'''
	'''get the size of the DataSet,that means how many elements in this set '''
	dataSetSize = dataSet.shape[0]
	'''tile(element,(rowNumber,colNumber)): This function takes three inputs and generate an array([[]])
	          The element can be a number or everything include the number.
	          The rowNumber and colNumber are the format you want. 
	    The diffMat is going to do the subtraction between the One you create and the original one. 
	    The inX is the data you want to predict. The format must be the same as the DataSet 
	'''
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	'''Calculate the suqre of the data set  '''
	sqDiffMat =  diffMat**2 
	''' '''
	sqDistances =  sqDiffMat.sum(axis=1)

