from typing import Optional

import bisect

from tangled_up_in_unicode.u14_0_0_data.prop_list_to_property import prop_list_to_property
from tangled_up_in_unicode.u14_0_0_data.blocks_to_block_start import blocks_to_block_start
from tangled_up_in_unicode.u14_0_0_data.blocks_to_block_end import blocks_to_block_end
from tangled_up_in_unicode.u14_0_0_data.property_value_alias_age_short_to_long import property_value_alias_age_short_to_long
from tangled_up_in_unicode.u14_0_0_data.property_value_alias_bc_short_to_long import property_value_alias_bc_short_to_long
from tangled_up_in_unicode.u14_0_0_data.property_value_alias_blk_long_to_short import property_value_alias_blk_long_to_short
from tangled_up_in_unicode.u14_0_0_data.property_value_alias_ccc_short_to_long import property_value_alias_ccc_short_to_long
from tangled_up_in_unicode.u14_0_0_data.property_value_alias_ea_short_to_long import property_value_alias_ea_short_to_long
from tangled_up_in_unicode.u14_0_0_data.property_value_alias_gc_short_to_long import property_value_alias_gc_short_to_long
from tangled_up_in_unicode.u14_0_0_data.property_value_alias_sc_long_to_short import property_value_alias_sc_long_to_short
from tangled_up_in_unicode.u14_0_0_data.scripts_to_script_start import scripts_to_script_start
from tangled_up_in_unicode.u14_0_0_data.scripts_to_script_end import scripts_to_script_end
from tangled_up_in_unicode.u14_0_0_data.east_asian_width_to_east_asian_width_start import east_asian_width_to_east_asian_width_start
from tangled_up_in_unicode.u14_0_0_data.east_asian_width_to_east_asian_width_end import east_asian_width_to_east_asian_width_end
from tangled_up_in_unicode.u14_0_0_data.derived_age_to_age_start import derived_age_to_age_start
from tangled_up_in_unicode.u14_0_0_data.derived_age_to_age_end import derived_age_to_age_end
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_name_start import unicode_data_to_name_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_category_start import unicode_data_to_category_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_category_end import unicode_data_to_category_end
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_bidirectional_start import unicode_data_to_bidirectional_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_bidirectional_end import unicode_data_to_bidirectional_end
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_decimal_start import unicode_data_to_decimal_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_digit_start import unicode_data_to_digit_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_numeric_start import unicode_data_to_numeric_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_combining_start import unicode_data_to_combining_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_mirrored_start import unicode_data_to_mirrored_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_mirrored_end import unicode_data_to_mirrored_end
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_decomposition_start import unicode_data_to_decomposition_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_uppercase_start import unicode_data_to_uppercase_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_lowercase_start import unicode_data_to_lowercase_start
from tangled_up_in_unicode.u14_0_0_data.unicode_data_to_titlecase_start import unicode_data_to_titlecase_start

unidata_version = "14.0.0"


def name(chr: str, default=None) -> str:
    """Returns the name assigned to the character chr as a string.
    If no name is defined, default is returned, or, if not given, ValueError is raised."""
    idx = ord(chr)
    try:
        return unicode_data_to_name_start[idx]
    except KeyError:
        if default is None:
            raise ValueError("no such name")
        else:
            return default


def category(chr: str) -> str:
    """Returns the general category assigned to the character chr as string."""
    idx = ord(chr)
    start_keys = sorted(unicode_data_to_category_start.keys())
    insertion_point = bisect.bisect_left(start_keys, idx)
    if insertion_point == len(start_keys) or start_keys[insertion_point] != idx:
        insertion_point -= 1
    key_start = start_keys[insertion_point]
    result_start = unicode_data_to_category_start[key_start]

    end_keys = sorted(unicode_data_to_category_end.keys())
    insertion_point = bisect.bisect_left(end_keys, idx)
    try:
        key_end = end_keys[insertion_point]
        result_end = unicode_data_to_category_end[key_end]

        if result_end != key_start:
            result_end = result_start
            key_end = key_start
        else:
            result_end = unicode_data_to_category_start[result_end]

        if key_start <= idx <= key_end and result_start == result_end:
            return result_start
        else:
            return "Zzzz"
    except IndexError:
        return "Zzzz"


