# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================
# pylint:disable=C0103,


def gui(self, Gtk, vboxstack25, design, fn):
    """create a gui"""
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("ArcoLinux projects")
    lbl1.set_name("title")
    hbox3.pack_start(lbl1, False, False, 0)

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)

    # ==========================================================
    #                     DESIGN
    # ==========================================================

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    vboxstack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxstack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

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
    #                       THEMES TAB
    # ==================================================================

    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10_label = Gtk.Label(xalign=0)
    hbox10_label.set_text(
        "Choose the project you like to install or remove and press apply\n\
We obey the dependencies of pacman"
    )
    hbox10.pack_start(hbox10_label, False, False, 10)

    # ARC THEMES
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.arcolinux_arc_aqua = Gtk.CheckButton(label="arcolinux-arc-aqua")
    self.arcolinux_arc_archlinux_blue = Gtk.CheckButton(
        label="arcolinux-arc-archlinux-blue"
    )
    self.arcolinux_arc_arcolinux_blue = Gtk.CheckButton(
        label="arcolinux-arc-arcolinux-blue"
    )
    self.arcolinux_arc_azul = Gtk.CheckButton(label="arcolinux-arc-azul")
    self.arcolinux_arc_azure_dodger_blue = Gtk.CheckButton(
        label="arcolinux-arc-azure-dodger-blue"
    )
    self.arcolinux_arc_blood = Gtk.CheckButton(label="arcolinux-arc-blood")
    self.arcolinux_arc_blue_sky = Gtk.CheckButton(label="arcolinux-arc-blue-sky")
    self.arcolinux_arc_botticelli = Gtk.CheckButton(label="arcolinux-arc-botticelli")
    self.arcolinux_arc_bright_lilac = Gtk.CheckButton(
        label="arcolinux-arc-bright-lilac"
    )
    self.arcolinux_arc_bright_lime_green = Gtk.CheckButton(
        label="arcolinux-arc-bright-lime-green"
    )
    self.arcolinux_arc_carnation = Gtk.CheckButton(label="arcolinux-arc-carnation")
    self.arcolinux_arc_carolina_blue = Gtk.CheckButton(
        label="arcolinux-arc-carolina-blue"
    )
    self.arcolinux_arc_casablanca = Gtk.CheckButton(label="arcolinux-arc-casablanca")
    self.arcolinux_arc_crimson = Gtk.CheckButton(label="arcolinux-arc-crimson")
    self.arcolinux_arc_dawn = Gtk.CheckButton(label="arcolinux-arc-dawn")
    self.arcolinux_arc_emerald = Gtk.CheckButton(label="arcolinux-arc-emerald")
    self.arcolinux_arc_evopop = Gtk.CheckButton(label="arcolinux-arc-evopop")
    self.arcolinux_arc_fern = Gtk.CheckButton(label="arcolinux-arc-fern")
    self.arcolinux_arc_fire = Gtk.CheckButton(label="arcolinux-arc-fire")
    self.arcolinux_arc_froly = Gtk.CheckButton(label="arcolinux-arc-froly")
    self.arcolinux_arc_havelock = Gtk.CheckButton(label="arcolinux-arc-havelock")
    self.arcolinux_arc_hibiscus = Gtk.CheckButton(label="arcolinux-arc-hibiscus")
    self.arcolinux_arc_light_blue_grey = Gtk.CheckButton(
        label="arcolinux-arc-light-blue-grey"
    )
    self.arcolinux_arc_light_blue_surfn = Gtk.CheckButton(
        label="arcolinux-arc-light-blue-surfn"
    )
    self.arcolinux_arc_light_salmon = Gtk.CheckButton(
        label="arcolinux-arc-light-salmon"
    )
    self.arcolinux_arc_mandy = Gtk.CheckButton(label="arcolinux-arc-mandy")
    self.arcolinux_arc_mantis = Gtk.CheckButton(label="arcolinux-arc-mantis")
    self.arcolinux_arc_medium_blue = Gtk.CheckButton(label="arcolinux-arc-medium-blue")
    self.arcolinux_arc_niagara = Gtk.CheckButton(label="arcolinux-arc-niagara")
    self.arcolinux_arc_nice_blue = Gtk.CheckButton(label="arcolinux-arc-nice-blue")
    self.arcolinux_arc_numix = Gtk.CheckButton(label="arcolinux-arc-numix")
    self.arcolinux_arc_orchid = Gtk.CheckButton(label="arcolinux-arc-orchid")
    self.arcolinux_arc_pale_grey = Gtk.CheckButton(label="arcolinux-arc-pale-grey")
    self.arcolinux_arc_paper = Gtk.CheckButton(label="arcolinux-arc-paper")
    self.arcolinux_arc_pink = Gtk.CheckButton(label="arcolinux-arc-pink")
    self.arcolinux_arc_polo = Gtk.CheckButton(label="arcolinux-arc-polo")
    self.arcolinux_arc_punch = Gtk.CheckButton(label="arcolinux-arc-punch")
    self.arcolinux_arc_red_orange = Gtk.CheckButton(label="arcolinux-arc-red-orange")
    self.arcolinux_arc_rusty_orange = Gtk.CheckButton(
        label="arcolinux-arc-rusty-orange"
    )
    self.arcolinux_arc_sky_blue = Gtk.CheckButton(label="arcolinux-arc-sky-blue")
    self.arcolinux_arc_slate_grey = Gtk.CheckButton(label="arcolinux-arc-slate-grey")
    self.arcolinux_arc_smoke = Gtk.CheckButton(label="arcolinux-arc-smoke")
    self.arcolinux_arc_soft_blue = Gtk.CheckButton(label="arcolinux-arc-soft-blue")
    self.arcolinux_arc_tacao = Gtk.CheckButton(label="arcolinux-arc-tacao")
    self.arcolinux_arc_tangerine = Gtk.CheckButton(label="arcolinux-arc-tangerinex")
    self.arcolinux_arc_tory = Gtk.CheckButton(label="arcolinux-arc-tory")
    self.arcolinux_arc_vampire = Gtk.CheckButton(label="arcolinux-arc-vampire")
    self.arcolinux_arc_warm_pink = Gtk.CheckButton(label="arcolinux-arc-warm-pink")

    flowbox = Gtk.FlowBox()
    flowbox.set_valign(Gtk.Align.START)
    flowbox.set_max_children_per_line(10)
    flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox.add(self.arcolinux_arc_aqua)
    flowbox.add(self.arcolinux_arc_archlinux_blue)
    flowbox.add(self.arcolinux_arc_arcolinux_blue)
    flowbox.add(self.arcolinux_arc_azul)
    flowbox.add(self.arcolinux_arc_azure_dodger_blue)
    flowbox.add(self.arcolinux_arc_blood)
    flowbox.add(self.arcolinux_arc_blue_sky)
    flowbox.add(self.arcolinux_arc_botticelli)
    flowbox.add(self.arcolinux_arc_bright_lilac)
    flowbox.add(self.arcolinux_arc_bright_lime_green)
    flowbox.add(self.arcolinux_arc_carnation)
    flowbox.add(self.arcolinux_arc_carolina_blue)
    flowbox.add(self.arcolinux_arc_casablanca)
    flowbox.add(self.arcolinux_arc_crimson)
    flowbox.add(self.arcolinux_arc_dawn)
    flowbox.add(self.arcolinux_arc_emerald)
    flowbox.add(self.arcolinux_arc_evopop)
    flowbox.add(self.arcolinux_arc_fern)
    flowbox.add(self.arcolinux_arc_fire)
    flowbox.add(self.arcolinux_arc_froly)
    flowbox.add(self.arcolinux_arc_havelock)
    flowbox.add(self.arcolinux_arc_hibiscus)
    flowbox.add(self.arcolinux_arc_light_blue_grey)
    flowbox.add(self.arcolinux_arc_light_blue_surfn)
    flowbox.add(self.arcolinux_arc_light_salmon)
    flowbox.add(self.arcolinux_arc_mandy)
    flowbox.add(self.arcolinux_arc_mantis)
    flowbox.add(self.arcolinux_arc_medium_blue)
    flowbox.add(self.arcolinux_arc_niagara)
    flowbox.add(self.arcolinux_arc_nice_blue)
    flowbox.add(self.arcolinux_arc_numix)
    flowbox.add(self.arcolinux_arc_orchid)
    flowbox.add(self.arcolinux_arc_pale_grey)
    flowbox.add(self.arcolinux_arc_paper)
    flowbox.add(self.arcolinux_arc_pink)
    flowbox.add(self.arcolinux_arc_polo)
    flowbox.add(self.arcolinux_arc_punch)
    flowbox.add(self.arcolinux_arc_red_orange)
    flowbox.add(self.arcolinux_arc_rusty_orange)
    flowbox.add(self.arcolinux_arc_sky_blue)
    flowbox.add(self.arcolinux_arc_slate_grey)
    flowbox.add(self.arcolinux_arc_smoke)
    flowbox.add(self.arcolinux_arc_soft_blue)
    flowbox.add(self.arcolinux_arc_tacao)
    flowbox.add(self.arcolinux_arc_tangerine)
    flowbox.add(self.arcolinux_arc_tory)
    flowbox.add(self.arcolinux_arc_vampire)
    flowbox.add(self.arcolinux_arc_warm_pink)

    hbox11.pack_start(flowbox, True, True, 10)

    hbox18 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label18 = Gtk.Label()
    label18.set_text("Choose what to select with a button")
    btn_all_selection = Gtk.Button(label="All")
    btn_all_selection.connect("clicked", self.on_click_att_theming_all_selection)
    btn_blue_selection = Gtk.Button(label="Blue")
    btn_blue_selection.connect("clicked", self.on_click_att_theming_blue_selection)
    btn_dark_selection = Gtk.Button(label="Dark")
    btn_dark_selection.connect("clicked", self.on_click_att_theming_dark_selection)
    btn_none_selection = Gtk.Button(label="None")
    btn_none_selection.connect("clicked", self.on_click_att_theming_none_selection)
    hbox18.pack_start(label18, False, False, 10)
    hbox18.pack_end(btn_none_selection, False, False, 10)
    hbox18.pack_end(btn_blue_selection, False, False, 10)
    hbox18.pack_end(btn_dark_selection, False, False, 10)
    hbox18.pack_end(btn_all_selection, False, False, 10)

    # at bottom
    hbox19 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_themes = Gtk.Button(label="Install the selected themes")
    button_install_themes.connect("clicked", self.on_install_att_themes_clicked)
    button_remove_themes = Gtk.Button(label="Uninstall the selected themes")
    button_remove_themes.connect("clicked", self.on_remove_att_themes_clicked)
    button_find_themes = Gtk.Button(label="Show the installed themes")
    button_find_themes.connect("clicked", self.on_find_att_themes_clicked)
    hbox19.pack_end(button_install_themes, False, False, 10)
    hbox19.pack_start(button_remove_themes, False, False, 10)
    hbox19.pack_start(button_find_themes, False, False, 10)

    # ==================================================================
    #                       ICONS TAB - SARDI
    # ==================================================================

    hbox20 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox20_label = Gtk.Label(xalign=0)
    hbox20_label.set_text(
        "Choose the project you like to install or remove and press apply\n\
We obey the dependencies of pacman"
    )
    hbox20.pack_start(hbox20_label, False, False, 10)

    hbox21 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.sardi_icons_att = Gtk.CheckButton(label="sardi-icons")
    self.sardi_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-colora-variations-icons-git"
    )
    self.sardi_flat_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-flat-colora-variations-icons-git"
    )
    self.sardi_flat_mint_y_icons_git = Gtk.CheckButton(
        label="sardi-flat-mint-y-icons-git"
    )
    self.sardi_flat_mixing_icons_git = Gtk.CheckButton(
        label="sardi-flat-mixing-icons-git"
    )
    self.sardi_flexible_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-flexible-colora-variations-icons-git"
    )
    self.sardi_flexible_luv_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-flexible-luv-colora-variations-icons-git"
    )
    self.sardi_flexible_mint_y_icons_git = Gtk.CheckButton(
        label="sardi-flexible-mint-y-icons-git"
    )
    self.sardi_flexible_mixing_icons_git = Gtk.CheckButton(
        label="sardi-flexible-mixing-icons-git"
    )
    self.sardi_flexible_variations_icons_git = Gtk.CheckButton(
        label="sardi-flexible-variations-icons-git"
    )
    self.sardi_ghost_flexible_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-ghost-flexible-colora-variations-icons-git"
    )
    self.sardi_ghost_flexible_mint_y_icons_git = Gtk.CheckButton(
        label="sardi-ghost-flexible-mint-y-icons-git"
    )
    self.sardi_ghost_flexible_mixing_icons_git = Gtk.CheckButton(
        label="sardi-ghost-flexible-mixing-icons-git"
    )
    self.sardi_ghost_flexible_variations_icons_git = Gtk.CheckButton(
        label="sardi-ghost-flexible-variations-icons-git"
    )
    self.sardi_mint_y_icons_git = Gtk.CheckButton(label="sardi-mint-y-icons-git")
    self.sardi_mixing_icons_git = Gtk.CheckButton(label="sardi-mixing-icons-git")
    self.sardi_mono_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-mono-colora-variations-icons-git"
    )
    self.sardi_mono_mint_y_icons_git = Gtk.CheckButton(
        label="sardi-mono-mint-y-icons-git"
    )
    self.sardi_mono_mixing_icons_git = Gtk.CheckButton(
        label="sardi-mono-mixing-icons-git"
    )
    self.sardi_mono_numix_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-mono-numix-colora-variations-icons-git"
    )
    self.sardi_mono_papirus_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-mono-papirus-colora-variations-icons-git"
    )
    self.sardi_orb_colora_mint_y_icons_git = Gtk.CheckButton(
        label="sardi-orb-colora-mint-y-icons-git"
    )
    self.sardi_orb_colora_mixing_icons_git = Gtk.CheckButton(
        label="sardi-orb-colora-mixing-icons-git"
    )
    self.sardi_orb_colora_variations_icons_git = Gtk.CheckButton(
        label="sardi-orb-colora-variations-icons-git"
    )

    flowbox = Gtk.FlowBox()
    flowbox.set_valign(Gtk.Align.START)
    flowbox.set_max_children_per_line(10)
    flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox.add(self.sardi_icons_att)
    flowbox.add(self.sardi_colora_variations_icons_git)
    flowbox.add(self.sardi_flat_colora_variations_icons_git)
    flowbox.add(self.sardi_flat_mint_y_icons_git)
    flowbox.add(self.sardi_flat_mixing_icons_git)
    flowbox.add(self.sardi_flexible_colora_variations_icons_git)
    flowbox.add(self.sardi_flexible_luv_colora_variations_icons_git)
    flowbox.add(self.sardi_flexible_mint_y_icons_git)
    flowbox.add(self.sardi_flexible_mixing_icons_git)
    flowbox.add(self.sardi_flexible_variations_icons_git)
    flowbox.add(self.sardi_ghost_flexible_colora_variations_icons_git)
    flowbox.add(self.sardi_ghost_flexible_mint_y_icons_git)
    flowbox.add(self.sardi_ghost_flexible_mixing_icons_git)
    flowbox.add(self.sardi_ghost_flexible_variations_icons_git)
    flowbox.add(self.sardi_mint_y_icons_git)
    flowbox.add(self.sardi_mixing_icons_git)
    flowbox.add(self.sardi_mono_colora_variations_icons_git)
    flowbox.add(self.sardi_mono_mint_y_icons_git)
    flowbox.add(self.sardi_mono_mixing_icons_git)
    flowbox.add(self.sardi_mono_numix_colora_variations_icons_git)
    flowbox.add(self.sardi_mono_papirus_colora_variations_icons_git)
    flowbox.add(self.sardi_orb_colora_mint_y_icons_git)
    flowbox.add(self.sardi_orb_colora_mixing_icons_git)
    flowbox.add(self.sardi_orb_colora_variations_icons_git)

    hbox21.pack_start(flowbox, True, True, 10)

    hbox23 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label13 = Gtk.Label()
    label13.set_text("Choose what to select with a button")
    btn_all_selection = Gtk.Button(label="All")
    btn_all_selection.connect(
        "clicked", self.on_click_att_sardi_icon_theming_all_selection
    )
    btn_mint_selection = Gtk.Button(label="Mint")
    btn_mint_selection.connect(
        "clicked", self.on_click_att_sardi_icon_theming_mint_selection
    )
    btn_mixing_selection = Gtk.Button(label="Mixing")
    btn_mixing_selection.connect(
        "clicked", self.on_click_att_sardi_icon_theming_mixing_selection
    )
    btn_variation_selection = Gtk.Button(label="Variations")
    btn_variation_selection.connect(
        "clicked", self.on_click_att_sardi_icon_theming_variations_selection
    )
    btn_none_selection = Gtk.Button(label="None")
    btn_none_selection.connect(
        "clicked", self.on_click_att_sardi_icon_theming_none_selection
    )
    hbox23.pack_start(label13, False, False, 10)
    hbox23.pack_start(btn_all_selection, False, False, 10)
    hbox23.pack_start(btn_variation_selection, False, False, 10)
    hbox23.pack_start(btn_mixing_selection, False, False, 10)
    hbox23.pack_start(btn_mint_selection, False, False, 10)
    hbox23.pack_start(btn_none_selection, False, False, 10)

    # families
    hbox22 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label13 = Gtk.Label()
    label13.set_text("Choose the family with a button")
    btn_sardi_fam = Gtk.Button(label="Sardi")
    btn_sardi_fam.connect(
        "clicked", self.on_click_att_fam_sardi_icon_theming_sardi_selection
    )
    btn_sardi_flexible_fam = Gtk.Button(label="Sardi Flexible")
    btn_sardi_flexible_fam.connect(
        "clicked", self.on_click_att_fam_sardi_icon_theming_sardi_flexible_selection
    )
    btn_sardi_mono_fam = Gtk.Button(label="Sardi Mono")
    btn_sardi_mono_fam.connect(
        "clicked", self.on_click_att_fam_sardi_icon_theming_sardi_mono_selection
    )
    btn_sardi_flat_fam = Gtk.Button(label="Sardi Flat")
    btn_sardi_flat_fam.connect(
        "clicked", self.on_click_att_fam_sardi_icon_theming_sardi_flat_selection
    )
    btn_sardi_ghost_fam = Gtk.Button(label="Sardi Ghost")
    btn_sardi_ghost_fam.connect(
        "clicked", self.on_click_att_fam_sardi_icon_theming_sardi_ghost_selection
    )
    btn_sardi_orb_fam = Gtk.Button(label="Sardi Orb")
    btn_sardi_orb_fam.connect(
        "clicked", self.on_click_att_fam_sardi_icon_theming_sardi_orb_selection
    )
    hbox22.pack_start(label13, False, False, 10)
    hbox22.pack_start(btn_sardi_fam, False, False, 10)
    hbox22.pack_start(btn_sardi_flexible_fam, False, False, 10)
    hbox22.pack_start(btn_sardi_mono_fam, False, False, 10)
    hbox22.pack_start(btn_sardi_flat_fam, False, False, 10)
    hbox22.pack_start(btn_sardi_ghost_fam, False, False, 10)
    hbox22.pack_start(btn_sardi_orb_fam, False, False, 10)

    hbox29 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_sardi = Gtk.Button(label="Install the selected icon themes")
    button_install_sardi.connect(
        "clicked", self.on_install_att_sardi_icon_themes_clicked
    )
    button_find_sardi_icons = Gtk.Button(label="Show the installed icon themes")
    button_find_sardi_icons.connect(
        "clicked", self.on_find_att_sardi_icon_themes_clicked
    )
    button_remove_sardi_icons = Gtk.Button(label="Uninstall the selected icon themes")
    button_remove_sardi_icons.connect(
        "clicked", self.on_remove_att_sardi_icon_themes_clicked
    )
    hbox29.pack_start(button_remove_sardi_icons, False, False, 10)
    hbox29.pack_start(button_find_sardi_icons, False, False, 10)
    hbox29.pack_end(button_install_sardi, False, False, 10)

    # ==================================================================
    #                       ICONS TAB - SURFN
    # ==================================================================

    hbox30 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox30_label = Gtk.Label(xalign=0)
    hbox30_label.set_text(
        "Choose the project you like to install or remove and press apply\n\
We obey the dependencies of pacman"
    )
    hbox30.pack_start(hbox30_label, False, False, 10)

    hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.surfn_icons_git_att = Gtk.CheckButton(label="surfn-icons-git")
    self.surfn_arc_breeze_icons_git = Gtk.CheckButton(
        label="surfn-arc-breeze-icons-git"
    )
    self.surfn_mint_y_icons_git = Gtk.CheckButton(label="surfn-mint-y-icons-git")
    self.surfn_plasma_dark = Gtk.CheckButton(label="surfn-plasma-dark")
    self.surfn_plasma_dark_tela = Gtk.CheckButton(label="surfn-plasma-dark-tela")
    self.surfn_plasma_light = Gtk.CheckButton(label="surfn-plasma-light")

    flowbox = Gtk.FlowBox()
    flowbox.set_valign(Gtk.Align.START)
    flowbox.set_max_children_per_line(10)
    flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox.add(self.surfn_icons_git_att)
    flowbox.add(self.surfn_arc_breeze_icons_git)
    flowbox.add(self.surfn_mint_y_icons_git)
    flowbox.add(self.surfn_plasma_dark)
    flowbox.add(self.surfn_plasma_dark_tela)
    flowbox.add(self.surfn_plasma_light)

    hbox31.pack_start(flowbox, True, True, 10)

    hbox32 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label13 = Gtk.Label()
    label13.set_text("Choose what to select with a button")
    btn_all_selection = Gtk.Button(label="All")
    btn_all_selection.connect("clicked", self.on_click_att_surfn_theming_all_selection)
    # btn_normal_selection = Gtk.Button(label="Normal")
    # btn_normal_selection.connect(
    #     "clicked", self.on_click_att_surfn_theming_normal_selection
    # )
    # btn_small_selection = Gtk.Button(label="Minimal")
    # btn_small_selection.connect(
    #     "clicked", self.on_click_att_surfn_theming_minimal_selection
    # )
    btn_none_selection = Gtk.Button(label="None")
    btn_none_selection.connect(
        "clicked", self.on_click_att_surfn_theming_none_selection
    )
    hbox32.pack_start(label13, False, False, 10)
    hbox32.pack_end(btn_none_selection, False, False, 10)
    # hbox32.pack_end(btn_small_selection, False, False, 10)
    # hbox32.pack_end(btn_normal_selection, False, False, 10)
    hbox32.pack_end(btn_all_selection, False, False, 10)

    hbox39 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_surfn_icons = Gtk.Button(label="Install the selected cursor themes")
    button_install_surfn_icons.connect(
        "clicked", self.on_install_att_surfn_icon_themes_clicked
    )
    button_find_surfn_icons = Gtk.Button(label="Show the installed icon themes")
    button_find_surfn_icons.connect(
        "clicked", self.on_find_att_surfn_icon_themes_clicked
    )
    button_remove_surfn_icons = Gtk.Button(label="Uninstall the selected cursor themes")
    button_remove_surfn_icons.connect(
        "clicked", self.on_remove_att_surfn_icon_themes_clicked
    )
    hbox39.pack_start(button_remove_surfn_icons, False, False, 10)
    hbox39.pack_start(button_find_surfn_icons, False, False, 10)
    hbox39.pack_end(button_install_surfn_icons, False, False, 10)

    # ==================================================================
    #                       EXTRAS TAB
    # ==================================================================

    hbox40 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox40_label = Gtk.Label(xalign=0)
    hbox40_label.set_text(
        "Choose the project you like to install or remove and press apply\n\
We obey the dependencies of pacman"
    )
    hbox40.pack_start(hbox40_label, False, False, 10)

    hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.att_candy_beauty = Gtk.CheckButton(label="ArcoLinux Candy Beauty")
    self.edu_candy_beauty_arc = Gtk.CheckButton(label="Edu Candy Beauty Arc")
    self.edu_candy_beauty_arc_mint_grey = Gtk.CheckButton(
        label="Edu Candy Beauty Arc Mint Grey"
    )
    self.edu_candy_beauty_arc_mint_red = Gtk.CheckButton(
        label="Edu Candy Beauty Arc Mint Red"
    )
    self.edu_candy_beauty_tela = Gtk.CheckButton(label="Edu Candy Beauty Tela")
    self.edu_papirus_dark_tela = Gtk.CheckButton(label="Edu Papirus Dark Tela")
    self.edu_papirus_dark_tela_grey = Gtk.CheckButton(
        label="Edu Papirus Dark Tela Grey "
    )
    self.edu_vimix_dark_tela = Gtk.CheckButton(label="Edu Vimix Dark Tela")

    flowbox = Gtk.FlowBox()
    flowbox.set_valign(Gtk.Align.START)
    flowbox.set_max_children_per_line(10)
    flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

    flowbox.add(self.att_candy_beauty)
    flowbox.add(self.edu_candy_beauty_arc)
    flowbox.add(self.edu_candy_beauty_arc_mint_grey)
    flowbox.add(self.edu_candy_beauty_arc_mint_red)
    flowbox.add(self.edu_candy_beauty_tela)
    flowbox.add(self.edu_papirus_dark_tela)
    flowbox.add(self.edu_papirus_dark_tela_grey)
    flowbox.add(self.edu_vimix_dark_tela)

    hbox41.pack_start(flowbox, True, True, 10)

    hbox42 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label13 = Gtk.Label()
    label13.set_text("Choose what to select with a button")
    btn_all_selection = Gtk.Button(label="All")
    btn_all_selection.connect("clicked", self.on_click_extras_theming_all_selection)
    btn_none_selection = Gtk.Button(label="None")
    btn_none_selection.connect("clicked", self.on_click_extras_theming_none_selection)
    hbox42.pack_start(label13, False, False, 10)
    hbox42.pack_end(btn_none_selection, False, False, 10)
    hbox42.pack_end(btn_all_selection, False, False, 10)

    hbox49 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    button_install_themes = Gtk.Button(label="Install the selected packages")
    button_install_themes.connect("clicked", self.on_install_extras_clicked)
    button_find_themes = Gtk.Button(label="Show  the installed packages")
    button_find_themes.connect("clicked", self.on_find_extras_clicked)
    button_remove_themes = Gtk.Button(label="Uninstall the selected packages")
    button_remove_themes.connect("clicked", self.on_remove_extras_clicked)
    hbox49.pack_start(button_remove_themes, False, False, 10)
    hbox49.pack_start(button_find_themes, False, False, 10)
    hbox49.pack_end(button_install_themes, False, False, 10)

    # ====================================================================
    #                       STACK
    # ====================================================================

    # themes
    vboxstack1.pack_start(hbox10, False, False, 0)
    vboxstack1.pack_start(hbox11, False, False, 10)
    vboxstack1.pack_start(hbox18, False, False, 10)
    vboxstack1.pack_end(hbox19, False, False, 10)

    # icons
    vboxstack2.pack_start(hbox20, False, False, 10)
    vboxstack2.pack_start(hbox21, False, False, 10)
    vboxstack2.pack_start(hbox23, False, False, 10)
    vboxstack2.pack_start(hbox22, False, False, 10)
    # vboxstack2.pack_start(hbox23, False, False, 10)

    vboxstack2.pack_end(hbox29, False, False, 0)
    # vboxstack2.pack_start(hbox4bis, False, False, 0)
    # vboxstack2.pack_start(hbox5, False, False, 0)
    # vboxstack2.pack_start(hbox16, False, False, 10)
    # vboxstack2.pack_start(hbox18, False, False, 10)
    # vboxstack2.pack_end(hbox19, False, False, 10)
    # vboxstack2.pack_end(hbox95, False, False, 10)
    # vboxstack2.pack_end(hbox94, False, False, 10)

    # cursors
    vboxstack3.pack_start(hbox30, False, False, 10)
    vboxstack3.pack_start(hbox31, False, False, 10)
    vboxstack3.pack_start(hbox32, False, False, 10)
    vboxstack3.pack_end(hbox39, False, False, 0)
    # vboxstack3.pack_start(hbox20, False, False, 0)
    # vboxstack3.pack_start(hbox26, False, False, 0)
    # vboxstack3.pack_start(hbox27, False, False, 0)
    # vboxstack3.pack_start(hbox21, False, False, 0)
    # vboxstack3.pack_start(hbox22, False, False, 10)
    # vboxstack3.pack_end(hbox29, False, False, 10)
    # vboxstack3.pack_end(hbox31, False, False, 10)

    # fonts
    vboxstack4.pack_start(hbox40, False, False, 10)
    vboxstack4.pack_start(hbox41, False, False, 10)
    vboxstack4.pack_start(hbox42, False, False, 10)
    vboxstack4.pack_end(hbox49, False, False, 0)
    # vboxstack4.pack_start(hbox42, False, False, 0)
    # vboxstack4.pack_end(hbox48, False, False, 10)

    # ==================================================================
    #                       PACK TO STACK
    # ==================================================================
    stack.add_titled(vboxstack1, "stack1", "Themes")
    stack.add_titled(vboxstack2, "stack2", "Icons - Sardi")
    stack.add_titled(vboxstack3, "stack3", "Icons - Surfn")
    stack.add_titled(vboxstack4, "stack4", "Extras")

    vbox.pack_start(stack_switcher, False, False, 0)
    vbox.pack_start(stack, True, True, 0)

    vboxstack25.pack_start(hbox3, False, False, 0)
    vboxstack25.pack_start(hbox4, False, False, 0)
    vboxstack25.pack_start(vbox, True, True, 0)
