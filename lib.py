import bpy, time
from .common import *
from bpy.app.handlers import persistent

# Node tree names
OVERLAY_NORMAL = '~TL Overlay Normal'
STRAIGHT_OVER = '~TL Straight Over Mix'
STRAIGHT_OVER_HACK = '~TL Straight Over Hack'
CHECK_INPUT_NORMAL = '~TL Check Input Normal'
FLIP_BACKFACE_NORMAL = '~TL Flip Backface Normal'

NEIGHBOR_UV ='~TL Neighbor UV'
NEIGHBOR_UV_TANGENT ='~TL Neighbor UV (Tangent)'
NEIGHBOR_UV_OBJECT ='~TL Neighbor UV (Object)'
NEIGHBOR_UV_CAMERA ='~TL Neighbor UV (Camera)'
NEIGHBOR_UV_OTHER_UV ='~TL Neighbor UV (Other UV)'
NEIGHBOR_FAKE ='~TL Fake Neighbor'
FINE_BUMP ='~TL Fine Bump'
CURVED_FINE_BUMP = '~TL Curved Fine Bump'
FLIP_CURVED_FINE_BUMP = '~TL Flip Curved Fine Bump'

VECTOR_MIX ='~TL Vector Mix'
INVERTED_MULTIPLIER ='~TL Inverted Multiplier'
INTENSITY_MULTIPLIER ='~TL Intensity Multiplier'
GET_BITANGENT ='~TL Get Bitangent'

# Modifier tree names
MOD_RGB2INT = '~TL Mod RGB To Intensity'
MOD_INT2RGB = '~TL Mod Intensity To RGB'
MOD_OVERRIDE_COLOR = '~TL Mod Override Color'
MOD_INVERT = '~TL Mod Invert'
MOD_INVERT_VALUE = '~TL Mod Invert Value'
MOD_MULTIPLIER = '~TL Mod Multiplier'
MOD_MULTIPLIER_VALUE = '~TL Mod Multiplier Value'
MOD_INTENSITY_HARDNESS = '~TL Mod Intensity Hardness'

tree_lib_names = {
        OVERLAY_NORMAL,
        STRAIGHT_OVER,
        CHECK_INPUT_NORMAL,
        FLIP_BACKFACE_NORMAL,

        MOD_RGB2INT,
        MOD_INVERT,
        MOD_INVERT_VALUE,
        MOD_MULTIPLIER,
        MOD_MULTIPLIER_VALUE,
        }

channel_custom_icon_dict = {
        'RGB' : 'rgb_channel',
        'VALUE' : 'value_channel',
        'NORMAL' : 'vector_channel',
        }

channel_icon_dict = {
        'RGB' : 'SPACE2',
        'VALUE' : 'SPACE3',
        'NORMAL' : 'KEYTYPE_BREAKDOWN_VEC',
        }

def load_custom_icons():
    # Custom Icon
    if not hasattr(bpy.utils, 'previews'): return
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    filepath = get_addon_filepath() + 'icons' + os.sep
    custom_icons.load('asterisk', filepath + 'asterisk_icon.png', 'IMAGE')

    custom_icons.load('channels', filepath + 'channels_icon.png', 'IMAGE')
    custom_icons.load('rgb_channel', filepath + 'rgb_channel_icon.png', 'IMAGE')
    custom_icons.load('value_channel', filepath + 'value_channel_icon.png', 'IMAGE')
    custom_icons.load('vector_channel', filepath + 'vector_channel_icon.png', 'IMAGE')

    custom_icons.load('add_modifier', filepath + 'add_modifier_icon.png', 'IMAGE')
    custom_icons.load('add_mask', filepath + 'add_mask_icon.png', 'IMAGE')

    custom_icons.load('collapsed_texture', filepath + 'collapsed_texture_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_texture', filepath + 'uncollapsed_texture_icon.png', 'IMAGE')
    custom_icons.load('collapsed_image', filepath + 'collapsed_image_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_image', filepath + 'uncollapsed_image_icon.png', 'IMAGE')
    custom_icons.load('collapsed_modifier', filepath + 'collapsed_modifier_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_modifier', filepath + 'uncollapsed_modifier_icon.png', 'IMAGE')
    custom_icons.load('collapsed_input', filepath + 'collapsed_input_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_input', filepath + 'uncollapsed_input_icon.png', 'IMAGE')
    custom_icons.load('collapsed_uv', filepath + 'collapsed_uv_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_uv', filepath + 'uncollapsed_uv_icon.png', 'IMAGE')
    custom_icons.load('collapsed_mask', filepath + 'collapsed_mask_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_mask', filepath + 'uncollapsed_mask_icon.png', 'IMAGE')
    custom_icons.load('collapsed_vcol', filepath + 'collapsed_vcol_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_vcol', filepath + 'uncollapsed_vcol_icon.png', 'IMAGE')

    custom_icons.load('collapsed_channels', filepath + 'collapsed_channels_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_channels', filepath + 'uncollapsed_channels_icon.png', 'IMAGE')

    custom_icons.load('collapsed_rgb_channel', filepath + 'collapsed_rgb_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_rgb_channel', filepath + 'uncollapsed_rgb_icon.png', 'IMAGE')
    custom_icons.load('collapsed_value_channel', filepath + 'collapsed_value_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_value_channel', filepath + 'uncollapsed_value_icon.png', 'IMAGE')
    custom_icons.load('collapsed_vector_channel', filepath + 'collapsed_vector_icon.png', 'IMAGE')
    custom_icons.load('uncollapsed_vector_channel', filepath + 'uncollapsed_vector_icon.png', 'IMAGE')

