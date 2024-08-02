import bpy
from .common import *

def register_module(*modules: list):
    for module in modules:
        if bpy.app.version < (4, 0, 0):
            bpy.app.translations.register(module.__name__, langs)
        else:
            langs['zh_HANS'] = langs['zh_CN']
            bpy.app.translations.register(module.__name__, langs)

def unregister_module(*modules: list):
    for module in modules:
        bpy.app.translations.unregister(module.__name__)
        
langs = {
    'zh_CN': {
        ('*', 'Special node to manage painting layers for Cycles and Eevee materials'): 'ucup',
        ('*', 'Auto Save/Pack Images'): '自动保存/打包图像',
        ('*', 'Auto save/pack images when saving blend'): '当保存.blend文件时，自动保存/打包图像',
        ('*', 'Force All Images'): '所有图像',
        ('*', 'Only Dirty Images'): '仅限改动的图像',
        ('*', 'Preview Mode'): '预览模式',
        ('*', 'Layer Preview Mode Type'): '图层预览类型',
        ('*', 'Layer'): '图层 (Layer)',
        ('*', 'Channel'): '通道 (Channel)',
        ('*', ' Channel'): ' 通道 (Channel)',
        ('*', ' Channels'): ' 通道 (Channel)',
        ('*', 'Channel:'): '通道:',
        ('*', 'Background:'): '背景 (Background):',
        ('*', 'Source: '): '来源 (Source): ',
        ('*', 'Mask'): '遮罩 (Mask)',
        ('*', 'Masks'): '遮罩 (Mask)',
        ('*', 'Material: '): '材质: ',
        ('*', 'Object: '): '对象: ',
        ('*', get_addon_title() + ' About'): '关于 %s' % get_addon_title(),
        ('*', get_addon_title() + ' Special Menu'): '%s 操作' % get_addon_title(),
        ('Operator', 'Add new ' + get_addon_title() + ' Node'): '新建 %s 节点' % get_addon_title(),
        ('Operator', 'Add new ' + get_addon_title() + ' Channel'): '新建 %s 通道' % get_addon_title(),
        ('Operator', 'Remove ' + get_addon_title() + ' Channel'): '删除 %s 通道' % get_addon_title(),
        ('Operator', 'Move ' + get_addon_title() + ' Channel'): '移动 %s 通道' % get_addon_title(),
        ('Operator', 'Open Available Image'): '打开现有图像',
        ('Operator', 'Open Images to Single Layer'): '打开多个图像至单一图层',
        ('Operator', 'Layer Group'): '新建图层组',
        ('Operator', 'New Vertex Color'): '新建顶点色 (New Vertex Color)',
        ('Operator', 'Open Available Vertex Color'): '打开现有顶点色',
        ('Operator', 'Use Available Vertex Color'): '使用现有顶点色',
        ('Operator', 'New Vertex Color Mask'): '新建顶点色遮罩',
        ('Operator', 'Open Available Vertex Color as Mask'): '使用现有顶点色为遮罩',
        ('Operator', 'Color ID'): '颜色 ID',
        ('Operator', 'Color ID '): '颜色 ID',
        ('Operator', 'Backface'): '背面',
        ('Operator', 'New Image Mask'): '新建图像遮罩',
        ('Operator', 'Open Image as Mask'): '打开图像为遮罩',
        ('Operator', 'Open Available Image as Mask'): '使用现有图像为遮罩',
        ('*', 'Bake as Mask:'): '烘焙为遮罩:',
        ('*', 'Generated Mask:'): '生成式遮罩:',
        ('*', 'Image Mask:'): '图像遮罩:',
        ('*', 'Vertex Color Mask:'): '顶点色遮罩:',
        ('Operator', 'Vertex Color'): '顶点色 (Vertex Color)',
        ('Operator', 'Image'): '图像 (Image)',
        ('Operator', 'Group'): '组 (Group)',
        ('Operator', 'Solid Color'): '实色 (Solid Color)',
        ('Operator', 'Solid Color'): '实色 (Solid Color)',
        ('Operator', 'Solid Color w/ Image Mask'): '实色 / 图像遮罩',
        ('Operator', 'Solid Color w/ Vertex Color Mask'): '实色 / 顶点色遮罩',
        ('Operator', 'Solid Color w/ Color ID Mask'): '实色 / 颜色 ID 遮罩',
        ('Operator', 'Background w/ Image Mask'): '背景 / 图像遮罩',
        ('Operator', 'Background w/ Vertex Color Mask'): '背景 / 顶点色遮罩',
        ('Operator', 'Bake Channel to Vertex Color (Batch All Materials)'): '烘焙通道至顶点色 (批处理所有材质)',
        ('Operator', 'Bake Channel to Vertex Color'): '烘焙通道至顶点色',
        ('*', 'Include Alpha:'): '包含 Alpha:',
        ('*', 'Bake To Alpha:'): '烘焙至 Alpha:',
        ('*', 'Force First Index:'): '强制移动到首位:',
        ('Operator', 'Fix Unconnected Channel Output'): '修复未连接的通道输出!',
        ('Operator', 'Brick'): '砖块 (Brick)',
        ('Operator', 'Checker'): '棋盘格 (Checker)',
        ('Operator', 'Noise'): '噪音 (Noise)',
        ('Operator', 'Wave'): '波纹 (Wave)',
        ('Operator', 'Intensity to RGB'): '强度 转为RGB',
        ('*', 'Intensity to RGB'): '强度 转为RGB',
        ('Operator', 'RGB to Intensity'): 'RGB 转为强度',
        ('*', 'RGB to Intensity'): 'RGB 转为强度',
        ('Operator', 'Color Ramp'): '颜色渐变',
        ('*', 'Color Ramp'): '颜色渐变',
        ('Operator', 'RGB Curve'): '曲线',
        ('*', 'RGB Curve'): '曲线',
        ('Operator', 'Hue Saturation'): '色相与饱和度',
        ('*', 'Hue Saturation'): '色相与饱和度',
        ('Operator', 'Brightness Contrast'): '亮度与对比度',
        ('*', 'Brightness Contrast'): '亮度与对比度',
        ('Operator', 'Math'): '运算',
        ('*', 'Math'): '运算',
        ('Operator', 'Move Mask Up'): '向上移动遮罩',
        ('Operator', 'Move Mask Down'): '向下移动遮罩',
        ('Operator', 'Merge Mask Up'): '向上合并遮罩',
        ('Operator', 'Merge Mask Down'): '向下移动遮罩',
        ('Operator', 'Duplicate as Image'): '复制为图像',
        ('Operator', 'Remove Mask'): '删除遮罩',
        ('*', 'Enable Mask'): '启用遮罩',
        ('*', 'Layer Mask Menu'): '图层遮罩操作',
        ('Operator', 'Move Mask Up'): '向上移动遮罩',
        ('Operator', 'Merge Layer Up'): '向上合并图层',
        ('Operator', 'Merge Layer Down'): '向下合并图层',
        ('*', 'Need at least one layer channel enabled!'): '至少需要一个图层为启用',
        ('*', 'Both layer should be enabled!'): '两个图层都必须为启用',
        ('*', 'No neighbor found!'): '没有邻近层!',
        ('*', 'Cannot merge with layer with different parent!'): '不能与不同的父层合并!',
        ('*', 'Merge doesn\'t works with layer group!'): '不可合并于图层组',
        ('*', 'Both layer should be enabled!'): '两个图层都必须为启用!',
        ('*', 'This layer has no image!'): '该图层没有图像!',
        ('*', 'These two layers has different normal map type!'): '两个图层拥有不同的法线贴图类型!',
        ('*', 'Main Channel:'): '主通道:',
        ('*', 'Apply Modifiers:'): '应用修改器:',
        ('*', 'Apply Neighbor Modifiers:'): '应用邻近层修改器:',
        ('*', 'This kind of merge is not supported yet!'): '此类型暂不支持合并',
        ('*', 'Merge failed for some reason!'): '合并出现未知错误!',
        ('*', 'New Layer Menu'): '新建图层',
        ('*', 'New Layer Mask'): '新建图层遮罩',
        ('*', 'Layer Special Menu'): '图层操作',
        ('*', 'Add Modifier Menu'): '添加修改器',
        ('*', 'Active mask for editing or preview'): '激活用于修改或预览',
        ('*', 'Enable Layer Masks'): '启用图层遮罩',
        ('*', 'Enable Layer'): '启用图层',
        ('Operator', 'Save/Pack All'): '保存/打包所有',
        ('Operator', 'Invert Image'): '反转图像',
        ('Operator', 'Duplicate Layer'): '复制图层',
        ('Operator', 'Duplicate Blank Layer'): '复制空图层',
        ('Operator', 'Copy Layer'): '复制图层至剪贴板',
        ('Operator', 'Copy All Layers'): '复制所有图层至剪贴板',
        ('Operator', 'Paste Layer(s)'): '粘贴图层',
        ('Operator', 'Refill UDIM Tiles'): '重填 UDIM 板块',
        ('*', 'Clamp:'): '约束数值 (Use Clamp):',
        ('*', 'Affect Alpha:'): '影响 Alpha:',
        ('*', 'Color:'): '颜色:',
        ('*', 'Change Layer Type'): '更改图层类型',
        ('*', 'Base Value:'): '基础值 (Base Value):',
        ('*', 'Base Alpha:'): '基础 Alpha (Base Alpha):',
        ('*', 'Use Clamp:'): '约束数值 (Use Clamp):',
        ('*', 'Space:'): '颜色空间 (Space):',
        ('*', 'Color Data'): 'sRGB (Color Data)',
        ('*', 'Non-Color Data'): '线性 (Non-Color Data)',
        ('*', 'Non color won\'t converted to linear first before blending'): '在混合之前，非颜色数据不会先转换为线性 (Non color won\'t converted to linear first before blending)',
        ('*', 'Base Color:'): '基础颜色 (Base Color):',
        ('*', 'Specific Mask / Override'): '指定遮罩 / 覆盖',
        ('Operator', 'Bake All Channels'): '烘焙所有通道 (Bake All Channels)',
        ('Operator', 'Rename Tree'): '重命名 %s 节点组 (Rename Tree)' % get_addon_title(),
        ('Operator', 'Remove ' + get_addon_title() + ' Node'): '删除 %s 节点 (Remove %s Node)' % (get_addon_title(), get_addon_title()),
        ('Operator', 'Clean ' + get_addon_title() + ' Caches'): '清除 %s 缓存 (Clean %s Caches)' % (get_addon_title(), get_addon_title()),
        ('Operator', 'Duplicate Material and ' + get_addon_title() + ' nodes'): '制作材质和 %s 节点副本 (Duplicate Material and %s nodes)' % (get_addon_title(), get_addon_title()),
        ('*', 'Active Tree:'): '激活的 %s 节点组 (Active Tree)' % get_addon_title(),
        ('*', 'Input:'): '输入:',
        ('*', 'Blend:'): '混合方式:',
        ('*', 'Override:'): '覆盖:',
        ('*', 'Stats'): '统计:',
        ('*', 'Default New Image Size'): '默认图像尺寸',
        ('*', 'Image Atlas Size'): '纹理图集 (Atlas) 尺寸',
        ('*', 'HDR Image Atlas Size'): 'HDR图集 (Atlas) 尺寸',
        ('*', 'Use unique Image Atlas per ' + get_addon_title() + ' tree'): '每 %s 节点使用独特的纹理图集 (Atlas)' % get_addon_title(),
        ('*', 'Make Preview Mode use sRGB'): '预览模式使用sRGB',
        ('*', 'Use Image Preview/Thumbnail'): '图像使用缩略图而非图标显示',
        ('*', 'Show Experimental Features'): '显示实验性功能',
        ('*', 'Developer Mode'): '开发者模式',
        ('*', 'Samples:'): '采样:',
        ('*', 'Margin:'): '边距:',
        ('*', 'AA Level:'): '抗锯齿:',
        ('*', 'Bake Device:'): '烘焙设备:',
        ('Operator', 'Bake channels to Image'): '烘焙通道至图像',
        ('Operator', 'Unpack As Image'): '解包为外部图像',
        ('Operator', 'Convert to Image Atlas'): '转换为图像纹理集 (Atlas)',
        ('Operator', 'Convert All Images to Image Atlas'): '转换所有图像为图像纹理集 (Atlas)',
        ('*', 'Use FXAA'): '启用 FXAA',
        ('*', 'Use Denoise'): '启用降噪 (Denoise)',
        ('*', 'Force Bake all Polygons'): '强制烘焙所有多边形',
        ('*', 'Force bake all polygons, useful if material is not using direct polygon (ex: solidify material)'): '强制烘焙所有多边形，可用于当材质不使用直接多边形(例如: 实体化修改器)',
        ('*', 'Add Mask'): '添加遮罩',
        ('*', 'Name:'): '名称:',
        ('*', 'Mask Type:'): '遮罩类型:',
        ('*', 'White (Full Opacity)'): '白色 (不透明)',
        ('*', 'Black (Full Transparency)'): '黑色 (全透明)',
        ('*', 'Mask Width:'): '遮罩宽度',
        ('*', 'Mask Height:'): '遮罩高度',
        ('*', 'Mask Color:'): '遮罩基础颜色:',
        ('Operator', 'Toggle Eraser'): '切换橡皮擦',
        ('Operator', 'Disable Eraser'): '关闭橡皮擦',
        ('*', 'Use Baked'): '使用烘焙结果',
        ('*', 'Enable Baked Outside'): '创建烘焙节点至节点外部',
        ('*', 'Create baked texture nodes outside of main node\n(Can be useful for exporting material to other application)'): '在主节点之外创建烘焙节点(可用于导出到其他地方)',
        ('*', 'No active image'): '没有激活的图像',
        ('*', 'Active Image: '): '激活的图像: ',
        ('*', 'Shortcut on list:'): '在列表中显示:',
        ('*', 'Connect To:'): '连接至:',
        ('Operator', 'Fix Active Vcol Mismatch!'): '切换为当前顶点色!',
        ('*', 'Fill '): '填充 ',
        ('Operator', 'White'): '白色',
        ('Operator', 'Black'): '黑色',
        ('*', 'Fill selected polygon with vertex color'): '填充选定多边形顶点色',
        ('*', 'Fill selected polygon with vertex color with custom color'): '填充选定多边形自定义顶点色',
        ('*', 'Fill Color ID'): '填充颜色 ID',
        ('*', 'Number of Images: '): '图像数量: ',
        ('*', 'Number of Vertex Colors: '): '顶点色数量: ',
        ('*', 'Number of Generated Textures: '): '生成式贴图数量: ',
        ('*', 'Number of Color Ramps: '): '颜色渐变数量: ',
        ('*', 'Number of RGB Curves: '): 'RGB曲线数量: ',

    },
    'ar': {

        ('*', 'Special node to manage painting layers for Cycles and Eevee materials'): 'Cycles and Eevee materials ـﻟ ﻢﺳﺮﻟا تﺎﻘﺒﻃ ةرادإ ﻞﺟﻷ ﺔﺻﺎﺧ ةﺪﻘﻋ',
        ('*', 'Auto Save/Pack Images'): 'رﻮﺼﻟا مﺰﺣ/ﻲﺋﺎﻘﻠﺘﻟا ﻂﻔﺤﻟا',
        ('*', 'Auto save/pack images when saving blend'): 'ﺪﻨﻠﺑ ﻒﻠﻣ ﻂﻔﺣ ﺪﻨﻋ رﻮﺼﻟا مﺰﺣ/ﻲﺋﺎﻘﻠﺘﻟا ﻂﻔﺤﻟا',
        ('*', 'Force All Images'): 'رﻮﺼﻟا ﻊﻴﻤﺟ ضﺮﻓ',
        ('*', 'Only Dirty Images'): 'ﺔﻃﻮﻔﺤﻣ ﺮﻴﻐﻟا رﻮﺼﻟا ﻂﻘﻓ',
        ('*', 'Preview Mode'): 'ﺔﻨﻳﺎﻌﻤﻟا ﻊﺿو',
        ('*', 'Layer Preview Mode Type'): 'ﺔﻘﺒﻄﻟا ﺔﻨﻳﺎﻌﻣ ﻊﺿو',
        ('*', 'Layer'): 'ﺔﻘﺒﻃ',
        ('*', 'Channel'): 'ةﺎﻨﻗ',
        ('*', ' Channel'): ' ةﺎﻨﻗ',
        ('*', ' Channels'): ' تاﻮﻨﻗ',
        ('*', 'Channel:'): 'ةﺎﻨﻗ:',
        ('*', 'Background:'): 'ﺔﻴﻔﻠﺧ:',
        ('*', 'Source: '): 'رﺪﺼﻤﻟا:',
        ('*', 'Mask'): 'عﺎﻨﻗ',
        ('*', 'Masks'): 'ﺔﻌﻨﻗا',
        ('*', 'Material'): 'ﺔﻣﺎﺧ',
        ('*', 'Object: '): 'ضﺮﻏ: ',
        ('*', 'Bake as Mask:'): 'عﺎﻨﻘﻛ نﺰﺧ:',
        ('*', 'Generated Mask:'): 'عﺎﻨﻗ ﺪﻟو:',
        ('*', 'Image Mask:'): 'عﺎﻨﻘﻟا ةرﻮﺻ:',
        ('*', 'Vertex Color Mask:'): 'طﺎﻘﻨﻟا ﻦﻳﻮﻠﺗ عﺎﻨﻗ:',
        ('*', 'Include Alpha:'): 'ﺎﻔﻟأ ﻦﻴﻤﻀﺗ:',
        ('*', 'Bake To Alpha:'): 'ﺎﻔﻟأ ﻲﻓ نﺰﺧ:',
        ('*', 'Force First Index:'): 'لوﻷا سﺮﻬﻔﻟا رﺎﺒﺟإ:',
        ('*', 'Intensity to RGB'): 'ناﻮﻟأ ﻰﻟا ةﺪﺸﻟا ﻞﻳﻮﺤﺗ',
        ('*', 'RGB to Intensity'): 'ةﺪﺷ ﻰﻟا ناﻮﻟأ ﻞﻳﻮﺤﺗ',
        ('*', 'Color Ramp'): 'ناﻮﻟأ رﺪﺤﻨﻣ',
        ('*', 'RGB Curve'): 'RGB ﻰﻨﺤﻨﻣ',
        ('*', 'Hue Saturation'): 'نﻮﻠﻟا ﻊﺒﺸﺗ',
        ('*', 'Brightness Contrast'): 'ﻦﻳﺎﺒﺘﻟا و عﻮﻄﺴﻟا',
        ('*', 'Math'): 'بﺎﺴﺣ',
        ('*', 'Layer Mask Menu'): 'ﺔﻘﺒﻄﻟا عﺎﻨﻗ ﺔﻤﺋﺎﻗ',
        ('*', 'Enable Mask'): 'عﺎﻨﻘﻟا ﻞﻴﻌﻔﺗ',
        ('*', 'Need at least one layer channel enabled!'): '!ﻞﻴﻌﻔﺘﻠﻟ ﻞﻗﻻا ﻰﻠﻋ ةﺪﺣاو ةﺎﻨﻗ ﺔﻘﺒﻃ جﺎﺘﺤﺗ',
        ('*', 'Both layer should be enabled!'): '!ﻢﻬﻠﻴﻔﺗ ﻲﻐﺒﻨﻳ ﻦﻴﺘﻘﺒﻄﻟا ﻼﻛ',
        ('*', 'No neighbor found!'): '!ناﺮﻴﺟ ﻰﻠﻋ رﻮﺜﻌﻟا ﻢﺘﻳ ﻢﻟ',
        ('*', 'Cannot merge with layer with different parent!'): '!ﻒﻠﺘﺨﻣ با ﻦﻣ ﺔﻘﺒﻃ ﻊﻣ ﺞﻣد ﻦﻜﻤﻳ ﻻ',
        ('*', 'Both layer should be enabled!'): '!ﻦﻴﻠﻌﻔﻣ ﻲﻐﺒﻨﻳ ﻦﻴﺘﻘﺒﻄﻟا ﻼﻛ',
        ('*', 'This layer has no image!'): '!ةرﻮﺻ يﻮﺤﺗ ﻻ ﺔﻘﺒﻄﻟا هﺬﻫ',
        ('*', 'These two layers has different normal map type!'): '!ﻢﻃﺎﻨﻟا ﻦﻣ ﻦﻴﻔﻠﺘﺨﻣ ﻦﻴﻋﻮﻧ نﺎﻳﻮﺤﺗ ﻦﻴﺘﻘﺒﻄﻟا ﻦﻳﺬﻫ',
        ('*', 'This kind of merge is not supported yet!'): '!ﺎﻴﻟﺎﺣ مﻮﻋﺪﻣ ﺮﻴﻏ ﺞﻣﺪﻟا ﻦﻣ عﻮﻨﻟا اﺬﻫ',
        ('*', 'Merge failed for some reason!'): '!ﺎﻣ ٍﺐﺒﺴﻟ ﻞﺸﻓ ﺞﻣﺪﻟا',
        ('*', 'Main Channel:'): 'ﺔﻴﺳﺎﺳﻷا ةﺎﻨﻘﻟا:',
        ('*', 'Apply Modifiers:'): 'تاﺮﻴﻐﻤﻟا ﻖﻴﺒﻄﺗ:',
        ('*', 'Apply Neighbor Modifiers:'): 'ناﺮﻴﺠﻟا تاﺮﻴﻐﻣ ﻖﻴﺒﻄﺗ:',
        ('*', 'New Layer Menu'): 'ةﺪﻳﺪﺠﻟا ﺔﻘﺒﻄﻟا ﺔﻤﺋﺎﻗ',
        ('*', 'New Layer Mask'): 'ةﺪﻳﺪﺟ عﺎﻨﻗ ﺔﻘﺒﻃ',
        ('*', 'Layer Special Menu'): 'ﺔﻘﺒﻄﻠﻟ ةﺰﻴﻤﻣ ﺔﻤﺋﺎﻗ',
        ('*', 'Add Modifier Menu'): 'ﺮﻴﻐﻤﻟا ﺔﻓﺎﺿإ ﺔﻤﺋﺎﻗ',
        ('*', 'Active mask for editing or preview'): 'ﺔﻨﻳﺎﻌﻤﻟا وأ ﻞﻳﺪﻌﺘﻟا ﻞﺟﻷ ﻞﻌﻔﻤﻟا عﺎﻨﻘﻟا',
        ('*', 'Enable Layer Masks'): 'ﺔﻘﺒﻄﻟا عﺎﻨﻗ ﻞﻴﻌﻔﺗ',
        ('*', 'Enable Layer'): 'ﺔﻘﺒﻄﻟا ﻞﻴﻌﻔﺗ',
        ('*', 'Clamp:'): 'دﺪﺤﻣ',
        ('*', 'Affect Alpha:'): 'ﺎﻔﻟأ ﺮﺛﺄﺗ',
        ('*', 'Color:'): 'نﻮﻟ:',
        ('*', 'Change Layer Type'): 'ﺔﻘﺒﻄﻟا عﻮﻧ ﺮﻴﻴﻐﺗ',
        ('*', 'Base Value:'): 'ﺔﻴﺳﺎﺳﻷا ﺔﻤﻴﻘﻟا:',
        ('*', 'Base Alpha:'): 'ﺔﻴﺳﺎﺳﻷا ﺔﻴﻓﺎﻔﺸﻟا:',
        ('*', 'Use Clamp:'): 'دﺪﺤﻣ ماﺪﺨﺘﺳأ:',
        ('*', 'Space:'): 'ءﺎﻀﻓ:',
        ('*', 'Color Data'): 'ناﻮﻟﻷا تﺎﻧﺎﻴﺑ',
        ('*', 'Non-Color Data'): 'ﺔﻴﻧﻮﻟ ﺮﻴﻏ تﺎﻧﺎﻴﺑ',
        ('*' , 'Base Color:'): 'ﻲﺳﺎﺳﻷا نﻮﻠﻟا:',
        ('*', 'Specific Mask / Override'): 'زوﺎﺠﺗ / دﺪﺤﻣ عﺎﻨﻗ',
        ('*', 'Active Tree:'): 'ﺔﻟﺎﻌﻔﻟا ةﺮﺠﺸﻟا',
        ('*', 'Input:'): 'ﻞﺧد:',
        ('*', 'Blend:'): 'جﺰﻣ:',
        ('*', 'Override:'): 'زوﺎﺠﺗ:',
        ('*', 'Stats'): 'تاءﺎﺼﺣإ:',
        ('*', 'Default New Image Size'): 'ةﺪﻳﺪﺟ ةرﻮﺼﻟ ﻲﺳﺎﺳﻷا ﻢﺠﺤﻟا',
        ('*', 'Image Atlas Size'): 'رﻮﺼﻟا ﺲﻠﻃأ ﻢﺠﺣ',
        ('*', 'HDR Image Atlas Size'): 'HDR رﻮﺼﻟا ﺲﻠﻃأ ﻢﺠﺣ',
        ('*', 'Make Preview Mode use sRGB'): 'sRGB مﺪﺨﺘﺴﻳ ﺔﻨﻳﺎﻌﻤﻟا ﻊﺿو ﻞﻌﺟإ',
        ('*', 'Use Image Preview/Thumbnail'): 'ةﺮﻐﺼﻣ ةرﻮﺻ/ةرﻮﺼﻟا ﺔﻨﻳﺎﻌﻣ مﺪﺨﺘﺳإ',
        ('*', 'Show Experimental Features'): 'ﺔﻴﺒﻳﺮﺠﺘﻟا تاﺰﻴﻤﻟا ﺮﻬﻃأ',
        ('*', 'Developer Mode'): 'رﻮﻄﻤﻟا ﻊﺿو',
        ('*', 'Samples:'): 'تﺎﻨﻴﻌﻟا:',
        ('*', 'Margin:'): 'ﺶﻣﺎﻫ:',
        ('*', 'AA Level:'): 'AA ﻦﻨﺴﺘﻟا ﺔﻟازإ ىﻮﺘﺴﻣ:',
        ('*', 'Bake Device:'): 'ﻂﻔﺤﻟا زﺎﻬﺟ:',
        ('*', 'Use FXAA'): 'FXAA ماﺪﺨﺘﺳأ',
        ('*', 'Use Denoise'): 'ءﺎﺿﻮﻀﻟا ﻒﻔﺨﻣ ماﺪﺨﺘﺳأ',
        ('*', 'Force Bake all Polygons'): 'تﺎﻌﻠﻀﻤﻟا ﻊﻴﻤﺟ ﻂﻔﺣ مﺎﻏرإ',
        ('*', 'Add Mask'): 'عﺎﻨﻗ ﺔﻓﺎﺿإ',
        ('*', 'Name:'): 'ﻢﺳا:',
        ('*', 'Mask Type:'): 'عﺎﻨﻘﻟا عﻮﻧ:',
        ('*', 'White (Full Opacity)'): '(ﺔﻴﻓﺎﻔﺷ ﻻ) ﺾﻴﺑأ',
        ('*', 'Black (Full Transparency)'): '(فﺎﻔﺷ) دﻮﺳأ',
        ('*', 'Mask Width:'): 'عﺎﻨﻘﻟا ضﺮﻋ:',
        ('*', 'Mask Height:'): 'عﺎﻨﻘﻟا عﺎﻔﺗرا:',
        ('*', 'Mask Color:'): 'عﺎﻨﻘﻟا نﻮﻟ:',
        ('*', 'Use Baked'): 'ظﻮﻔﺤﻤﻟا ماﺪﺨﺘﺳأ',
        ('*', 'Enable Baked Outside'): 'ﺎﺟرﺎﺧ ﻞﻳﺪﻌﺘﻟا ﻞﻴﻌﻔﺗ',
        ('*', 'Create baked texture nodes outside of main node\n(Can be useful for exporting material to other application)'): 'ucupaint ـﻟ ﺔﻴﺳﺎﺳﻷا ةﺪﻘﻌﻟا جرﺎﺧ ﺔﻃﻮﻔﺤﻤﻟا رﻮﺼﻠﻟ ﺪﻘﻋ ءﺎﺸﻧإ \n(ﺞﻣاﺮﺑ ﺮﻴﻐﻟ جاﺮﺧﻷا ﻞﺟﻷ ةﺪﻴﻔﻣ نﻮﻜﺗ نأ ﻦﻜﻤﻤﻟا ﻦﻣ)',
        ('*', 'No active image'): 'ﺔﻟﺎﻌﻓ ةرﻮﺻ ﺪﺟﻮﺗ ﻻ',
        ('*', 'Active Image: '): 'ﺔﻟﺎﻌﻔﻟا ةرﻮﺼﻟا: ',
        ('*', 'Shortcut on list:'): 'ﻢﺋاﻮﻘﻟا ﻰﻠﻋ تارﺎﺼﺘﺧأ:',
        ('*', 'Connect To:'): 'ـﻟ ﻞﻴﺻﻮﺗ:',
        ('*', 'Fill '): 'ﺊﻠﻣ ',
        ('*', 'Fill selected polygon with vertex color'): 'طﺎﻘﻨﻟا نﻮﻠﺑ ةدﺪﺤﻤﻟا تﺎﻌﻠﻀﻤﻟا ﺊﻠﻣ',
        ('*', 'Fill selected polygon with vertex color with custom color'): 'ﺺﺼﺨﻣ نﻮﻟ ﻊﻣ طﺎﻘﻨﻟا نﻮﻠﺑ ةدﺪﺤﻤﻟا تﺎﻌﻠﻀﻤﻟا ﺊﻠﻣ',
        ('*', 'Fill Color ID'): 'نﻮﻠﻟا فﺮﻌﻣ ﺊﻠﻣ',
        ('*', 'Number of Images: '): 'رﻮﺼﻟا دﺪﻋ: ',
        ('*', 'Number of Vertex Colors: '): 'طﺎﻘﻨﻟا ناﻮﻟأ دﺪﻋ: ',
        ('*', 'Number of Generated Textures: '): 'ﺔﺠﺘﻨﻤﻟا ﺞﺴﻨﻟا دﺪﻋ: ',
        ('*', 'Number of Color Ramps: '): 'نﻮﻠﻟا رﺪﺤﻨﻣ دﺪﻋ: ',
        ('*', 'Number of RGB Curves: '): 'ناﻮﻟﻷا ﻰﻨﺤﻨﻣ دﺪﻋ: ',
        ('*', 'Inbetween Modifier Mask:'): 'عﺎﻨﻘﻠﻟ ﻲﻨﻴﺑ ﺮﻴﻐﻣ:',
        ('*', 'Extra Props'): 'ﺔﻴﻓﺎﺿإ تارﺎﻴﺧ',
        ('*', 'Material: '): 'ةدﺎﻣ: ',
        ('*', 'Blur:'): 'ﺔﻴﺑﺎﺒﻀﻟا:',
        ('*', 'Use Clamp'): 'دﺪﺤﻤﻟا ماﺪﺨﺘﺳأ',
        ('*', 'Documentation:'): 'ﻖﻴﺛﻮﺗ:',
        ('*', get_addon_title() + ' About'): '%s ﻦَﻋ' % get_addon_title(),
        ('*', get_addon_title() + ' is created by:'): 'ﻞَﺒِﻗ ﻦﻣ ﺖﻌﻨُﺻ %s:' % get_addon_title(),
        ('*', get_addon_title() + ' Special Menu'): 'ةﺰﻴﻤﻤﻟا ﺔﻤﺋﺎﻗ %s' % get_addon_title(),
        ('Operator', 'Add new ' + get_addon_title() + ' Node'): 'ةﺪﻳﺪﺟ %s ةﺪﻘﻋ ﻒﺿأ' % get_addon_title(),
        ('Operator', 'Add new ' + get_addon_title() + ' Channel'): 'ةﺪﻳﺪﺟ %s ةﺎﻨﻗ ﻒﺿأ' % get_addon_title(),
        ('Operator', 'Remove ' + get_addon_title() + ' Channel'): '%s ةﺎﻨﻗ فﺬﺣ' % get_addon_title(),
        ('Operator', 'Move ' + get_addon_title() + ' Channel'): '%s ةﺎﻨﻗ ﻚﻳﺮﺤﺗ' % get_addon_title(),
        ('Operator', 'Open Available Image'): 'ﺔﺣﺎﺘﻤﻟا رﻮﺼﻟا ﺢﺘﻓ',
        ('Operator', 'Background'): 'ﺔﻴﻔﻠﺧ',
        ('Operator', 'Ramp'): 'نﻮﻠﻟا رﺪﺤﻨﻣ',
        ('Operator', 'Fake Lighting'): 'ﺔﻴﻤﻫو ةءﺎﺿإ',
        ('Operator', 'Curve'): 'ﻰﻨﺤﻨﻣ',
        ('Operator', 'Resize Image'): 'ةرﻮﺼﻟا ﻢﺠﺣ ﺮﻴﻴﻐﺗ',
        ('Operator', 'Open Images to Single Layer'): 'ةﺪﺣاو ﺔﻘﺒﻃ ﻲﻓ رﻮﺼﻟا ﺢﺘﻓ',
        ('Operator', 'Layer Group'): 'ﺔﻘﺒﻄﻟا ﺔﻋﻮﻤﺠﻣ',
        ('Operator', 'New Vertex Color'): 'ﺪﻳﺪﺟ طﺎﻘﻧ نﻮﻟ',
        ('Operator', 'Open Available Vertex Color'): 'ﺔﺣﺎﺘﻤﻟا طﺎﻘﻨﻟا ناﻮﻟأ ﺢﺘﻓ',
        ('Operator', 'Use Available Vertex Color'): 'ﺔﺣﺎﺘﻤﻟا طﺎﻘﻨﻟا ناﻮﻟأ مﺪﺨﺘﺳا',
        ('Operator', 'New Vertex Color Mask'): 'ﺪﻳﺪﺟ طﺎﻘﻧ ناﻮﻟأ عﺎﻨﻗ',
        ('Operator', 'Open Available Vertex Color as Mask'): 'عﺎﻨﻘﻛ ﺔﺣﺎﺘﻤﻟا طﺎﻘﻨﻟا ناﻮﻟأ ﺢﺘﻓ',
        ('Operator', 'Color ID'): 'نﻮﻠﻟا فﺮﻌﻣ',
        ('Operator', 'Color ID '): ' نﻮﻠﻟا فﺮﻌﻣ',
        ('Operator', 'Backface'): 'ﺔﻴﻔﻠﺨﻟا هﻮﺟﻮﻟا',
        ('Operator', 'New Image Mask'): 'ﺪﻳﺪﺟ عﺎﻨﻗ ةرﻮﺻ',
        ('Operator', 'Open Image as Mask'): 'عﺎﻨﻘﻛ ةرﻮﺻ ﺢﺘﻓ',
        ('Operator', 'Open Available Image as Mask'): 'عﺎﻨﻘﻛ ﺔﺣﺎﺘﻤﻟا رﻮﺼﻟا ﺢﺘﻓ',
        ('Operator', 'Vertex Color'): 'طﺎﻘﻨﻟا ﻦﻳﻮﻠﺗ',
        ('Operator', 'Image'): 'ةرﻮﺻ',
        ('Operator', 'Group'): 'ﺔﻋﻮﻤﺠﻣ',
        ('Operator', 'RGB to Intensity'): 'ةﺪﺤﻠﻟ RGB',
        ('Operator', 'Color Ramp'): 'ناﻮﻟﻷا رﺪﺤﻨﻣ',
        ('Operator', 'RGB Curve'): 'RGB ﻰﻨﺤﻨﻣ',
        ('Operator', 'Hue Saturation'): 'نﻮﻠﻟا ﻊﺒﺸﺗ',
        ('Operator', 'Brightness Contrast'): 'ﻦﻳﺎﺒﺘﻟا و عﻮﻄﺴﻟا',
        ('Operator', 'Math'): 'بﺎﺴﺣ',
        ('Operator', 'Solid Color'): 'ﻲﻓﺎﺻ نﻮﻟ',
        ('Operator', 'Solid Color w/ Image Mask'): 'عﺎﻨﻗ ةرﻮﺻ ﻊﻣ ﻲﻓﺎﺻ نﻮﻟ',
        ('Operator', 'Solid Color w/ Vertex Color Mask'): 'طﺎﻘﻨﻟا نﻮﻟ عﺎﻨﻗ ﻊﻣ ﻲﻓﺎﺻ نﻮﻟ',
        ('Operator', 'Solid Color w/ Color ID Mask'): 'نﻮﻠﻟا فﺮﻌﻣ عﺎﻨﻗ ﻊﻣ ﻲﻓﺎﺻ نﻮﻟ',
        ('Operator', 'Background w/ Image Mask'): 'ةرﻮﺻ عﺎﻨﻗ ﻊﻣ ﺔﻴﻔﻠﺧ',
        ('Operator', 'Background w/ Vertex Color Mask'): 'طﺎﻘﻨﻟا نﻮﻟ عﺎﻨﻗ ﻊﻣ ﺔﻴﻔﻠﺧ',
        ('Operator', 'Bake Channel to Vertex Color (Batch All Materials)'): '(داﻮﻤﻟا ﻊﻴﻤﺟ ﺔﻌﻓد) طﺎﻘﻨﻟا نﻮﻠﻟ ةﺎﻨﻘﻟا ﻂﻔﺣ',
        ('Operator', 'Bake Channel to Vertex Color'): 'طﺎﻘﻨﻟا نﻮﻠﻟ ةﺎﻨﻘﻟا ﻂﻔﺣ',
        ('Operator', 'Fix Unconnected Channel Output'): 'لﻮﺻﻮﻣ ﺮﻴﻏ ةﺎﻨﻗ جﺮﺨﻣ حﻼﺻإ',
        ('Operator', 'Brick'): '(Brick) بﻮﻃ',
        ('Operator', 'Checker'): '(Checker) ﺔﻌﻗر',
        ('Operator', 'Noise'): '(Noise) ءﺎﺿﻮﺿ',
        ('Operator', 'Wave'): '(Wave) ﺔﺟﻮﻣ',
        ('Operator', 'Intensity to RGB'): 'ناﻮﻟأ ﻰﻟا ةﺪﺸﻟا ﻞﻳﻮﺤﺗ',
        ('Operator', 'Move Mask Up'): 'ﻰﻠﻋﻸﻟ عﺎﻨﻘﻟا ﻚﻳﺮﺤﺗ',
        ('Operator', 'Move Mask Down'): 'ﻞﻔﺳﻸﻟ عﺎﻨﻘﻟا ﻚﻳﺮﺤﺗ',
        ('Operator', 'Merge Mask Up'): 'ﻰﻠﻋﻸﻟ عﺎﻨﻘﻟا ﺞﻣد',
        ('Operator', 'Merge Mask Down'): 'ﻞﻔﺳﻸﻟ عﺎﻨﻘﻟا ﺞﻣد',
        ('Operator', 'Duplicate as Image'): 'ةرﻮﺼﻛ ﺔﻔﻋﺎﻀﻣ',
        ('Operator', 'Remove Mask'): 'عﺎﻨﻘﻟا ﺔﻟاذإ',
        ('Operator', 'Merge Layer Up'): 'ﻰﻠﻋﻸﻟ ﺔﻘﺒﻄﻟا ﺞﻣد',
        ('Operator', 'Merge Layer Down'): 'ﻞﻔﺳﻸﻟ ﺔﻘﺒﻄﻟا ﺞﻣد',
        ('Operator', 'Move Mask Up'): 'ﻰﻠﻋﻸﻟ عﺎﻨﻘﻟا ﻚﻳﺮﺤﺗ',
        ('Operator', 'Save/Pack All'): 'ءﻲﺷ ﻞﻛ مﺰﺣ/ﻂﻔﺣ',
        ('Operator', 'Invert Image'): 'رﻮﺼﻟا ﺲﻜﻋ',
        ('Operator', 'Duplicate Layer'): 'ﺔﻘﺒﻄﻟا ﺔﻔﻋﺎﻀﻣ',
        ('Operator', 'Duplicate Blank Layer'): 'ﺔﻏرﺎﻓ ﺔﻘﺒﻃ ﺔﻔﻋﺎﻀﻣ',
        ('Operator', 'Copy Layer'): 'ﺔﻘﺒﻄﻟا ﺦﺴﻧ',
        ('Operator', 'Copy All Layers'): 'تﺎﻘﺒﻄﻟا ﻞﻛ ﺦﺴﻧ',
        ('Operator', 'Paste Layer(s)'): 'تﺎﻘﺒﻄﻟا ﻖﺼﻟ',
        ('Operator', 'Refill UDIM Tiles'): 'UDIM ﺔﻌﻗر ﺊﻠﻣ ةدﺎﻋإ',
        ('Operator', 'Bake All Channels'): 'تاﻮﻨﻘﻟا ﻞﻛ ﻂﻔﺣ',
        ('Operator', 'Rename Tree'): 'ucupaint ةﺮﺠﺷ ﺔﻴﻤﺴﺗ ةدﺎﻋإ',
        ('Operator', 'Remove ' + get_addon_title() + ' Node'): '%s ةﺪﻘﻋ ﺔﻟازإ' % (get_addon_title()),
        ('Operator', 'Clean ' + get_addon_title() + ' Caches'): '%s ـﻟ ﻦﻳﺰﺨﺘﻟا ةﺮﻛاذ ﺢﺴﻣ' % (get_addon_title()),
        ('Operator', 'Duplicate Material and ' + get_addon_title() + ' nodes'): '%s ﺪﻘﻋو ةدﺎﻤﻟا ﺔﻔﻋﺎﻀﻣ' % (get_addon_title()),
        ('Operator', 'Bake channels to Image'): 'ةرﻮﺻ ﻲﻓ تاﻮﻨﻘﻟا ﻂﻔﺣ',
        ('Operator', 'Unpack As Image'): 'ةرﻮﺼﻛ غاﺮﻓإ',
        ('Operator', 'Convert to Image Atlas'): 'ﺲﻠﻃأ ﻰﻟا ةرﻮﺼﻟا ﻞﻳﻮﺤﺗ',
        ('Operator', 'Convert All Images to Image Atlas'): 'ﺲﻠﻃأ ﻰﻟا ةﻮﺼﻟا ﻊﻴﻤﺟ ﻞﻳﻮﺤﺗ',
        ('Operator', 'Toggle Eraser'): 'ةﺎﺤﻤﻣ ﻰﻟا ﻞﻳﺪﺒﺗ',
        ('Operator', 'Disable Eraser'): 'ةﺎﺤﻤﻤﻟا فﺎﻘﻳإ',
        ('Operator', 'Fix Active Vcol Mismatch!'): '!ﻞﻌﻔﻤﻟا طﺎﻘﻨﻟا نﻮﻟ حﻼﺻإ',
        ('Operator', 'White'): 'ﺾﻴﺑأ',
        ('Operator', 'Black'): 'دﻮﺳأ',
    }
}