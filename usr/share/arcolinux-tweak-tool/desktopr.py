# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import numpy as np
import Functions as fn
import Settings
import gi
import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk  # noqa

desktops = [
    "awesome",
    "bspwm",
    "budgie-desktop",
    "cinnamon",
    "cwm",
    "deepin",
    "fvwm3",
    "dwm",
    "gnome",
    "herbstluftwm",
    "i3",
    "icewm",
    "jwm",
    "lxqt",
    "mate",
    "openbox",
    "plasma",
    "qtile",
    "spectrwm",
    "ukui",
    "xfce",
    "xmonad"
]
pkexec = ["pkexec", "pacman", "-S", "--needed", "--noconfirm", "--ask=4"]
pkexec_reinstall = ["pkexec", "pacman", "-S", "--noconfirm"]
copy = ["cp", "-Rv"]

awesome = [
    "arcolinux-awesome-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "autorandr",
    "awesome",
    "dmenu",
    "feh",
    "gmrun",
    "lxappearance",
    "picom",
    "polkit-gnome",
    "rofi",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "vicious",
    "volumeicon",
    "xfce4-terminal",
]
bspwm = [
    "arcolinux-bspwm-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "bspwm",
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polybar",
    "polkit-gnome",
    "rofi",
    "sutils-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-terminal",
    "xtitle-git",
]
budgie = [
    "arcolinux-budgie-dconf-git",
    "arcolinux-budgie-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-guake-autostart-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "budgie-desktop",
    "budgie-extras",
    "dconf-editor",
    "gnome",
    "guake",
    "ttf-hack",
]
cinnamon = [
    "arcolinux-cinnamon-dconf-git",
    "arcolinux-cinnamon-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "cinnamon",
    "cinnamon-translations",
    "gnome-screenshot",
    "gnome-system-monitor",
    "gnome-terminal",
    "iso-flag-png",
    "mintlocale",
    "nemo-fileroller",
    "xfce4-terminal",
]
cwm = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-cwm-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-polybar-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "autorandr",
    "cwm",
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polybar",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-terminal",
]
deepin = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-deepin-dconf-git",
    "arcolinux-deepin-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "deepin",
    "deepin-extra",
]
dwm = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-dwm-git",
    "arcolinux-dwm-slstatus-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "dmenu",
    "feh",
    "gmrun",
    "gsimplecal",
    "picom",
    "polkit-gnome",
    "rofi",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-notifyd",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
fvwm3 = [
     "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-fvwm3-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "dmenu",
    "feh",
    "gmrun",
    "gsimplecal",
    "picom",
    "polkit-gnome",
    "rofi",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-notifyd",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
gnome = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-gnome-dconf-git",
    "arcolinux-gnome-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-guake-autostart-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "dconf-editor",
    "gnome",
    "gnome-extra",
    "guake",
    "ttf-hack",
]
hlwm = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-herbstluftwm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "herbstluftwm",
    "picom",
    "polkit-gnome",
    "polybar",
    "rofi",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-terminal",
    "xtitle-git",
]
i3 = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-i3wm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-nitrogen-git",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "autotiling",
    "dmenu",
    "feh",
    "i3blocks",
    "i3-gaps",
    "i3status",
    "nitrogen",
    "picom",
    "polkit-gnome",
    "polybar",
    "rofi",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-terminal",
]
icewm = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-icewm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "autorandr",
    "dmenu",
    "feh",
    "icewm",
    "picom",
    "polkit-gnome",
    "rofi",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xdgmenumaker",
    "xfce4-notifyd",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
jwm = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-jwm-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "autorandr",
    "dmenu",
    "feh",
    "jwm",
    "picom",
    "polkit-gnome",
    "rofi",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xdgmenumaker",
    "xfce4-notifyd",
    "xfce4-screenshooter",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
