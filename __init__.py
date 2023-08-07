# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Hesperia",
    "author" : "CNISIDIS",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning":"WIP - ",
    "category" : "Tools"
}

import bpy
from . OP import HSP_OT_ExporterOperator, HSP_OT_UDPOperator
from . UI import HSP_PT_Panel, HSPProperties

classes = ( HSP_OT_ExporterOperator, HSP_OT_UDPOperator, HSP_PT_Panel, HSPProperties)


register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
    register_classes()
    bpy.types.Scene.HSP =  bpy.props.PointerProperty(type=HSPProperties)

def unregister():
    unregister_classes()
    del bpy.types.Scene.HSP