def get_node_tree_lib(name):
    # Node groups necessary are in nodegroups_lib.blend
    filepath = get_addon_filepath() + "lib.blend"

    with bpy.data.libraries.load(filepath) as (data_from, data_to):

        # Load node groups
        exist_groups = [ng.name for ng in bpy.data.node_groups]
        for ng in data_from.node_groups:
            if ng == name and ng not in exist_groups:
                data_to.node_groups.append(ng)
                break

    return bpy.data.node_groups.get(name)

def get_neighbor_uv_tree(texcoord_type, different_uv=False):
    if texcoord_type == 'UV':
        if different_uv: return get_node_tree_lib(NEIGHBOR_UV_OTHER_UV)
        return get_node_tree_lib(NEIGHBOR_UV_TANGENT)
    if texcoord_type in {'Generated', 'Normal', 'Object'}:
        return get_node_tree_lib(NEIGHBOR_UV_OBJECT)
    if texcoord_type in {'Camera', 'Window', 'Reflection'}: 
        return get_node_tree_lib(NEIGHBOR_UV_CAMERA)

def new_intensity_multiplier_node(tree, obj, prop, sharpness=1.0, label=''):
    if label == '': label = 'Intensity Multiplier'
    im = new_node(tree, obj, prop, 'ShaderNodeGroup', label)
    im.node_tree = get_node_tree_lib(INTENSITY_MULTIPLIER)
    im.inputs[1].default_value = sharpness
    im.inputs['Sharpen'].default_value = 1.0

    if BLENDER_28_GROUP_INPUT_HACK:
        duplicate_lib_node_tree(im)

    m = re.match(r'tl\.textures\[(\d+)\]\.channels\[(\d+)\]', obj.path_from_id())
    if m:
        tl = obj.id_data.tl
        root_ch = tl.channels[int(m.group(2))]
        print(root_ch.name, prop)

    return im

#@persistent
#def load_libraries(scene):
#    # Node groups necessary are in nodegroups_lib.blend
#    filepath = get_addon_filepath() + "lib.blend"
#
#    with bpy.data.libraries.load(filepath) as (data_from, data_to):
#
#        # Load node groups
#        exist_groups = [ng.name for ng in bpy.data.node_groups]
#        for ng in data_from.node_groups:
#            if ng not in exist_groups:
#                data_to.node_groups.append(ng)

@persistent
def update_node_tree_libs(name):
    T = time.time()

    filepath = get_addon_filepath() + "lib.blend"

    if bpy.data.filepath == filepath: return

    trees = []
    tree_names = []
    exist_groups = [ng.name for ng in bpy.data.node_groups if ng.name in tree_lib_names]

    if not exist_groups: return

    # Load node groups
    with bpy.data.libraries.load(filepath) as (data_from, data_to):
        for ng in data_from.node_groups:
            if ng in exist_groups:
                tree = bpy.data.node_groups.get(ng)
                tree.name += '__OLD'
                trees.append(tree)
                tree_names.append(ng)
                data_to.node_groups.append(ng)

    for i, name in enumerate(tree_names):
        update = False

        cur_tree = trees[i]
        cur_ver = cur_tree.nodes.get('version')
        lib_tree = bpy.data.node_groups.get(name)
        lib_ver = lib_tree.nodes.get('version')

        # Check lib tree version
        if cur_ver:
            cur_ver = float(cur_ver.label)

        if lib_ver:
            lib_ver = float(lib_ver.label)

            # Update tree if current version isn't found or older than lib version
            if not cur_ver or (cur_ver and lib_ver > cur_ver):
                update = True

        if update:
            # Search for old tree usages
            for mat in bpy.data.materials:
                if not mat.node_tree: continue
                for node in mat.node_tree.nodes:
                    if node.type == 'GROUP' and node.node_tree == cur_tree:
                        node.node_tree = lib_tree
            for group in bpy.data.node_groups:
                for node in group.nodes:
                    if node.type == 'GROUP' and node.node_tree == cur_tree:
                        node.node_tree = lib_tree

            # Remove old tree
            bpy.data.node_groups.remove(cur_tree)

            print('INFO: Node group', name, 'is updated to version', str(lib_ver) + '!')

        else:
            # Remove loaded lib tree
            bpy.data.node_groups.remove(lib_tree)

            # Bring back original tree name
            cur_tree.name = cur_tree.name[:-5]

    print('INFO: Node group libraries are checked at', '{:0.2f}'.format((time.time() - T) * 1000), 'ms!')

def register():
    load_custom_icons()
    #bpy.app.handlers.load_post.append(load_libraries)
    bpy.app.handlers.load_post.append(update_node_tree_libs)

def unregister():
    global custom_icons
    if hasattr(bpy.utils, 'previews'):
        bpy.utils.previews.remove(custom_icons)
    #bpy.app.handlers.load_post.remove(load_libraries)
    bpy.app.handlers.load_post.remove(update_node_tree_libs)
