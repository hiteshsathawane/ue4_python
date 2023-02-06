import unreal

import_setting = unreal.MovieSceneUserImportFBXSettings()
                 
import_setting.set_editor_property('convert_scene_unit',True)
import_setting.set_editor_property('create_cameras',True) 
import_setting.set_editor_property('force_front_x_axis',False) 
import_setting.set_editor_property('match_by_name_only',False)
import_setting.set_editor_property('reduce_keys',False)
import_setting.set_editor_property('reduce_keys_tolerance',0.001)