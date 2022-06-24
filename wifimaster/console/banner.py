from .io import IO


_MAIN_BANNER = r"""{}
--------------WIFIMASTER-------=>@yokai
                {}by EL sigei  ~  limit devices on your network :3
                                    v[_V_]

""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.Style.BRIGHT)


def get_main_banner(version):
    return _MAIN_BANNER.replace('[_V_]', version)
