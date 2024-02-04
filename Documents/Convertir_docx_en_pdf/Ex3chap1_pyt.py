# -*- coding: utf-8 -*-

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "DoR"
        self.alias = "Can be use to make a selection, combied with a buffer and a clip"

        # List of tool classes associated with this toolbox
        self.tools = [Route_geomorpho]


class Route_geomorpho(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "SelBuffClip"
        self.category ="data analysis combined tools"
        self.description = "Can be use to make a selection, combied with a buffer and a clip"
        self.canRunInBackground = False

    def getParameterInfo(self):
        #Define parameter definitions

        gdb_output = arcpy.Parameter(
        displayName="GDB de travail",
        name="gdb_output",
        datatype="DEWorkspace",
        parameterType="Derived",
        direction="Input")

        geomorpho = arcpy.Parameter(
        displayName="Fichier de géomorphologie",
        name="geomorpho",
        datatype="GPFeatureLayer",
        parameterType="Required",
        direction="Input")
        geomorpho.filter.list = ["Polygon"]

        routes = arcpy.Parameter(
        displayName="Fichier de routes",
        name="routes",
        datatype="GPFeatureLayer",
        parameterType="Required",
        direction="Input")
        routes.filter.list = ["line"]

        buffer_value = arcpy.Parameter(
        displayName="Rayon du du buffer",
        name="Buffer value",
        datatype="GPString",
        parameterType="Required",
        direction="Input")

        buffer_unit = arcpy.Parameter(
        displayName="Unité du buffer",
        name="Buffer unit",
        datatype="GPString",
        parameterType="Required",
        direction="Input")
        buffer_unit.filter.type="ValueList"
        buffer_unit.filter.list=["kilometers","Meters","Miles","DecimalDegrees"]
        buffer_unit.value="Meters"
        
        output = arcpy.Parameter(
        displayName="Fichier en sortie",
        name="output",
        datatype="DEWorkspace",
        parameterType="Required",
        direction="Output")

        parameters = [gdb_output, geomorpho, routes, buffer_value, buffer_unit, output]
        
        return parameters

    def isLicensed(self): #optional
        return True

    def updateParameters(self, parameters): #optional
        return

    def updateMessages(self, parameters): #optional
        return

    def execute(self, parameters, messages):
        gdb_output = parameters[0].valueAsText
        geomorpho  = parameters[1].valueAsText
        routes   = parameters[2].valueAsText
        buffer_value  = parameters[3].valueAsText
        buffer_unit  = parameters[4].valueAsText
        output  = parameters[5].valueAsText

        #Select by attriubte
        arcpy.MakeFeatureLayer_management(geomorpho, "lyr")
        where_clause="activite = 'actif'"
        arcpy.SelectLayerByAttribute_management('lyr', 'NEW_SELECTION', where_clause)
        output_actif = 'processus_actif'
        arcpy.CopyFeatures_management('lyr', output_actif)

        distance = '{0} {1}'.format(buffer_value,buffer_unit)
        output_buff = 'buff_layer'

        arcpy.analysis.Buffer(output_actif, output_buff, distance)

        arcpy.analysis.Clip(routes, output_buff, output)

