from libqtile import qtile, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from settings.keys import keys
from settings.screens import screens
import os
import random
import subprocess

if qtile.core.name == "wayland":
    os.environ["XDG_SESSION_DESKTOP"] = "qtile:wlroots"
    os.environ["XDG_CURRENT_DESKTOP"] = "qtile:wlroots"

mod = "mod4"
terminal = "kitty"
wallpaper_dir = "/home/dhruv/Wallpapers/"
cursor_warp = True
# WM_NAME(UTF8_STRING) = "Picture-in-picture"

# borders
# color_focused = "#24a695"
color_focused = "#ffffff"
color_normal = "#000000"
border_width = 4


def set_wallpaper(qtile=None, picture=None):
    if picture == None:
        wallpaper_list = os.listdir(wallpaper_dir)
        for i in wallpaper_list:
            if os.path.isdir(wallpaper_dir + i):
                wallpaper_list.remove(i)

        picture = random.choice(wallpaper_list)

    for screen in screens:
        screen.set_wallpaper(wallpaper_dir+picture, "fill")


groups = [Group("1",
                layout="columns",
                label="一"),
          Group("2",
                layout="columns",
                label="二"),
          Group("3",
                label="三"),
          Group("4",
                label="四"),
          Group("5",
                label="五")]
layout_key_dict = {
    "1": "a",
    "2": "s",
    "3": "d",
    "4": "f",
    "5": "g",
}

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                layout_key_dict[i.name],
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                layout_key_dict[i.name],
                # i.name,
                lazy.window.togroup(i.name),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
        ]
    )
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
        ]
    )

groups.append(
    ScratchPad("scratchpad", [
        DropDown("term",
                 terminal,
                 height=0.6,
                 width=0.7,
                 x=0.15,
                 y=0.2,
                 opacity=1,
                 warp_pointer=True,
                 ),
    ]),
)

keys.extend(
    [
        Key([mod], "y", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "x", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "w", lazy.function(set_wallpaper)),
    ]
)
layouts = [
    layout.Columns(border_focus=color_focused,
                   border_normal=color_normal,
                   border_width=border_width,
                   border_on_single=True,
                   margin=5,
                   margin_y=3,
                   insert_postion=1),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(border_focus=color_focused,
    #            border_normal=color_normal,
    #            border_width=border_width,
    #            margin=5,
    #            margin_y=3),

    # layout.Matrix(border_focus=color_focused,
    #               border_normal=color_normal,
    #               border_width=border_width),
    #
    # layout.MonadTall(border_focus=color_focused,
    #                  border_normal=color_normal,
    #                  border_width=border_width),
    #
    # layout.MonadWide(border_focus=color_focused,
    #                  border_normal=color_normal,
    #                  border_width=border_width),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="VeraSe",
    background="#010F1A",
    foreground="#ffffff",
    font="FiraSans",
    fontsize=18,
)

extension_defaults = widget_defaults.copy()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, "shift"], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="Godot_Engine"),
        Match(wm_class="Godot_Editor"),
        Match(wm_class="Godot"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Screenshot"),  # Screenshot tool
    ],
    border_focus="#7AA2F7",
    border_normal="#00000000",
    border_width=3,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([script])
    # lazy.function(set_wallpaper)
    set_wallpaper(picture="15.jpg")