lxqt = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-lxqt-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "dmenu",
    "lxqt",
    "lxqt-arc-dark-theme-git",
    "obconf-qt",
    "pavucontrol-qt",
    "picom",
    "polkit-gnome",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-screenshooter",
    "xfce4-taskmanager",
    "xfce4-terminal",
    "xscreensaver",
]
mate = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-mate-dconf-git",
    "arcolinux-mate-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "dmenu",
    "gnome-screenshot",
    "mate",
    "mate-extra",
    "mate-tweak",
    "xfce4-terminal",
]
openbox = [
    "arcolinux-common-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-docs-git",
    "arcolinux-geany-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-nitrogen-git",
    "arcolinux-obmenu-generator-git",
    "arcolinux-openbox-git",
    "arcolinux-pipemenus-git",
    "arcolinux-plank-git",
    "arcolinux-plank-themes-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tint2-git",
    "arcolinux-tint2-themes-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "dmenu",
    "feh",
    "geany",
    "gksu",
    "gmrun",
    "gnome-screenshot",
    "gsimplecal",
    "gtk2-perl",
    "lxappearance-obconf",
    "lxrandr",
    "nitrogen",
    "obconf",
    "obkey",
    "obmenu-generator",
    "obmenu3",
    "openbox",
    "openbox-arc-git",
    "openbox-themes-pambudi-git",
    "perl-linux-desktopfiles",
    "picom",
    "plank",
    "polkit-gnome",
    "rofi",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "tint2",
    "volumeicon",
    "xcape",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-terminal",
    "yad",
]
plasma = [
    "plasma",
    "kde-applications-meta",
    "kde-system-meta",
    "arcolinux-arc-kde",
    "arcolinux-config-plasma-git",
    "arcolinux-gtk3-surfn-arc-breeze-git",
    "arcolinux-plasma-dconf-git",
    "arcolinux-plasma-git",
    "arcolinux-plasma-kservices-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-wallpapers-git",
    "ark",
    "breeze",
    "cryfs",
    "discover",
    "dolphin",
    "dolphin-plugins",
    "encfs",
    "ffmpegthumbs",
    "gocryptfs",
    "gwenview",
    "kate",
    "kde-gtk-config",
    "kdeconnect",
    "kdenetwork-filesharing",
    "ktorrent",
    "ocs-url",
    "okular",
    "packagekit-qt5",
    "partitionmanager",
    "sddm-kcm",
    "spectacle",
    "surfn-arc-breeze-icons-git",
    "systemd-kcm",
    "yakuake",
]
qtile = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-qtile-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polkit-gnome",
    "python-psutil",
    "qtile",
    "rofi",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-terminal",
]
spectrwm = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-spectrwm-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "picom",
    "polkit-gnome",
    "polybar",
    "python-psutil",
    "spectrwm",
    "sutils-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xdo",
    "xfce4-terminal",
    "xtitle-git",
]
ukui = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-qt5-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-ukui-dconf-git",
    "arcolinux-ukui-git",
    "arcolinux-xfce-git",
    "arcolinux-wallpapers-git",
    "dmenu",
    "gnome-screenshot",
    "gvfs",
    "mate-control-center",
    "mate-desktop",
    "mate-menus",
    "mate-system-monitor",
    "mate-terminal",
    "qt5-quickcontrols",
    "redshift",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "ukui",
    "xfce4-terminal",
]
xfce = [
    "xfce4",
    "xfce4-goodies",
    "dmenu",
    "gmrun",
    "polkit-gnome",
    "rofi",
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",    
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",    
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "arcolinux-wallpapers-git",
]
xmonad = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-wallpapers-git",
    "arcolinux-xfce-git",
    "arcolinux-xmonad-polybar-git",
    "awesome-terminal-fonts",
    "dmenu",
    "feh",
    "gmrun",
    "haskell-dbus",
    "perl-checkupdates-aur",
    "perl-www-aur",
    "picom",
    "polybar",
    "rofi",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-terminal",
    "xmonad",
    "xmonad-contrib",
    "xmonad-log",
    "xmonad-utils",
]


