import arcpy
def ScriptTool(geomorpho, route, buffer_v, buffer_u, output):
    # Script execution code goes here
        arcpy.MakeFeatureLayer_management(geomorpho, "lyr")
        arcpy.SelectLayerByAttribute_management('lyr', 'NEW_SELECTION', "activite = 'actif'")
        output_actif = 'processus_actif'
        arcpy.CopyFeatures_management('lyr', output_actif)
        distance = '{0} {1}'.format(buffer_v,buffer_u)
        output_buff = 'buff_layer'
        output_buff1 = 'buf_dissolve'
        arcpy.analysis.Buffer(output_actif, output_buff, distance)
        arcpy.analysis.Clip(route, output_buff, output)
        
        return
# This is used to execute code if the file was run but not imported
if __name__ == '__main__':
    # Tool parameter accessed with GetParameter or GetParameterAsText
    geomorpho = arcpy.GetParameterAsText(0)
    route = arcpy.GetParameterAsText(1)
    buffer_v = arcpy.GetParameterAsText(2)
    buffer_u = arcpy.GetParameterAsText(3)
    output = arcpy.GetParameterAsText(4)
    
    ScriptTool(geomorpho, route, buffer_v, buffer_u, output)
    
    # Update derived parameter values using arcpy.SetParameter() or arcpy.SetParameterAsText()


