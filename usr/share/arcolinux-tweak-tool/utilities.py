# =================================================================
# =          Author: Cameron Percival
# =================================================================

import os
import Functions

#This function has one job, and one job only; ensure that check boxes match what is passed to it, based on the logic from the calling function
def set_util_state(self, util, util_state, lolcat_state):
    if util == "neofetch":
        self.neofetch_lolcat.set_state(lolcat_state)
        self.neofetch_util.set_state(util_state)
        self.neo_lolcat.set_state(lolcat_state)
        self.neo_util.set_state(lolcat_state)
    elif util == "screenfetch":
        self.screenfetch_lolcat.set_state(lolcat_state)
        self.screenfetch_util.set_state(util_state)
    elif util == "ufetch":
        self.ufetch_lolcat.set_state(lolcat_state)
        self.ufetch_util.set_state(util_state)
    elif util == "ufetch-arco":
        self.ufetch_arco_lolcat.set_state(lolcat_state)
        self.ufetch_arco_util.set_state(util_state)
    elif util == "pfetch":
        self.pfetch_lolcat.set_state(lolcat_state)
        self.pfetch_util.set_state(util_state)
    elif util == "paleofetch":
        self.paleofetch_lolcat.set_state(lolcat_state)
        self.paleofetch_util.set_state(util_state)
    elif util == "alsi":
        self.alsi_lolcat.set_state(lolcat_state)
        self.alsi_util.set_state(util_state)
    elif util == "hfetch":
        self.hfetch_lolcat.set_state(lolcat_state)
        self.hfetch_util.set_state(util_state)
    elif util == "fetch":
        self.fetch_lolcat.set_state(lolcat_state)
        self.fetch_util.set_state(util_state)
    elif util == "sfetch":
        self.sfetch_lolcat.set_state(lolcat_state)
        self.sfetch_util.set_state(util_state)
    elif util == "sysinfo":
        self.sysinfo_lolcat.set_state(lolcat_state)
        self.sysinfo_util.set_state(util_state)
    elif util == "sysinfo-retro":
        self.sysinfo_retro_lolcat.set_state(lolcat_state)
        self.sysinfo_retro_util.set_state(util_state)
    else:
        print("You should not be here. Something has been input incorrectly.")

def get_util_state(self, util):
    if util == "neofetch":
        return self.neofetch_util.get_active()
    elif util == "screenfetch":
        return self.screenfetch_util.get_active()
    elif util == "ufetch":
        return self.ufetch_util.get_active()
    elif util == "ufetch-arco":
        return self.ufetch_arco_util.get_active()
    elif util == "pfetch":
        return self.pfetch_util.get_active()
    elif util == "paleofetch":
        return self.paleofetch_util.get_active()
    elif util == "alsi":
        return self.alsi_util.get_active()
    elif util == "hfetch":
        return self.hfetch_util.get_active()
    elif util == "fetch":
        return self.fetch_util.get_active()
    elif util == "sfetch":
        return self.sfetch_util.get_active()
    elif util == "sysinfo":
        return self.sysinfo_util.get_active()
    elif util == "sysinfo-retro":
        return self.sysinfo_retro_util.get_active()
    else:
        print("Get Util State error. Something has been input incorrectly.")
        return False

def get_lolcat_state(self, util):
    if util == "neofetch":
        return self.neofetch_lolcat.get_active()
    elif util == "screenfetch":
        return self.screenfetch_lolcat.get_active()
    elif util == "ufetch":
        return self.ufetch_lolcat.get_active()
    elif util == "ufetch-arco":
        return self.ufetch_arco_lolcat.get_active()
    elif util == "pfetch":
        return self.pfetch_lolcat.get_active()
    elif util == "paleofetch":
        return self.paleofetch_lolcat.get_active()
    elif util == "alsi":
        return self.alsi_lolcat.get_active()
    elif util == "hfetch":
        return self.hfetch_lolcat.get_active()
    elif util == "fetch":
        return self.fetch_lolcat.get_active()
    elif util == "sfetch":
        return self.sfetch_lolcat.get_active()
    elif util == "sysinfo":
        return self.sysinfo_lolcat.get_active()
    elif util == "sysinfo-retro":
        return self.sysinfo_retro_lolcat.get_active()
    else:
        print("Get lolcat state error. Something has been input incorrectly.")
        return False

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
    elif util == "hfetch":
        command = 'pacman -S arcolinux-bin-git --noconfirm --needed'
    elif util == "sfetch":
        command = 'pacman -S arcolinux-bin-git --noconfirm --needed'
    elif util == "fetch":
        command = 'pacman -S arcolinux-bin-git --noconfirm --needed'
    elif util == "sysinfo":
        command = 'pacman -S arcolinux-bin-git --noconfirm --needed'
    elif util == "sysinfo-retro":
        command = 'pacman -S arcolinux-bin-git --noconfirm --needed'
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

def _get_position(lists, value):
    data = []
    #Because we don't know EXACTLY how the app will process the rc file, we need to account for every variation.
    special_cases = ["fetch", "fetch | lolcat", "fetch\n", "fetch | lolcat\n", "#fetch", "#fetch | lolcat", "#fetch\n", "#fetch | lolcat\n"] #
    is_special = False

    if value == "fetch":
        is_special = True

    for string in lists:
        if is_special:
            for item in special_cases:
                if string == item:
                    data.append(string)
        else:
            if value in string:
                data.append(string)

    position = lists.index(data[0])
    return position

def write_configs(utility, util_str):
    configs = [Functions.bash_config, Functions.zsh_config]
    for config in configs:
        with open(config, "r") as f:
            lines = f.readlines()
            f.close()
            try:
                pos = _get_position(lines, utility)
                lines[pos] = util_str + "\n"
            #this will cover use cases where the util is not in the rc files
            except Exception as e:
                print(e)
                #lines.append(util_str)
        with open(config, "w") as f:
            f.writelines(lines)
            f.close()