def check_desktop(desktop):
    # /usr/share/xsessions/xfce.desktop
    lst = fn.os.listdir("/usr/share/xsessions/")
    for x in lst:
        if desktop + ".desktop" == x:
            return True

    return False


def uninstall_desktop_check(self, desktop):
    dsk = Settings.read_settings("DESKTOP", "default")
    if not desktop == dsk.strip():
        if check_desktop(desktop):
            uninstall_desktop(desktop)
        else:
            fn.show_in_app_notification(self,
                                        "Not installed...")
    else:
        fn.show_in_app_notification(self,
                                    "That is your default desktop!")


def uninstall_desktop(desktop):
    print("Uninstalling.....")

def check_lock(self, desktop, state):
    if fn.os.path.isfile("/var/lib/pacman/db.lck"):
        md = Gtk.MessageDialog(parent=self,
                            flags=0,
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.YES_NO,
                            text="Lock File Found")
        md.format_secondary_markup(
            "pacman lock file found, do you want to remove it and continue?")  # noqa

        result = md.run()
        md.destroy()

        if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
            fn.os.unlink("/var/lib/pacman/db.lck")
            # print("YES")
            t1 = fn.threading.Thread(target=install_desktop,
                                    args=(self,
                                        self.d_combo.get_active_text(),
                                        state))
            t1.daemon = True
            t1.start()
    else:
        # print("NO FILE")
        t1 = fn.threading.Thread(target=install_desktop,
                                 args=(self,
                                       self.d_combo.get_active_text(),
                                       state))
        t1.daemon = True
        t1.start()

    return False


