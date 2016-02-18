#2/18/2016
# A.Bock
# creates shapefile from parameter file
# import modules
import sys, arcpy, os

# set directoriesr
thisdir = os.getcwd()
# select parameter file
paramFile="Params/8.6_Seg1046/r11.params"
region_pre=paramFile.split("/")
segID=region_pre[1].split("_")[1]
region=region_pre[2].split(".")[0]
# open parameter file and read lines
params = open(paramFile,"r")
plines = params.readlines()

# create loop to get HRU IDs for region
hruList=[]
count=0
for lines in plines:
    items = lines.split()
    #print items
    if items[0]=="parent_hru":
        count=1
    if items[0]=="####":
        count=0
    if count > 0:
        count=count+1
        if count > 6:
            hruList.append(items[0])

# open the region shapefile
hru = "D:\\abock\\Water_Balance\\Step1_CLIMATE_DATA\\Tiles\\"+region+"\\"+region+"\\nhru.shp"
# make a feature layer
arcpy.MakeFeatureLayer_management(hru,"hruLYR")
# create query to select HRUS from parameter file from regio nhru shapefile
current_var_float=[int(x) for x in hruList]
qry = '"hru_id" IN'+str(tuple(current_var_float))
arcpy.SelectLayerByAttribute_management('hruLYR',"NEW_SELECTION",qry)
# create shapefile for parameter file
arcpy.FeatureClassToFeatureClass_conversion('hruLYR',".","Shapes\\"+region_pre[1]+"_"+segID+".shp")
arcpy.Delete_management("hruLYR")