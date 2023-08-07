import bpy

class HSP_PT_Panel(bpy.types.Panel):
    bl_idname = "HSP_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Hesperia"
    bl_label = "Hesperia"

    #string_filepath: bpy.props.StringProperty( name='Export To File', description="Define path for exported files", default="", subtype = "FILE_PATH", maxlen=1024)
    #bool_type_binary: bpy.props.BoolProperty(name="Toggle Option", default=False)

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw(self, context):
        scene = context.scene
        HSP = scene.HSP

        layout = self.layout

        box = layout.box()
        box.label(text="Hesperia Points Export")
        row = layout.row()
        row.prop(HSP, 'string_filepath')
        row = layout.row()
        row.prop(HSP, 'bool_type_binary')
        row = layout.row(align=True)
        row = box.row()
        row.operator("hsp.exporter")

class HSPProperties(bpy.types.PropertyGroup):
    string_filepath: bpy.props.StringProperty( name='Export To File', description="Define path for exported files", default="", subtype = "FILE_PATH", maxlen=1024)
    curve_filepath: bpy.props.StringProperty( name='Export To File', description="Define path for exported files", default="", subtype = "FILE_PATH", maxlen=1024)
    bool_type_binary: bpy.props.BoolProperty(name="Export As Binary File", default=False)
    curvepath_type_binary: bpy.props.BoolProperty(name="Export As Binary File", default=False)