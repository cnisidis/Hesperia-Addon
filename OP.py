import bpy
import sys



class Hesperia_OT_UDPOperator(bpy.types.Operator):
    bl_idname = "Hesperia.udp"
    bl_label = "UDP Receiver"


class Hesperia_OT_ExporterOperator(bpy.types.Operator):
    bl_idname = "Hesperia.exporter"
    bl_label = "Export"


    def __init__(self) -> None:
        super().__init__()
        pass

    def execute(self, context):
        pass

