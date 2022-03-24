import bpy, sys, os

from . Grid_Align import *

# from bpy_extras.io_utils import ImportHelper
# from bpy.types import Operator, Header
# from bpy.props import PointerProperty


# GNU GENERAL PUBLIC LICENSE
# Version 3, 29 June 2007

# Thank you all that download, suggest, and request features
# As well as the whole Blender community. You're all epic :)


bl_info = {
    "name": "Grid_Align",
    "author": "Johnathan Mueller",
    "descrtion": "This script allows you to align any object along an axis between the centers of two other objects.",
    "blender": (2, 80, 0),
    "version": (0, 1, 1),
    "location": "View3D (ObjectMode) > Sidebar > Edit Tab",
    "warning": "",
    "category": "Object"
}


classes = (
    # Properties
    Align_Grid_Vars,

    # Panels
    ALIGN_OT_Align_Grid,

    # Operators
    ALIGN_PT_Align_Grid_Panel,
)


def register():
    for rsclass in classes:
        bpy.utils.register_class(rsclass)
        bpy.types.Scene.align_grid_vars = bpy.props.PointerProperty(type=Align_Grid_Vars)


def unregister():
    for rsclass in classes:
        bpy.utils.unregister_class(rsclass)


if __name__ == "__main__":
    register()