def bidirectional(chr: str) -> str:
    """Returns the bidirectional class assigned to the character chr as string.
    If no such value is defined, an empty string is returned."""
    idx = ord(chr)
    start_keys = sorted(unicode_data_to_bidirectional_start.keys())
    insertion_point = bisect.bisect_left(start_keys, idx)
    if insertion_point == len(start_keys) or start_keys[insertion_point] != idx:
        insertion_point -= 1
    key_start = start_keys[insertion_point]
    result_start = unicode_data_to_bidirectional_start[key_start]

    end_keys = sorted(unicode_data_to_bidirectional_end.keys())
    insertion_point = bisect.bisect_left(end_keys, idx)
    try:
        key_end = end_keys[insertion_point]
        result_end = unicode_data_to_bidirectional_end[key_end]

        if result_end != key_start:
            result_end = result_start
            key_end = key_start
        else:
            result_end = unicode_data_to_bidirectional_start[result_end]

        if key_start <= idx <= key_end and result_start == result_end:
            return result_start
        else:
            return ""
    except IndexError:
        return ""


def decimal(chr: str, default=None) -> int:
    """Returns the decimal value assigned to the character chr as integer.
    If no such value is defined, default is returned, or, if not given, ValueError is raised."""
    idx = ord(chr)
    try:
        return unicode_data_to_decimal_start[idx]
    except KeyError:
        if default is None:
            raise ValueError("not a decimal")
        else:
            return default


def digit(chr: str, default=None) -> int:
    """Returns the digit value assigned to the character chr as integer.
    If no such value is defined, default is returned, or, if not given, ValueError is raised."""
    idx = ord(chr)
    try:
        return unicode_data_to_digit_start[idx]
    except KeyError:
        if default is None:
            raise ValueError("not a digit")
        else:
            return default


def numeric(chr: str, default=None) -> float:
    """Returns the numeric value assigned to the character chr as float.
    If no such value is defined, default is returned, or, if not given, ValueError is raised."""
    idx = ord(chr)
    try:
        return unicode_data_to_numeric_start[idx]
    except KeyError:
        if default is None:
            raise ValueError("not a numeric character")
        else:
            return default


def combining(chr: str) -> int:
    """Returns the canonical combining class assigned to the character chr as integer.
    Returns 0 if no combining class is defined."""
    idx = ord(chr)
    try:
        return unicode_data_to_combining_start[idx]
    except KeyError:
        return 0


def mirrored(chr: str) -> int:
    """Returns the mirrored property assigned to the character chr as integer.
    Returns 1 if the character has been identified as a "mirrored" character in bidirectional text, 0 otherwise."""
    idx = ord(chr)
    start_keys = sorted(unicode_data_to_mirrored_start.keys())
    insertion_point = bisect.bisect_left(start_keys, idx)
    if insertion_point == len(start_keys) or start_keys[insertion_point] != idx:
        insertion_point -= 1
    key_start = start_keys[insertion_point]
    result_start = unicode_data_to_mirrored_start[key_start]

    end_keys = sorted(unicode_data_to_mirrored_end.keys())
    insertion_point = bisect.bisect_left(end_keys, idx)
    try:
        key_end = end_keys[insertion_point]
        result_end = unicode_data_to_mirrored_end[key_end]

        if result_end != key_start:
            result_end = result_start
            key_end = key_start
        else:
            result_end = unicode_data_to_mirrored_start[result_end]

        if key_start <= idx <= key_end and result_start == result_end:
            return result_start
        else:
            return 0
    except IndexError:
        return 0


def decomposition(chr: str) -> str:
    """Returns the character decomposition mapping assigned to the character chr as string.
    An empty string is returned in case no such mapping is defined."""
    idx = ord(chr)
    try:
        return unicode_data_to_decomposition_start[idx]
    except KeyError:
        return ""


def uppercase(chr: str) -> str:
    """"""
    idx = ord(chr)
    try:
        return unicode_data_to_uppercase_start[idx]
    except KeyError:
        return ""


def lowercase(chr: str) -> str:
    """"""
    idx = ord(chr)
    try:
        return unicode_data_to_lowercase_start[idx]
    except KeyError:
        return ""


def titlecase(chr: str) -> str:
    """"""
    idx = ord(chr)
    try:
        return unicode_data_to_titlecase_start[idx]
    except KeyError:
        return ""


