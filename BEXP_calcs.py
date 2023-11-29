

# Valid Level Range
MIN_LEVEL       =   1
MAX_LEVEL       =   60
MAX_DISP_LEVEL  =   20

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

# Calculate BEXP Requirements to go from level to level
def calc_bexp_cost(start_lvl, end_lvl, lvl_mod, diff_mod):
    # Check that level selection was valid
    if(validate_level_range(start_lvl, end_lvl)):
        return INVALID_LVLS

    # Calculate total BEXP cost by summing BEXP cost at each level
    total = 0
    for lvl in range(start_lvl, end_lvl):
        total += int(diff_mod * ((50 * lvl_mod*lvl)+50))
    return total

# Check valid level range
# returns 0 on success, 1 on failure
def validate_level_range(start_lvl, end_lvl):
    if(start_lvl < MIN_LEVEL):
        return FAILURE
    if(end_lvl > MAX_LEVEL):
        return FAILURE
    if(end_lvl <= start_lvl):
        return FAILURE
    return SUCCESS

def convertToInternalLevel(tier, disp_lvl):
    return (tier*20) + disp_lvl