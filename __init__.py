bl_info = {
    "name" : "Hesperia",
    "author": "cnisidis http://nisidis.com",
    "description" : "UDP bridge for vvvv and Blender - Preview Engine for Hesperos",
    "blender" : (3, 00, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
     "warning":"WIP - ",
    "support": "TESTING",
    
    "category": "Tools"
}

import bpy
#from . OP import Hesperia_OT_UDPOperator, Hesperia_OT_ExporterOperator

classes = ()
register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)


def register():
    register_classes()
    #bpy.types.Scene.BMD =  bpy.props.PointerProperty(type=BMDProperties)

def unregister():
    unregister_classes()
    #del bpy.types.Scene.BMD
