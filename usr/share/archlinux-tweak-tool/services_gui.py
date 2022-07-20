# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================


def gui(self, Gtk, vboxstack14, fn):
    """create a gui"""
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1_label = Gtk.Label(xalign=0)
    hbox1_label.set_text("Services")
    hbox1_label.set_name("title")
    hbox1.pack_start(hbox1_label, False, False, 10)

    hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox0.pack_start(hseparator, True, True, 0)

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    vboxstack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vboxstack5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vboxstack6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)
    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)

    # ==================================================================
    #                       NETWORK TAB
    # ==================================================================

    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2_label = Gtk.Label(xalign=0)
    hbox2_label.set_text(
        "Discover other computers in your network (to access other computers)"
    )
    button_install_discovery = Gtk.Button(label="Install network discovery")
    button_install_discovery.connect("clicked", self.on_install_discovery_clicked)
    button_remove_discovery = Gtk.Button(label="Uninstall network discovery")
    button_remove_discovery.connect("clicked", self.on_remove_discovery_clicked)
    hbox2.pack_start(hbox2_label, False, False, 10)
    hbox2.pack_end(button_remove_discovery, False, False, 10)
    hbox2.pack_end(button_install_discovery, False, False, 10)

    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3_label = Gtk.Label(xalign=0)
    hbox3_label.set_text("Change the /etc/nsswitch.conf to connect to computers/NAS")
    hbox3.pack_start(hbox3_label, False, False, 10)

    hbox30 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    self.nsswitch_choices = Gtk.ComboBoxText()
    options = ["ArcoLinux", "Garuda", "Arch Linux", "EndeavourOS", "Manjaro"]
    for option in options:
        self.nsswitch_choices.append_text(option)
    self.nsswitch_choices.set_active(0)
    button_apply_nsswitch = Gtk.Button(label="Apply selected nsswitch.conf")
    button_apply_nsswitch.connect("clicked", self.on_click_apply_nsswitch)
    button_reset_nsswitch = Gtk.Button(label="Reset to default nsswitch")
    button_reset_nsswitch.connect("clicked", self.on_click_reset_nsswitch)
    hbox30.pack_start(self.nsswitch_choices, False, False, 10)
    hbox30.pack_start(button_apply_nsswitch, False, False, 10)
    hbox30.pack_start(button_reset_nsswitch, False, False, 10)

    # ==================================================================
    #                       SAMBA EASY TAB
    # ==================================================================

    hbox_header_samba = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox_header_samba = Gtk.Label(xalign=0)
    hbox_header_samba.set_markup(
        "You install a samba server if you need to \
share a folder and its contents in your home network\n\
The purpose is to create <b>one</b> shared folder - the current user can later \
access this folder from other computers\n\
The easy configuration will create the folder 'Shared' in your home directory \
if it is not already there\n\
The usershares configuration will not create a 'Shared' folder - you share any folder you like\n\
Follow the instruction numbers below - <b>we recommend the easy configuration</b>"
    )

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4_label = Gtk.Label(xalign=0)
    hbox4_label.set_text("1. Install the samba server")
    button_uninstall_samba = Gtk.Button(label="Uninstall Samba")
    button_uninstall_samba.connect("clicked", self.on_click_uninstall_samba)
    button_install_samba = Gtk.Button(label="Install Samba")
    button_install_samba.connect("clicked", self.on_click_install_samba)
    hbox4.pack_start(hbox4_label, False, False, 10)
    hbox4.pack_end(button_uninstall_samba, False, False, 10)
    hbox4.pack_start(button_install_samba, False, False, 10)

    hbox4bis = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4bis_label = Gtk.Label(xalign=0)
    hbox4bis_label.set_text("2. Apply the /etc/samba/smb.conf of your choice")
    self.samba_choices = Gtk.ComboBoxText()
    options_samba = ["Easy", "Usershares", "Windows", "ArcoLinux", "Original"]
    for option in options_samba:
        self.samba_choices.append_text(option)
    self.samba_choices.set_active(0)
    button_apply_samba = Gtk.Button(label="Apply selected samba.conf")
    button_apply_samba.connect("clicked", self.on_click_apply_samba)
    button_reset_samba = Gtk.Button(label="Reset to default samba.conf")
    button_reset_samba.connect("clicked", self.on_click_reset_samba)
    hbox4bis.pack_start(hbox4bis_label, False, False, 10)
    hbox4bis.pack_start(self.samba_choices, True, False, 10)
    hbox4bis.pack_start(button_apply_samba, True, False, 10)
    hbox4bis.pack_end(button_reset_samba, False, False, 10)

    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5_label = Gtk.Label(xalign=0)
    hbox5_label.set_text(
        "3. Create a password for the current user to be able to access the Samba server"
    )
    button_create_samba_user = Gtk.Button(
        label="Create a password for the current user"
    )
    button_create_samba_user.connect("clicked", self.on_click_create_samba_user)
    hbox5.pack_start(hbox5_label, False, False, 10)
    hbox5.pack_start(button_create_samba_user, False, False, 10)

    hbox16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox16_label = Gtk.Label(xalign=0)
    hbox16_label.set_markup(
        "You can now reboot and enjoy the <b>'Shared'</b> folder if you choose '<b>easy</b>' "
    )
    hbox16.pack_start(hbox16_label, False, False, 10)

    hbox18 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox18_label = Gtk.Label(xalign=0)
    hbox18_label.set_markup(
        "If you choose '<b>usershares</b>' then we recommend you install \
also thunar and its plugin and \
right-click to share any folder in your home directory\nThere are other filemanagers with \
their plugins at the bottom"
    )
    hbox18.pack_start(hbox18_label, False, False, 10)

    hbox92 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox92_label = Gtk.Label(xalign=0)
    hbox92_label.set_markup(
        '<span foreground="red" size="large">We found a firewall on your system</span>'
    )
    hbox92.pack_start(hbox92_label, False, False, 10)

    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    install_arco_thunar_plugin = Gtk.Button(label="Install ArcoLinux Thunar plugin")
    install_arco_thunar_plugin.connect(
        "clicked", self.on_click_install_arco_thunar_plugin
    )
    install_arco_nemo_plugin = Gtk.Button(label="Install ArcoLinux Nemo plugin")
    install_arco_nemo_plugin.connect("clicked", self.on_click_install_arco_nemo_plugin)
    install_arco_caja_plugin = Gtk.Button(label="Install ArcoLinux Caja plugin")
    install_arco_caja_plugin.connect("clicked", self.on_click_install_arco_caja_plugin)
    hbox19.pack_start(install_arco_thunar_plugin, False, False, 10)
    hbox19.pack_start(install_arco_nemo_plugin, False, False, 10)
    hbox19.pack_start(install_arco_caja_plugin, False, False, 10)

    hbox91 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox91_label = Gtk.Label(xalign=0)
    hbox91_label.set_text(
        "With the Avahi daemon (network discovery) running on both the server \
and client,\nthe file manager on the client should automatically find the server - \
Beware of firewalls"
    )
    restart_smb = Gtk.Button(label="Restart Smb")
    restart_smb.connect("clicked", self.on_click_restart_smb)
    hbox91.pack_start(hbox91_label, False, False, 10)
    hbox91.pack_end(restart_smb, False, False, 10)

    hbox93 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox93_label = Gtk.Label(xalign=0)
    hbox94 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox94_label = Gtk.Label(xalign=0)

    status1 = fn.check_service("smb")
    if status1 is True:
        status1 = "active"
    else:
        status1 = "inactive"

    status2 = fn.check_service("nmb")
    if status2 is True:
        status2 = "active"
    else:
        status2 = "inactive"

    status3 = fn.check_service("avahi-daemon")
    if status3 is True:
        status3 = "active"
    else:
        status3 = "inactive"

    hbox93_label.set_text(
        "Samba : " + status1 + "   Nmb : " + status2 + "   Avahi : " + status3
    )
    hbox93.pack_start(hbox93_label, False, False, 10)
    hbox94_label.set_text(
        "Samba : " + status1 + "   Nmb : " + status2 + "   Avahi : " + status3
    )
    hbox94.pack_start(hbox94_label, False, False, 10)

    hbox95 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox95_label = Gtk.Label(xalign=0)
    hbox95_label.set_text(
        "With the Avahi daemon (network discovery) running on both \
the server and client,\n\
the file manager on the client should automatically find the server- Beware of firewalls\n\
All computers in your network must have a unique name /etc/hostname"
    )
    restart_smb = Gtk.Button(label="Restart Smb")
    restart_smb.connect("clicked", self.on_click_restart_smb)
    hbox95.pack_start(hbox95_label, False, False, 10)
    hbox95.pack_end(restart_smb, False, False, 10)

    # ==================================================================
    #                       CUPS TAB
    # ==================================================================

    hbox15 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox15_label = Gtk.Label(xalign=0)
    hbox15_label.set_text(
        "Printing can be a challenge. We recommend reading the Arch wiki cups page. Check before you buy.\n\
There are also printer specific pages. Lastly the AUR might contain the driver you need."
    )
    hbox15.pack_start(hbox15_label, False, False, 10)

    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8_label = Gtk.Label(xalign=0)
    hbox8_label.set_text("Install cups printing")
    btn_install_cups = Gtk.Button(label="Install cups")
    btn_install_cups.connect("clicked", self.on_click_install_cups)
    btn_remove_cups = Gtk.Button(label="Remove cups")
    btn_remove_cups.connect("clicked", self.on_click_remove_cups)
    hbox8.pack_start(hbox8_label, False, False, 10)
    hbox8.pack_end(btn_remove_cups, False, False, 10)
    hbox8.pack_end(btn_install_cups, False, False, 10)

    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox20_label = Gtk.Label(xalign=0)
    hbox20_label.set_text("Install cups-pdf printing")
    btn_install_cups = Gtk.Button(label="Install cups-pdf")
    btn_install_cups.connect("clicked", self.on_click_install_cups_pdf)
    btn_remove_cups = Gtk.Button(label="Remove cups-pdf")
    btn_remove_cups.connect("clicked", self.on_click_remove_cups_pdf)
    hbox20.pack_start(hbox20_label, False, False, 10)
    hbox20.pack_end(btn_remove_cups, False, False, 10)
    hbox20.pack_end(btn_install_cups, False, False, 10)

    hbox26 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox26_label = Gtk.Label(xalign=0)
    hbox26_label.set_text("Install drivers")
    hbox26.pack_start(hbox26_label, False, False, 10)

    hbox27 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox27_label = Gtk.Label(xalign=0)
    hbox27_label.set_text(
        "   Install common printer drivers (foomatic, gutenprint, ...)"
    )
    btn_install_printer_drivers = Gtk.Button(label="Install drivers")
    btn_install_printer_drivers.connect(
        "clicked", self.on_click_install_printer_drivers
    )
    btn_remove_printer_drivers = Gtk.Button(label="Remove drivers")
    btn_remove_printer_drivers.connect("clicked", self.on_click_remove_printer_drivers)
    hbox27.pack_start(hbox27_label, False, False, 10)
    hbox27.pack_end(btn_remove_printer_drivers, False, False, 10)
    hbox27.pack_end(btn_install_printer_drivers, False, False, 10)

    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox21_label = Gtk.Label(xalign=0)
    hbox21_label.set_text("   Install HP drivers")
    btn_install_hplip = Gtk.Button(label="Install hplip")
    btn_install_hplip.connect("clicked", self.on_click_install_hplip)
    btn_remove_hplip = Gtk.Button(label="Uninstall hplip")
    btn_remove_hplip.connect("clicked", self.on_click_remove_hplip)
    hbox21.pack_start(hbox21_label, False, False, 10)
    hbox21.pack_end(btn_remove_hplip, False, False, 10)
    hbox21.pack_end(btn_install_hplip, False, False, 10)

    # hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # btn_launch_system_config_printer = Gtk.Button(label="Launch system-config-printer")
    # btn_launch_system_config_printer.connect(
    #     "clicked", self.on_click_launch_system_config_printer
    # )
    # hbox23.pack_end(btn_launch_system_config_printer, True, True, 10)

    hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox22_label = Gtk.Label(xalign=0)
    hbox22_label.set_text(
        "Install configuration tool for cups \n(launch the app and add your printer)"
    )
    btn_install_system_config_printer = Gtk.Button(
        label="Install system-config-printer"
    )
    btn_install_system_config_printer.connect(
        "clicked", self.on_click_install_system_config_printer
    )
    btn_remove_system_config_printer = Gtk.Button(label="Remove system-config-printer")
    btn_remove_system_config_printer.connect(
        "clicked", self.on_click_remove_system_config_printer
    )
    hbox22.pack_start(hbox22_label, False, False, 10)
    hbox22.pack_end(btn_remove_system_config_printer, False, False, 10)
    hbox22.pack_end(btn_install_system_config_printer, False, False, 10)

    # at bottom of page
    hbox29 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    enable_cups = Gtk.Button(label="Enable cups")
    enable_cups.connect("clicked", self.on_click_enable_cups)
    disable_cups = Gtk.Button(label="Disable cups")
    disable_cups.connect("clicked", self.on_click_disable_cups)
    restart_cups = Gtk.Button(label="Start/Restart cups")
    restart_cups.connect("clicked", self.on_click_restart_cups)
    hbox29.pack_end(restart_cups, False, False, 10)
    hbox29.pack_start(enable_cups, False, False, 10)
    hbox29.pack_start(disable_cups, False, False, 10)

    hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox31_label = Gtk.Label(xalign=0)

    status1 = fn.check_service("cups")
    if status1 is True:
        status1 = "active"
    else:
        status1 = "inactive"

    status2 = fn.check_socket("cups")
    if status2 is True:
        status2 = "active"
    else:
        status2 = "inactive"

    hbox31_label.set_text("Cups service : " + status1 + "   Cups socket : " + status2)
    hbox31.pack_start(hbox31_label, False, False, 10)

    # hbox32 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox32_label = Gtk.Label(xalign=0)
    # hbox32_label.set_text(
    #     "Samba : " + status1 + "   Nmb : " + status2 + "   Avahi : " + status3
    # )
    # hbox32.pack_start(hbox32_label, False, False, 10)

    #     hbox95 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    #     hbox95_label = Gtk.Label(xalign=0)
    #     hbox95_label.set_text(
    #         "With the Avahi daemon (network discovery) running on both \
    # the server and client,\n\
    # the file manager on the client should automatically find the server- Beware of firewalls\n\
    # All computers in your network must have a unique name /etc/hostname"
    #     )
    #     restart_smb = Gtk.Button(label="Restart Smb")
    #     restart_smb.connect("clicked", self.on_click_restart_smb)
    #     hbox95.pack_start(hbox95_label, False, False, 10)
    #     hbox95.pack_end(restart_smb, False, False, 10)

    # ====================================================================
    #                       STACK
    # ====================================================================

    # network
    vboxstack1.pack_start(hbox2, False, False, 10)
    vboxstack1.pack_start(hbox3, False, False, 0)
    vboxstack1.pack_start(hbox30, False, False, 0)
    if fn.check_service("firewalld"):
        vboxstack1.pack_end(hbox92, False, False, 10)
    vboxstack1.pack_end(hbox91, False, False, 10)
    vboxstack1.pack_end(hbox93, False, False, 10)

    # samba easy
    vboxstack2.pack_start(hbox_header_samba, False, False, 10)
    vboxstack2.pack_start(hbox4, False, False, 0)
    vboxstack2.pack_start(hbox4bis, False, False, 0)
    vboxstack2.pack_start(hbox5, False, False, 0)
    vboxstack2.pack_start(hbox16, False, False, 10)
    vboxstack2.pack_start(hbox18, False, False, 10)
    vboxstack2.pack_end(hbox19, False, False, 10)
    vboxstack2.pack_end(hbox95, False, False, 10)
    vboxstack2.pack_end(hbox94, False, False, 10)

    # cups
    vboxstack3.pack_start(hbox15, False, False, 10)
    vboxstack3.pack_start(hbox8, False, False, 0)
    vboxstack3.pack_start(hbox20, False, False, 0)
    vboxstack3.pack_start(hbox26, False, False, 0)
    vboxstack3.pack_start(hbox27, False, False, 0)
    vboxstack3.pack_start(hbox21, False, False, 0)
    # vboxstack3.pack_start(hbox23, False, False, 10)
    vboxstack3.pack_start(hbox22, False, False, 10)
    vboxstack3.pack_end(hbox29, False, False, 10)
    vboxstack3.pack_end(hbox31, False, False, 10)

    # ==================================================================
    #                       BLUETOOTH TAB
    # ==================================================================

    # ==================================================================
    #                       AUDIO TAB
    # ==================================================================

    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================
    stack.add_titled(vboxstack1, "stack1", "Network")
    stack.add_titled(vboxstack2, "stack2", "Samba")
    stack.add_titled(vboxstack3, "stack3", "Printing")
    # stack.add_titled(vboxstack5, "stack4", "Bluetooth")
    # stack.add_titled(vboxstack6, "stack5", "Audio")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxstack14.pack_start(hbox1, False, False, 0)
    vboxstack14.pack_start(hbox0, False, False, 0)
    vboxstack14.pack_start(vbox, True, True, 0)
