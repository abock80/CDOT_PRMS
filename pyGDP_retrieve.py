
# coding: utf-8

# In[ ]:

# This is a script/ipython notebook to summarize area-weighted precipitation and temperature data by HRU 
# for a specific area of interest


# In[1]:

import pyGDP,os
import pprint
pyGDP=pyGDP.pyGDPwebProcessing()
thisdir = os.getcwd()


# In[2]:

shapefiles = pyGDP.getShapefiles()
#prints 'Available shapefiles: '
for shapefile in shapefiles:
    print shapefile

# will need to manually upload shapefiles to GDP until we get the shapetoZip/upload shapefile function working    


# In[18]:

# shapefile to use on the GDP
shapefile="upload:R10L_56"
names=shapefile.split(":")[1]
#attributes = pyGDP.getAttributes(shapefile)
#for attr in attributes:
#    print attr


# In[19]:

usr_attribute="hru_id"
usr_values=None
#usr_values = pyGDP.getValues(shapefile, usr_attribute)
#for v in values:
#    print v


# In[7]:

# Set our datasetURI
#dataSetURI = 'dods://cida.usgs.gov/thredds/dodsC/prism'
dataSetURI = 'http://thredds.daac.ornl.gov/thredds/dodsC/daymet-agg/daymet-agg.ncml'
# Get the available data types associated with the dataset
datatypes = pyGDP.getDataType(dataSetURI)
for dt in datatypes:
	print dt


# In[9]:

# Set the dataType. Note that leaving dataType out below will select all.
# Get available time range on the dataset
dataType='prcp'
timeRange = pyGDP.getTimeRange(dataSetURI, dataType)
for t in timeRange:
    print t


# In[14]:

# Submit job to pyGDP
# result is area-weighted mean in CSV for given datatype
path = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, dataType, timeRange[0], timeRange[1], usr_attribute, usr_values, gmlIDs=None, verbose=True)
print path
import shutil
shutil.copy2(path, names+'_'+dataType)


# In[20]:

datatype="tmax"
path = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, dataType, timeRange[0], timeRange[1], usr_attribute, usr_values, gmlIDs=None, verbose=True)
print path
import shutil
shutil.copy2(path, names+'_'+dataType)


# In[17]:

datatype="tmin"
path = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, dataType, timeRange[0], timeRange[1], usr_attribute, usr_values, gmlIDs=None, verbose=True)
print path
import shutil
shutil.copy2(path, names+'_'+dataType)


# In[ ]:



