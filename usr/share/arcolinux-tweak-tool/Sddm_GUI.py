#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================


def GUI(self, Gtk, GdkPixbuf, vboxStack10, sddm, Functions):
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Sddm Configuration")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox5.pack_start(hseparator, True, True, 0)
    hbox4.pack_start(lbl1, False, False, 0)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label(xalign=0)
    label.set_text("Autologin")

    label1 = Gtk.Label(xalign=0)
    label1.set_text("Desktop session")

    label_note = Gtk.Label(xalign=0)
    label_note.set_text("Choose the desktop you want to autologin to")

    self.autologin_sddm = Gtk.Switch()
    self.autologin_sddm.connect("notify::active", self.on_autologin_sddm_activated)

    self.sessions_sddm = Gtk.ComboBoxText()
    sddm.pop_box(self, self.sessions_sddm)

    label_theme = Gtk.Label(xalign=0)
    label_theme.set_text("Choose the Sddm theme")

    label2 = Gtk.Label(xalign=0)
    label2.set_text("Theme")
    
    label_empty1 = Gtk.Label(xalign=0)
    label_empty1.set_text("")
    
    label_empty2 = Gtk.Label(xalign=0)
    label_empty2.set_text("")

    self.theme_sddm = Gtk.ComboBoxText()

    sddm.pop_theme_box(self, self.theme_sddm)


    apply_sddm = Gtk.Button(label="Apply settings")
    apply_sddm.connect("clicked", self.on_click_sddm_apply)
    
    reset_sddm = Gtk.Button(label="Reset")
    reset_sddm.connect("clicked", self.on_click_sddm_reset)


    hbox.pack_start(label, False, False, 10)
    hbox.pack_end(self.autologin_sddm, False, False, 10)

    hbox3.pack_start(label_note, False, False, 10)

    hbox1.pack_start(label1, False, False, 10)
    hbox1.pack_end(self.sessions_sddm, True, True, 10)
    
    hbox6.pack_start(label_theme, False, False, 10)
    
    hbox7.pack_start(label_empty1, False, False, 10)
    
    hbox8.pack_start(label_empty2, False, False, 10)
    
    hbox4.pack_start(label2, False, False, 10)
    hbox4.pack_end(self.theme_sddm, True, True, 10) 

    hbox2.pack_end(apply_sddm, False, False, 0)
    hbox2.pack_end(reset_sddm, False, False, 0)

    vboxStack10.pack_start(hbox5, False, False, 10)
    vboxStack10.pack_start(hbox, False, False, 0)
    vboxStack10.pack_start(hbox7, False, False, 0)
    vboxStack10.pack_start(hbox3, False, False, 0)
    vboxStack10.pack_start(hbox1, False, False, 0)
    vboxStack10.pack_start(hbox8, False, False, 0)
    vboxStack10.pack_start(hbox6, False, False, 0)
    vboxStack10.pack_start(hbox4, False, False, 0)
    vboxStack10.pack_end(hbox2, False, False, 0)
