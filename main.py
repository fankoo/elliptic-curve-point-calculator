import dearpygui.dearpygui as dpg
# import dearpygui_ext.themes as themes
from callback import *

dpg.create_context()
# DARK_IMGUI_THEME = themes.create_theme_imgui_dark()
# LIGHT_IMGUI_THEME = themes.create_theme_imgui_light()
app_name = 'Elliptic curve point Calculator'
app_id = dict()

def add_app_window():
    with dpg.window(label=app_name, width=600, height=730, pos=[0,0], no_resize=True, no_move=True, no_close=True) as app_id[app_name]:
        with dpg.menu_bar():
            with dpg.menu(label='Help'):
                dpg.add_menu_item(label="Show About", callback=lambda:dpg.show_tool(dpg.mvTool_About))
                dpg.add_menu_item(label="Show Metrics", callback=lambda:dpg.show_tool(dpg.mvTool_Metrics))
                dpg.add_menu_item(label="Show Documentation", callback=lambda:dpg.show_tool(dpg.mvTool_Doc))
                dpg.add_menu_item(label="Show Debug", callback=lambda:dpg.show_tool(dpg.mvTool_Debug))
                dpg.add_menu_item(label="Show Style Editor", callback=lambda:dpg.show_tool(dpg.mvTool_Style))
                dpg.add_menu_item(label="Show Font Manager", callback=lambda:dpg.show_tool(dpg.mvTool_Font))
                dpg.add_menu_item(label="Show Item Registry", callback=lambda:dpg.show_tool(dpg.mvTool_ItemRegistry))
                dpg.add_menu_item(label="Show ImGui Demo", callback=lambda:dpg.show_imgui_demo())
                dpg.add_menu_item(label="Show ImPlot Demo", callback=lambda:dpg.show_implot_demo())
                dpg.add_menu_item(label="Default",
                    callback=lambda: dpg.set_item_theme(app_id[app_name], 0))
                dpg.add_menu_item(label="Dark ImGui",
                                  callback=lambda: dpg.set_item_theme(app_id[app_name], DARK_IMGUI_THEME))
                dpg.add_menu_item(label="Light ImGui",
                                  callback=lambda: dpg.set_item_theme(app_id[app_name], LIGHT_IMGUI_THEME))
        for i in "AB":
            with dpg.child_window(width=-1, height=110):
                with dpg.group(label="group_%s##%s" % (i, app_name)):
                    with dpg.group(horizontal=True):
                        dpg.add_text(" %s" %i, color=[255, 0, 0])
                        app_id["%s_radio_button" % i] = dpg.add_radio_button(label="radio##%s##%s" % (i, app_name), items=("Vector", "Scalar"), default_value="Vector", horizontal=True, user_data=app_id, callback=select_type)
                        app_id["%s_rand_button" % i] = dpg.add_button(label="RAND##%s##%s" % (i, app_name), user_data=app_id, callback=rand_callback)
                        app_id["%s_base_button" % i] = dpg.add_button(label="basePoint##%s##%s" % (i, app_name), user_data=app_id, callback=base_point_callback)
                        dpg.add_text("2^")
                        app_id["%s_drag_int" % i] = dpg.add_drag_int(label="##%s##%s" % (i, app_name), min_value=0, max_value=256, width=75, user_data=app_id, callback=drag_pow_callback)
                        # app_id["%s_y_neg_y_button" % i] = dpg.add_button(label="Y<>-Y##%s##%s" % (i, app_name), user_data=app_id, callback=transposition_callback)
                        app_id["%s_to_memory_button" % i] = dpg.add_button(label="->Memory##%s##%s" % (i, app_name), indent=448, user_data=app_id, callback=send_to_memory)
                        app_id["%s_clear_button" % i] = dpg.add_button(label="Clear##%s##%s" % (i, app_name), user_data=app_id, callback=clear_callback)

                    with dpg.group(label="group_x_%s##%s" % (i, app_name), horizontal=True):
                        dpg.add_text(" X")
                        app_id["%s_x_input_text" % i] = dpg.add_input_text(label="##%s_x##%s" % (i, app_name), width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                        app_id["%s_x_pow" % i] = dpg.add_text(label="##pow##%s_x##%s" % (i, app_name))
                        app_id["%s_get_y_button" % i] = dpg.add_button(label="cal Y##%s##%s" % (i, app_name), indent=520, user_data=app_id, callback=get_y_coordinate)


                    with dpg.group(label="group_y_%s##%s" % (i, app_name), horizontal=True):
                        dpg.add_text(" Y")
                        app_id["%s_y_input_text" % i] = dpg.add_input_text(label="##%s_y##%s" % (i, app_name), width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                        app_id["%s_y_pow" % i] = dpg.add_text(label="##pow##%s_y##%s" % (i, app_name))
                        app_id["%s_y_neg_y_button" % i] = dpg.add_button(label="Y<>-Y##%s##%s" % (i, app_name), indent=520, arrow=True, direction=dpg.mvDir_Down, user_data=app_id, callback=transposition_callback)
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text("exchange Y -Y")

                    with dpg.group(label="group_neg_y_%s##%s" % (i, app_name), horizontal=True):
                        dpg.add_text("-Y")
                        app_id["%s_neg_y_input_text" % i] = dpg.add_input_text(label="##%s_neg_y##%s" % (i, app_name), width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                        app_id["%s_neg_y_pow" % i] = dpg.add_text(label="##pow##%s_neg_y##%s" % (i, app_name))

        with dpg.child_window(width=-1, height=35):
            with dpg.group(horizontal=True):
                dpg.add_text("Operation", color=[255, 0, 0])
                dpg.add_button(label=f"A + B##{app_name}", user_data=app_id, callback=add_callback)
                dpg.add_button(label=f"A - B##{app_name}", user_data=app_id, callback=sub_callback)
                dpg.add_button(label=f"A * B##{app_name}", user_data=app_id, callback=mul_callback)
                dpg.add_button(label=f"A / B##{app_name}", user_data=app_id, callback=div_callback)
        
        with dpg.child_window(width=-1, height=200):
            with dpg.group(label=f"group_C##{app_name}"):
                with dpg.group(horizontal=True):
                    dpg.add_text(" C", color=[255, 0, 0])
                    app_id["C_to_memory_button"] = dpg.add_button(label=f"->Memory##C##{app_name}", indent=500, user_data=app_id, callback=send_to_memory)

                with dpg.group(horizontal=True):
                    dpg.add_text(" X")
                    app_id["C_x_input_text"] = dpg.add_input_text(label=f"##C_x##{app_name}", width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                    app_id["C_x_pow"] = dpg.add_text(label=f"##pow##C_x##{app_name}")

                with dpg.group(horizontal=True):
                    dpg.add_text(" Y")
                    app_id["C_y_input_text"] = dpg.add_input_text(label=f"##C_y##{app_name}", width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                    app_id["C_y_pow"] = dpg.add_text(label=f"##pow##C_y##{app_name}")

                with dpg.group(horizontal=True):
                    dpg.add_text("-Y")
                    app_id["C_neg_y_input_text"] = dpg.add_input_text(label=f"##C_neg_y##{app_name}", width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                    app_id["C_neg_y_pow"] = dpg.add_text(label=f"##pow##C_neg_y##{app_name}")

            with dpg.group(label=f"group_public_key##{app_name}"):
                with dpg.group(horizontal=True):
                    dpg.add_text("Public key of C:")
                    app_id["public_to_memory_button"] = dpg.add_button(label=f"->Memory##public##{app_name}", indent=500, user_data=app_id, callback=send_to_memory)

                with dpg.group(horizontal=True):
                    dpg.add_text(" X")
                    app_id["public_x_input_text"] = dpg.add_input_text(label=f"##public_x##{app_name}", width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                    app_id["public_x_pow"] = dpg.add_text(label=f"##pow##public_x##{app_name}")
                
                with dpg.group(horizontal=True):
                    dpg.add_text(" Y")
                    app_id["public_y_input_text"] = dpg.add_input_text(label=f"##public_y##{app_name}", width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                    app_id["public_y_pow"] = dpg.add_text(label=f"##pow##public_y##{app_name}")
                
                with dpg.group(horizontal=True):
                    dpg.add_text("-Y")
                    app_id["public_neg_y_input_text"] = dpg.add_input_text(label=f"##public_neg_y##{app_name}", width=460, hexadecimal=True, no_spaces=True, uppercase=True, user_data=app_id, callback=get_bit_length)
                    app_id["public_neg_y_pow"] = dpg.add_text(label=f"##pow##public_neg_y##{app_name}")
        
        with dpg.child_window(width=-1, height=200, no_scrollbar=True):
            clear_memory_buton = dpg.add_button(label=f"Clear Memory##{app_name}", indent=475, user_data=app_id, callback=clear_memory)
            with dpg.table(header_row=True, policy=dpg.mvTable_SizingFixedFit, row_background=True, resizable=True, 
                        no_host_extendX=False, hideable=True, delay_search=True, 
                        borders_innerV=True, borders_outerV=True, borders_innerH=True, borders_outerH=True) as app_id["memory"]:

                dpg.add_table_column(label="Memory", width_stretch=True, init_width_or_weight=0.0)
                # dpg.add_table_column(label="Y", width_stretch=True, init_width_or_weight=0.0)
                dpg.add_table_column(label="Operation     ", width_fixed=True)


if __name__ == '__main__':
    dpg.create_viewport(title=app_name, width=620, height=750, x_pos=0, y_pos=0)
    add_app_window()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.set_primary_window(window=app_id[app_name], value=True)
    dpg.start_dearpygui()
    dpg.destroy_context()
