# =================================================================
# =          Author: Cameron Percival
# =================================================================

import os
import Functions

#This function has one job, and one job only; ensure that check boxes match what is passed to it, based on the logic from the calling function
def set_util_state(self, util, util_state, lolcat_state):
    if util == "neofetch":
        self.neofetch_lolcat.set_active(lolcat_state)
        self.neofetch_util.set_active(util_state)
        self.neo_lolcat.set_active(lolcat_state)
    elif util == "screenfetch":
        self.screenfetch_lolcat.set_active(lolcat_state)
        self.screenfetch_util.set_active(util_state)
    elif util == "ufetch":
        self.ufetch_lolcat.set_active(lolcat_state)
        self.ufetch_util.set_active(util_state)
    elif util == "ufetch-arco":
        self.ufetch_arco_lolcat.set_active(lolcat_state)
        self.ufetch_arco_util.set_active(util_state)
    elif util == "pfetch":
        self.pfetch_lolcat.set_active(lolcat_state)
        self.pfetch_util.set_active(util_state)
    elif util == "paleofetch":
        self.paleofetch_lolcat.set_active(lolcat_state)
        self.paleofetch_util.set_active(util_state)
    elif util == "alsi":
        self.alsi_lolcat.set_active(lolcat_state)
        self.alsi_util.set_active(util_state)
    elif util == "hfetch":
        self.hfetch_lolcat.set_active(lolcat_state)
        self.hfetch_util.set_active(util_state)
    elif util == "sfetch":
        self.sfetch_lolcat.set_active(lolcat_state)
        self.sfetch_util.set_active(util_state)
    elif util == "sysinfo":
        self.sysinfo_lolcat.set_active(lolcat_state)
        self.sysinfo_util.set_active(util_state)
    elif util == "sysinfo-retro":
        self.sysinfo_retro_lolcat.set_active(lolcat_state)
        self.sysinfo_retro_util.set_active(util_state)
    else:
        print("You should not be here. Something has been input incorrectly.")

def install_util(util):
    command = ""
    if util == "neofetch":
        command = 'pacman -S neofetch arcolinux-neofetch-git --noconfirm --needed'
    elif util == "screenfetch":
        command = 'pacman -S screenfetch --noconfirm --needed'
    elif util == "ufetch":
        command = 'pacman -S ufetch-git --noconfirm --needed'
    elif util == "ufetch-arco":
        command = 'pacman -S ufetch-arco-git --noconfirm --needed'
    elif util == "pfetch":
        command = 'pacman -S pfetch --noconfirm --needed'
    elif util == "paleofetch":
        command = 'pacman -S arcolinux-paleofetch-git --noconfirm --needed'
    elif util == "alsi":
        command = 'pacman -S alsi --noconfirm --needed'
    #elif util == "hfetch":
    #    command = 'pacman -S sddm --noconfirm --needed'
    #elif util == "sfetch":
    #    command = 'pacman -S sddm --noconfirm --needed'
    #elif util == "sysinfo":
    #    command = 'pacman -S sddm --noconfirm --needed'
    #elif util == "sysinfo-retro":
    #    command = 'pacman -S sddm --noconfirm --needed'
    elif util == "lolcat":
        command = 'pacman -S lolcat --noconfirm --needed'
    else:
        pass

    #This is just protection to avoid unneeded errors.
    if len(command)>0:
        Functions.subprocess.call(command.split(" "),
                        shell=False,
                        stdout=Functions.subprocess.PIPE,
                        stderr=Functions.subprocess.STDOUT)
