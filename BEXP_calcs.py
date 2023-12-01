import math

# Valid Level Range
MIN_LEVEL           =   1
MAX_DISP_LVL_BEORC  =   20
MAX_TRUE_LVL_BEORC  =   60
MAX_DISP_LVL_LAGUZ  =   40
MAX_TRUE_LVL_LAGUZ  =   40

# Valid Tier Ranges (Laguz vs. Beorc)
MAX_TIERS_BEORC     =   3
MAX_TIERS_LAGUZ     =   1

# Difficulty Mode Multiplier
DIFF_MOD_EASY   =   2/3
DIFF_MOD_NORMAL =   1
DIFF_MOD_HARD   =   2

# Level Modifiers
LVL_MOD_BEORC   =   1
LVL_MOD_LAGUZ   =   1.5

# Return values
SUCCESS         =   0
FAILURE         =   1
INVALID_LVLS    =  -1

# Misc Constants
AUDIO_ON        =   1
AUDIO_OFF       =   0
RACE_BEORC      =   0
RACE_LAGUZ      =   1

# Calculate BEXP Requirements to go from level to level
def calc_bexp_cost(start_lvl, end_lvl, lvl_mod, diff_mod, race):
    # Check that level selection was valid
    if(validate_level_range(start_lvl, end_lvl, race)):
        return INVALID_LVLS

    # Calculate total BEXP cost by summing BEXP cost at each level
    total = 0
    for lvl in range(start_lvl, end_lvl):
        total += diff_mod * ((50 * (lvl_mod*(lvl)+1))+50)
    # Last minute rounding or sumn idk 
    # (refined through testing/comparing to real game)
    if((total - int(total) > 0.5)):
        return math.ceil(total)
    else:
        return math.floor(total)

# Check valid level range
# returns 0 on success, 1 on failure
def validate_level_range(start_lvl, end_lvl, race):
    if(race == RACE_BEORC):
        max_true_lvl = MAX_TRUE_LVL_BEORC
    else:
        max_true_lvl = MAX_TRUE_LVL_LAGUZ
    if(start_lvl < MIN_LEVEL):
        return FAILURE
    if(end_lvl > max_true_lvl):
        return FAILURE
    if(end_lvl < start_lvl):
        return FAILURE
    return SUCCESS

def convertToInternalLevel(tier, disp_lvl):
    return (tier*20) + disp_lvl