"""Create random smooth 3D objects by applying a modifier
to a UV sphere, and saves each object so it can be
loaded later.

katherine.storrs@gmail.com"""

import bpy
from math import radians
import random

def create_object(filename):
    """
    filename = absolute path of file name to save this object as
    """

    # create empty object to hold texture coords
    empty = bpy.ops.object.empty_add(location=(0,0,0))

    # create primitive object geometry
    bpy.ops.mesh.primitive_ico_sphere_add()
    so = bpy.context.active_object # selected object(so) is active object

    # modifiers
    mod_subsurf=so.modifiers.new("My Modif","SUBSURF")
    mod_subsurf.levels = 6  #or random.randint(1,5) #is easier faster

    # smooth the object
    bpy.ops.object.shade_smooth()

    """Set up displacement modifier for Shape Deformation"""
    mod_disp = so.modifiers.new("My Displacement","DISPLACE")
    # link texture coords to empty object
    mod_disp.texture_coords = "OBJECT"
    mod_disp.texture_coords_object = bpy.data.objects["Empty"]
    bpy.data.objects["Empty"].location[0] = random.uniform(-10.0,10.0)
    bpy.data.objects["Empty"].location[1] = random.uniform(-10.0,10.0)
    bpy.data.objects["Empty"].location[2] = random.uniform(-10.0,10.0)

    """Specify parameters for this noise type
    (each type is a hand-picked combination of noise basis
    and param values)
    Comment out all but the type you want to generate
    at the moment:"""
#    # type 1
#    new_text = bpy.data.textures.new("My Texture","CLOUDS")
#    new_text.noise_basis = "IMPROVED_PERLIN"
#    new_text.noise_scale = 1.5
#    new_text.noise_depth = 1.0
#    mod_disp.strength = 2.0

#    # type 2
#    new_text = bpy.data.textures.new("My Texture","MUSGRAVE")
#    new_text.noise_basis = "IMPROVED_PERLIN"
#    new_text.noise_scale = 1.0
#    mod_disp.strength = 1.0
#
#    # type 3
#    new_text = bpy.data.textures.new("My Texture","MARBLE")
#    new_text.noise_basis = "IMPROVED_PERLIN"
#    new_text.marble_type = "SHARP"
#    new_text.noise_scale = 1.5
#    new_text.noise_depth = 1.0
#    new_text.turbulence = 10.0
#    mod_disp.strength = 0.3
##
#    # type 4
#    new_text = bpy.data.textures.new("My Texture","VORONOI")
#    new_text.noise_scale = 1.0
#    mod_disp.strength = 1.0
#
#    # type 5
#    new_text = bpy.data.textures.new("My Texture","CLOUDS")
#    new_text.noise_basis = "VORONOI_F2_F1"
#    new_text.noise_scale = 1.0
#    new_text.noise_depth = 0.0
#    mod_disp.strength = 0.3
#
#    # type 6
#    new_text = bpy.data.textures.new("My Texture","MUSGRAVE")
#    new_text.noise_basis = "VORONOI_F1"
#    new_text.musgrave_type = "RIDGED_MULTIFRACTAL"
#    new_text.noise_scale = 1.3
#    new_text.lacunarity = 1.0
#    new_text.intensity = 0.4
#    mod_disp.strength = 0.1

    # assign this texture to displacement modifier
    mod_disp.texture = new_text

    """Save object geometry"""
    bpy.ops.export_scene.obj(filepath=filename, use_selection=True)


for x in range(0,5):
    filename = "D:\\path\\to\\project\\geometries\\mesh"+str(x).zfill(3)
    create_object(filename)
    # tidy up
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
