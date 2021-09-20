# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack9, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Utilities Enabler")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    vbox14 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #Every util needs to have a util switch, and a lolcat switch.
    utils = [ "neofetch", "screenfetch", "ufetch", "ufetch-arco", "pfetch", "paleofetch", "alsi", "hfetch", "sfetch", "sysinfo", "sysinfo-retro" ]


    util_switches = [ ]
    self.neofetch_util = Gtk.Switch()
    self.screenfetch_util = Gtk.Switch()
    self.ufetch_util = Gtk.Switch()
    self.ufetch_arco_util = Gtk.Switch()
    self.pfetch_util = Gtk.Switch()
    self.paleofetch_util = Gtk.Switch()
    self.alsi_util = Gtk.Switch()
    self.hfetch_util = Gtk.Switch()
    self.sfetch_util = Gtk.Switch()
    self.sysinfo_util = Gtk.Switch()
    self.sysinfo_retro_util = Gtk.Switch()
    util_switches.append(self.neofetch_util)
    util_switches.append(self.screenfetch_util)
    util_switches.append(self.ufetch_util)
    util_switches.append(self.ufetch_arco_util)
    util_switches.append(self.pfetch_util)
    util_switches.append(self.paleofetch_util)
    util_switches.append(self.alsi_util)
    util_switches.append(self.hfetch_util)
    util_switches.append(self.sfetch_util)
    util_switches.append(self.sysinfo_util)
    util_switches.append(self.sysinfo_retro_util)

    lolcat_switches = [ ]
    self.neofetch_lolcat = Gtk.Switch()
    self.screenfetch_lolcat = Gtk.Switch()
    self.ufetch_lolcat = Gtk.Switch()
    self.ufetch_arco_lolcat = Gtk.Switch()
    self.pfetch_lolcat = Gtk.Switch()
    self.paleofetch_lolcat = Gtk.Switch()
    self.alsi_lolcat = Gtk.Switch()
    self.hfetch_lolcat = Gtk.Switch()
    self.sfetch_lolcat = Gtk.Switch()
    self.sysinfo_lolcat = Gtk.Switch()
    self.sysinfo_retro_lolcat = Gtk.Switch()
    lolcat_switches.append(self.neofetch_lolcat)
    lolcat_switches.append(self.screenfetch_lolcat)
    lolcat_switches.append(self.ufetch_lolcat)
    lolcat_switches.append(self.ufetch_arco_lolcat)
    lolcat_switches.append(self.pfetch_lolcat)
    lolcat_switches.append(self.paleofetch_lolcat)
    lolcat_switches.append(self.alsi_lolcat)
    lolcat_switches.append(self.hfetch_lolcat)
    lolcat_switches.append(self.sfetch_lolcat)
    lolcat_switches.append(self.sysinfo_lolcat)
    lolcat_switches.append(self.sysinfo_retro_lolcat)

    #Now we take all the prepared containers and switches, and create a page out of them.
    for i in range(len(utils)):
        util_hbox = (Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10))
        util_label = Gtk.Label(xalign=0)
        util_label.set_text(utils[i].capitalize())
        util_switches[i].connect("notify::active", self.util_toggle, utils[i])
        lolcat_switches[i].connect("notify::active", self.lolcat_toggle, utils[i])
        lolcat_label = Gtk.Label(xalign=0)
        lolcat_label.set_markup("Use lolcat")
        util_hbox.pack_start(util_label, False, False, 0)
        util_hbox.pack_start(util_switches[i], False, False, 0)
        util_hbox.pack_start(lolcat_label, False, False, 0)
        util_hbox.pack_start(lolcat_switches[i], False, False, 0)
        vbox14.pack_start(util_hbox, False, False, 0)

    vboxStack9.pack_start(hbox3, False, False, 0)
    vboxStack9.pack_start(hbox4, False, False, 0)
    vboxStack9.pack_start(vbox14, False, False, 0)