def check_package(self, path, package):
    if fn.os.path.isfile(path + "/" + package):
        with fn.subprocess.Popen(["sh", "-c", "yes | pkexec pacman -R " + package], bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
            for line in p.stdout:
                GLib.idle_add(self.desktopr_stat.set_text, line.strip())


def install_desktop(self, desktop, state):

    src = []
    twm = False
    # error = False
    # make backup of your .config
    now = datetime.datetime.now()
    fn.copy_func(fn.home + "/.config/", fn.home + "/.config-att-" + now.strftime("%Y-%m-%d-%H-%M-%S"), isdir=True)
    if desktop == "awesome":
        command = list(np.append(awesome))
        src.append("/etc/skel/.config/awesome")
        twm = True
    elif desktop == "bspwm":
        command = list(np.append(bspwm))
        src.append("/etc/skel/.config/bspwm")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "budgie-desktop":
        check_package(self, "/usr/bin", "catfish")
        command = budgie
    elif desktop == "cinnamon":
        command = cinnamon
    elif desktop == "cwm":
        command = list(np.append(cwm)
        src.append("/etc/skel/.config/cwm")
        src.append("/etc/skel/.cwmrc")
        src.append("/etc/skel/.xprofile")
        src.append("/etc/skel/.config/polybar")
        twm = True        
    elif desktop == "deepin":
        check_package(self, "/usr/bin", "qt5ct")
        command = deepin
    elif desktop == "dwm":
        command = list(np.append(dwm)
        src.append("/etc/skel/.config/arco-dwm")
        twm = True
    elif desktop == "fvwm3":
        command = list(np.append(fvwm3)
        src.append("/etc/skel/.config/fvwm3")
        src.append("/etc/skel/.fvwm")
        twm = True
    elif desktop == "gnome":
        command = gnome
    elif desktop == "herbstluftwm":
        command = list(np.append(hlwm)
        src.append("/etc/skel/.config/herbstluftwm")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "i3":
        command = list(np.append(i3)
        src.append("/etc/skel/.config/i3")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "icewm":
        command = list(np.append(icewm)
        src.append("/etc/skel/.config/icewm")
        twm = True
    elif desktop == "jwm":
        command = list(np.append(jwm)
        src.append("/etc/skel/.config/jwm")
        src.append("/etc/skel/.jwmrc")
        twm = True
    elif desktop == "lxqt":
        command = list(np.append(lxqt)
        src.append("/etc/skel/.config/lxqt")
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/pcmanfm-qt")
        src.append("/etc/skel/.config/qterminal.org")
        src.append("/etc/skel/.local/share/filemanager/actions/")
        twm = True
    elif desktop == "mate":
        command = mate
    elif desktop == "openbox":
        command = list(np.append(openbox)
        src.append("/etc/skel/.config/openbox")
        src.append("/etc/skel/.config/obmenu-generator")
        src.append("/etc/skel/.config/tint2")
        src.append("/etc/skel/.config/nitrogen")
        twm = True
    elif desktop == "plasma":
        check_package(self, "/usr/bin", "qt5ct")
        command = plasma
        src.append("/etc/skel/.config")
        src.append("/etc/skel/.local/share")
        twm = True
    elif desktop == "qtile":
        command = list(np.append(qtile)
        src.append("/etc/skel/.config/qtile")
        twm = True
    elif desktop == "spectrwm":
        command = list(np.append(spectrwm)
        src.append("/etc/skel/.config/spectrwm")
        src.append("/etc/skel/.spectrwm.conf")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "ukui":
        command = list(np.append(ukui)
        src.append("/etc/skel/.config/")
        twm = True
    elif desktop == "xfce":
        command = list(np.append(xfce)
    elif desktop == "xmonad":
        command = list(np.append(xmonad)
        src.append("/etc/skel/.xmonad")
        src.append("/etc/skel/.config/polybar")
        twm = True
    # fn.subprocess.call(list(np.append(pkexec, command)))

    GLib.idle_add(self.desktopr_prog.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, fn.do_pulse, None, self.desktopr_prog)
    # print(command)

    if state == "reinst":
        com1 = pkexec_reinstall
        if self.ch1.get_active():
            GLib.idle_add(self.desktopr_stat.set_text, "Clearing cache .....")
            fn.subprocess.call(["sh", "-c", "yes | pkexec pacman -Scc"], shell=False, stdout=fn.subprocess.PIPE)
    else:
        com1 = pkexec

    # print(list(np.append(com1, command)))

    GLib.idle_add(self.desktopr_stat.set_text, "installing " + self.d_combo.get_active_text() + "...")

    with fn.subprocess.Popen(list(np.append(com1, command)), bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
        for line in p.stdout:
            GLib.idle_add(self.desktopr_stat.set_text, line.strip())

    GLib.source_remove(timeout_id)
    timeout_id = None
    GLib.idle_add(self.desktopr_prog.set_fraction, 0)

    if check_desktop(desktop):
        print(src)
        if twm is True:
            for x in src:
                if fn.os.path.isdir(x) or fn.os.path.isfile(x):
                    print(x)
                    dest = x.replace("/etc/skel", fn.home)
                    # print(dest)
                    if fn.os.path.isdir(x):
                        dest = fn.os.path.split(dest)[0]
                    l1 = np.append(copy, [x])
                    l2 = np.append(l1, [dest])
                    GLib.idle_add(self.desktopr_stat.set_text, "Copying " + x + " to " + dest)

                    with fn.subprocess.Popen(list(l2), bufsize=1, stdout=fn.subprocess.PIPE, universal_newlines=True) as p:
                        for line in p.stdout:
                            GLib.idle_add(self.desktopr_stat.set_text, line.strip())
                    # fn.subprocess.call(list(l2), shell=False, stdout=fn.subprocess.PIPE)
                    fn.permissions(dest)

        GLib.idle_add(self.desktopr_stat.set_text, "")
        GLib.idle_add(self.desktop_status.set_text, "This desktop is installed")
        GLib.idle_add(fn.show_in_app_notification, self, desktop + " has been installed")
    else:
        GLib.idle_add(self.desktop_status.set_markup, "This desktop is <b>NOT</b> installed")
        GLib.idle_add(self.desktopr_error.set_text, "Install " + desktop + " via terminal")
        # GLib.idle_add(self.desktopr_stat.set_text, "An error has occured in installation")
        GLib.idle_add(fn.show_in_app_notification, self, desktop + " has not been installed")
