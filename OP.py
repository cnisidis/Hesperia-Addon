import bpy
import sys



class HSP_OT_UDPOperator(bpy.types.Operator):
    bl_idname = "hsp.udp"
    bl_label = "UDP Receiver"

    def __init__(self) -> None:
        super().__init__()
        
    def execute(self, context):
        pass   

    


class HSP_OT_ExporterOperator(bpy.types.Operator):
    bl_idname = "hsp.exporter"
    bl_label = "Export"


    def __init__(self) -> None:
        super().__init__()
        pass

    def execute(self, context):
        pass

