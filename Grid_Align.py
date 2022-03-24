import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty, FloatProperty, FloatVectorProperty

class Align_Grid_Vars(bpy.types.PropertyGroup):
    column : bpy.props.IntProperty(name="Column", default=2, min=0, soft_max=10, description="Columns to align on grid")
    space : bpy.props.FloatVectorProperty(name="Space", default=(0.0, 0.0, 0.0), description="Space in between objects")
    

class ALIGN_OT_Align_Grid(bpy.types.Operator):
    bl_idname = 'wm.align_ot_align_grid'
    bl_label = 'Align Grid'
    bl_description = 'Align rotation of active object to other selected objects.'
    bl_options = {'REGISTER', 'UNDO'}

    column : IntProperty(default=1, min=1)
    space : FloatVectorProperty()
        
    def execute(self, context):
        scene = context.scene
        # align_grid_vars = scene.align_grid_vars

        objs = []

        for ob in bpy.context.selected_objects:
            objs.append(ob)

        idx = 0
        y = 0
        x = 0
        z = 0
        
        while idx < len(objs):
        #    dimension = objs[idx].bound_box.data.dimensions

            objs[idx].location[0] = 0 + y * self.space[0]
            objs[idx].location[1] = 0 + x * self.space[1]
            objs[idx].location[2] = 0 + z * self.space[2]
            
            y = 0 + y + 1
            if y > self.column-1:
                y = 0
                x = 0 + x + 1
                z = 0 + z + 1
                
            idx = idx + 1

        return {'FINISHED'}
    

class ALIGN_PT_Align_Grid_Panel(bpy.types.Panel):
    bl_idname = 'ALIGN_PT_align_grid_panel'
    bl_category = 'Align Grid Panel'
    bl_label = 'Align Grid Tools'
    bl_context = "objectmode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def draw(self, context):
        scene = context.scene
        align_grid_vars = scene.align_grid_vars
       
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column(align=True)
        row = col.row(align=True)

        if len(bpy.context.selected_objects) <= 0:
            col.label(text="Select objects to align")
        else:
            # col.prop(align_grid_vars, 'column')
            # col.prop(align_grid_vars, 'space')
            col.operator('wm.align_ot_align_grid')

        # Not enough objects selected
        # if len(bpy.context.selected_objects) > 0:
        #     row = layout.column(align=True)
        #     row.label(text='No objects selected')
        #     row.label(text='Select 2 objects')
        #     row.label(text='then select a 3rd object to align')

        # Active object is outside operator range
        # elif len(bpy.context.selected_objects) == 2:
        #     row = layout.column(align=True)
        #     row.label(text='Select object to align')

        # Proper amount of objects selected for operator
        # elif len(bpy.context.selected_objects) == 3 and bpy.context.view_layer.objects.active in bpy.context.selected_objects:
        #     row = layout.row(align=True)            
        #     row.operator('wm.align_ot_align_active_to_selected', icon='OBJECT_ORIGIN')

        # Active object is outside operator range
        # elif len(bpy.context.selected_objects) == 3 and not bpy.context.view_layer.objects.active in bpy.context.selected_objects:
        #     row = layout.column(align=True)
        #     row.label(text='Active object not selected')
        #     row.label(text='Select object to align')

        # Too many objects selected
        # elif len(bpy.context.selected_objects) > 3:
        #     row = layout.column(align=True)
        #     row.label(text='Too many objects selected')
        #     row.label(text='Select 2 objects')
        #     row.label(text='then select a 3rd object to align')

        # Axis Selector
        # if len(bpy.context.selected_objects) == 3 and bpy.context.view_layer.objects.active in bpy.context.selected_objects:
        #     col = layout.column(align=True)
        #     col.prop(rot_vars, 'side_axis')
        #     col.prop(rot_vars, 'up_axis')

        #     if rot_vars.up_axis == rot_vars.side_axis:
        #         row = layout.column(align=True)
        #         row.label(text='Both axis cant be the same')
        
