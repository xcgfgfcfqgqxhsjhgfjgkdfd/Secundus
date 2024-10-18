# -*- coding: utf-8 -*-

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "DoR"
        self.alias = "Can be use to make a selection, combied with a buffer and a clip"

        # List of tool classes associated with this toolbox
        self.tools = [Limons_plateaux]


class Limons_plateaux(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Limons des plateaux"
        self.category ="data analysis combined tools"
        self.description = "Select by location-select by attribute (x2)-select by location"
        self.canRunInBackground = False

    def getParameterInfo(self):
        #Define parameter definitions

        gdb_output = arcpy.Parameter(
        displayName="GDB de travail",
        name="gdb_output",
        datatype="DELayer",
        parameterType="Derived",
        direction="Input")

        communes = arcpy.Parameter(
        displayName="Fichier des communes",
        name="communes",
        datatype="GPFeatureLayer",
        parameterType="Required",
        direction="Input")
        communes.filter.list = ["Point"]

        geol = arcpy.Parameter(
        displayName="Fichier de géologie",
        name="geol",
        datatype="GPFeatureLayer",
        parameterType="Required",
        direction="Input")
        geol.filter.list = ["Polygon"]
        
        output = arcpy.Parameter(
        displayName="Fichier en sortie",
        name="output",
        datatype="DEWorkspace",
        parameterType="Derived",
        direction="Output")

        parameters = [gdb_output, communes, geol, output]
        
        return parameters

    def isLicensed(self): #optional
        return True

    def updateParameters(self, parameters): #optional
        return

    def updateMessages(self, parameters): #optional
        return

    def execute(self, parameters, messages):
        gdb_output = parameters[0].valueAsText
        communes  = parameters[1].valueAsText
        geol   = parameters[2].valueAsText
        output  = parameters[3].valueAsText

          # Extraction 1 : communes du 60
        arcpy.MakeFeatureLayer_management(communes, "60")
        arcpy.management.SelectLayerByLocation("60", "HAVE_THEIR_CENTER_IN", geol)
        arcpy.management.CopyFeatures("60", "communes_60")

        # Extraction 2 : communes > 1000 habitants
        arcpy.MakeFeatureLayer_management("communes_60", "loor")
        arcpy.management.SelectLayerByAttribute("loor", "NEW_SELECTION", "POPU > 1000")
        arcpy.management.CopyFeatures("loor", "communes_1k_hab")

        # Extraction 3 : extraire les limons des plateaux
        arcpy.MakeFeatureLayer_management(geol, "ge")
        arcpy.management.SelectLayerByAttribute("ge", "NEW_SELECTION", "DESCRIPTIO = 'Limons des plateaux'")
        arcpy.management.CopyFeatures("ge", "limons_plateaux")

        # Extraction 4 : extraire les alluvions
        arcpy.MakeFeatureLayer_management(geol, "a")
        arcpy.management.SelectLayerByAttribute("a", "NEW_SELECTION", "DESCRIPTIO LIKE '%Alluvions%'")
        arcpy.management.CopyFeatures("a", "Alluvions")
    
        # Extraction 5 : extraire le réseau hydro
        arcpy.MakeFeatureLayer_management(geol, "b")
        arcpy.management.SelectLayerByAttribute("b", "NEW_SELECTION", "DESCRIPTIO LIKE '%Hydro%'")
        arcpy.management.CopyFeatures("b", "hydro")
    
          # Extraction 6 : extraire le reste
        arcpy.MakeFeatureLayer_management(geol, "c")
        arcpy.management.SelectLayerByAttribute("c", "NEW_SELECTION", "DESCRIPTIO = 'Limons des plateaux' Or DESCRIPTIO LIKE '%Hydro%' Or DESCRIPTIO LIKE '%Alluvions%'", "INVERT")
        arcpy.management.CopyFeatures("c", "Reste")

        # Croisement limon - communes
        arcpy.MakeFeatureLayer_management("communes_1k_hab", "ye")
        arcpy.management.SelectLayerByLocation("ye", "HAVE_THEIR_CENTER_IN", "limons_plateaux")
        arcpy.management.CopyFeatures("ye", output)