def east_asian_width(chr: str, default=None) -> str:
    """Returns the east asian width assigned to the character chr as string."""
    idx = ord(chr)
    start_keys = sorted(east_asian_width_to_east_asian_width_start.keys())
    insertion_point = bisect.bisect_left(start_keys, idx)
    if insertion_point == len(start_keys) or start_keys[insertion_point] != idx:
        insertion_point -= 1
    key_start = start_keys[insertion_point]
    result_start = east_asian_width_to_east_asian_width_start[key_start]

    end_keys = sorted(east_asian_width_to_east_asian_width_end.keys())
    insertion_point = bisect.bisect_left(end_keys, idx)
    key_end = end_keys[insertion_point]
    result_end = east_asian_width_to_east_asian_width_end[key_end]

    if result_end != key_start:
        result_end = result_start
        key_end = key_start
    else:
        result_end = east_asian_width_to_east_asian_width_start[result_end]

    if key_start <= idx <= key_end and result_start == result_end:
        return result_start
    else:
        if default is None:
            raise ValueError("no east asian width")
        else:
            return default


def age(chr: str) -> str:
    """"""
    idx = ord(chr)
    start_keys = sorted(derived_age_to_age_start.keys())
    insertion_point = bisect.bisect_left(start_keys, idx)
    if insertion_point == len(start_keys) or start_keys[insertion_point] != idx:
        insertion_point -= 1
    key_start = start_keys[insertion_point]
    result_start = derived_age_to_age_start[key_start]

    end_keys = sorted(derived_age_to_age_end.keys())
    insertion_point = bisect.bisect_left(end_keys, idx)
    try:
        key_end = end_keys[insertion_point]
        result_end = derived_age_to_age_end[key_end]

        if result_end != key_start:
            result_end = result_start
            key_end = key_start
        else:
            result_end = derived_age_to_age_start[result_end]

        if key_start <= idx <= key_end and result_start == result_end:
            return result_start
        else:
            return "1.0"
    except IndexError:
        return "1.0"


def block(chr: str) -> str:
    """"""
    idx = ord(chr)
    start_keys = sorted(blocks_to_block_start.keys())
    insertion_point = bisect.bisect_left(start_keys, idx)
    if insertion_point == len(start_keys) or start_keys[insertion_point] != idx:
        insertion_point -= 1
    key_start = start_keys[insertion_point]
    result_start = blocks_to_block_start[key_start]

    end_keys = sorted(blocks_to_block_end.keys())
    insertion_point = bisect.bisect_left(end_keys, idx)
    try:
        key_end = end_keys[insertion_point]
        result_end = blocks_to_block_end[key_end]

        if result_end != key_start:
            result_end = result_start
            key_end = key_start
        else:
            result_end = blocks_to_block_start[result_end]

        if key_start <= idx <= key_end and result_start == result_end:
            return result_start
        else:
            return "Unknown"
    except IndexError:
        return "Unknown"


def script(chr: str) -> str:
    """"""
    idx = ord(chr)
    start_keys = sorted(scripts_to_script_start.keys())
    insertion_point = bisect.bisect_left(start_keys, idx)
    if insertion_point == len(start_keys) or start_keys[insertion_point] != idx:
        insertion_point -= 1
    key_start = start_keys[insertion_point]
    result_start = scripts_to_script_start[key_start]

    end_keys = sorted(scripts_to_script_end.keys())
    insertion_point = bisect.bisect_left(end_keys, idx)
    try:
        key_end = end_keys[insertion_point]
        result_end = scripts_to_script_end[key_end]

        if result_end != key_start:
            result_end = result_start
            key_end = key_start
        else:
            result_end = scripts_to_script_start[result_end]

        if key_start <= idx <= key_end and result_start == result_end:
            return result_start
        else:
            return "Unknown"
    except IndexError:
        return "Unknown"


def prop_list(chr: str) -> list:
    """"""
    idx = ord(chr)
    try:
        return prop_list_to_property[idx]
    except KeyError:
        return set()


def age_long(value: str) -> Optional[str]:
    """"""
    try:
        return property_value_alias_age_short_to_long[value]
    except KeyError:
        return None


def category_long(value: str) -> Optional[str]:
    """"""
    try:
        return property_value_alias_gc_short_to_long[value]
    except KeyError:
        return None


def east_asian_width_long(value: str) -> Optional[str]:
    """"""
    try:
        return property_value_alias_ea_short_to_long[value]
    except KeyError:
        return None


def bidirectional_long(value: str) -> Optional[str]:
    """"""
    try:
        return property_value_alias_bc_short_to_long[value]
    except KeyError:
        return None


def combining_long(value: str) -> Optional[str]:
    """"""
    try:
        return property_value_alias_ccc_short_to_long[value]
    except KeyError:
        return None


def block_abbr(value: str) -> Optional[str]:
    """"""
    try:
        return property_value_alias_blk_long_to_short[value]
    except KeyError:
        return None


def script_abbr(value: str) -> Optional[str]:
    """"""
    try:
        return property_value_alias_sc_long_to_short[value]
    except KeyError:
        return None


