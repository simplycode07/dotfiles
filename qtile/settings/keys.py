from libqtile.config import Key
from libqtile.lazy import lazy
import os, subprocess

mod = "mod4"
terminal = "kitty"

def toggle_touchpad(qtile=None):
    script = os.path.expanduser("~/.config/qtile/toggle_touchpad.sh")
    subprocess.Popen([script])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(["mod1"], "Tab", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key(["mod1"], "Return", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "o",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "Shift"], "r", lazy.restart(), desc="Restart conf"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # launch browsers and shit
    Key([mod], "Backspace", lazy.spawn("rofi -show drun"), desc="run rofi"),
    Key([mod], "b", lazy.spawn("brave"), desc="Spawn brave browser"), 
    Key([mod], "e", lazy.spawn("nemo"), desc="Spawn Ranger"),
    #Key([mod, "shift"], "e", lazy.spawn("nemo"), desc="Spawn File explorer"),

    # screenshot
    # Key([], "Print", lazy.spawn(["sh", "-c", "gnome-screenshot -c /tmp/screenshot && cat /tmp/screenshot | xclip -i -selection clipboard -target image/png"]), desc="Copy Screenshot to Clipboard"),
    # Key(["shift"], "Print", lazy.spawn(["sh","-c","gnome-screenshot -acf /tmp/screenshot && cat /tmp/screenshot | xclip -i -selection clipboard -target image/png"]), desc="Screenshot of area to clipboard"),
    
    Key([], "Print", lazy.spawn("flameshot screen -c"), desc="Screenshot of screen"),
    Key(["shift"], "Print", lazy.spawn("flameshot gui -c -s"), desc="Screenshot of area"),
    # sound and volume controls

    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    
    # brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5-")),

    # move between workspaces
    Key([mod], "Tab", lazy.screen.next_group(skip_empty=True)),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group()),

    # lock screen
    Key([], "XF86PowerOff", lazy.spawn("cinnamon-screensaver-command -l")),

    # toggle touchpad
    Key([], "XF86TouchpadToggle", lazy.function(toggle_touchpad)),

]
