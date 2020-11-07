######IMPORTS & FUNCTIONS START#########
# External Import -> func_spacing
import func_spacing

space = " "
divider = "========"


# Internal Func
def tupspace():
    print(func_spacing.space(space))


def tupdivider():
    print(func_spacing.space(divider))


def combspacing():
    tupdivider()
    tupspace()


def minor_divide():
    print("--------")


######IMPORTS & FUNCTIONS END#########



info_dict2 = {
    "usr0": {
        "username": "Steve",
        "age": 23,
        "total_views": 2560
    },
    "usr1": {
        "username2": "JA",
        "age2": 25,
        "total_views2": 3460
    }

}


print(info_dict2)
