from libqtile import qtile, bar, widget
from libqtile.config import Screen

max_title_length = 10

# highlight_color = "#1f274f"
highlight_color = "#045159"
highlight_color2 = "001a2f"

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),

                widget.CurrentLayout(padding=2),

                widget.GroupBox(inactive="127D87",
                                highlight_method="line",
                                highlight_color=[
                                    highlight_color2, highlight_color],
                                this_current_screen_border=highlight_color,
                                this_screen_border=highlight_color,
                                disable_drag=True,
                                padding=4),

                widget.Prompt(font="JetBrainsMono Nerd Font",
                              fmt="${}",
                              prompt=" "),

                # widget.TaskList(icon_size=20,
                #                 border=highlight_color,
                #                 highlight_method="block",
                #                 margin=0,
                #                 padding_y=8,
                #                 padding_x=5,
                #                 # this is to slice title and add ... at end
                #                 parse_text=lambda x: x[:max_title_length] +
                #                 "..." if len(x) > max_title_length else "",
                #
                #
                #                 ),

                # widget.Sep(padding=16),
                # widget.Spacer(length=605),

                # widget.LaunchBar(progs=[
                #         ("/usr/lib/kitty/logo/kitty-128.png", "kitty", "terminal"),
                #         ("/opt/brave-bin/product_logo_128.png", "brave", "browser"),
                #     ],
                #
                #     padding=8),

                widget.Spacer(),
                widget.Clock(format="%b %d   %H:%M",
                             padding=0,
                             margin=0),
                # widget.Spacer(length=605),
                widget.Spacer(),

                widget.Systray(padding=5, margin=0),

                widget.Sep(padding=16, size_percent=70),

                widget.ThermalZone(padding=0, margin=0),
                # widget.Sep(padding=16),

                widget.Sep(padding=16, size_percent=70),
                # Using 2 widgets because the scroll function doesnt work with TextBox, I could use mouse_callback but thats too much work
                widget.Volume(fmt="{}",
                              emoji=True,
                              emoji_list=["󰸈 ", "󰖀 ", "󰕾 ", " "],
                              step=2,
                              padding=0),

                widget.Volume(fmt="{}",
                              step=2,
                              padding=0),
                widget.Sep(padding=16, size_percent=70),

                widget.Backlight(backlight_name="amdgpu_bl1",
                                 change_command="brightnessctl set {0}%",
                                 fmt="󰖨  {}",
                                 step=5.2,
                                 padding=0),
                widget.Sep(padding=16, size_percent=70),

                widget.Battery(format='{char} {percent:2.0%} {watt:.1f} W',
                               padding=0,
                               discharge_char="",
                               charge_char="󱐋",
                               empty_char="∅",
                               low_percentage=0.4,
                               update_interval=10,
                               notify_below=40,
                               low_background="#FF0000",
                               low_foreground="#FFFFFF"),
                widget.Sep(padding=16, size_percent=70),

                widget.QuickExit(default_text="[󰐥]",
                                 countdown_format="[{}]",
                                 padding=0),

                widget.Spacer(length=10),
            ],
            35,
            opacity=1,
            margin=[5, 5, 5, 5],
            # border_width=[2, 2, 2, 2],
            # border_color="#00000000",
        ),

        x11_drag_polling_rate=60,
    ),
    Screen(
        right=bar.Bar([
            widget.Spacer(10),
            widget.Clock(format="%H",
                         rotate=False,
                         padding=0,
                         margin=0,
                         fontsize=30),

            widget.Clock(format="%M",
                         rotate=False,
                         padding=0,
                         margin=0,
                         fontsize=30),

            # widget.Clock(format="%p",
            #              rotate=False,
            #              padding=0,
            #              margin=0,
            #              fontsize=16),

        ], 35,
            opacity=0.7,
            margin=[5, 5, 5, 5],
            border_width=[2, 2, 2, 2],
            border_color="#000000"
        ),
    )
]
