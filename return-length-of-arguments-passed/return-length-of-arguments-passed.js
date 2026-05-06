# ==========================================================
# Problem    : Return Length of Arguments Passed
# URL        : https://leetcode.com/problems/return-length-of-arguments-passed/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 94.5%
# Likes      : 426  |  Dislikes: 177
#
# Language   : javascript
# Runtime    : 34  (beats 94.3013%)
# Memory     : 53392000  (beats 71.21640000000002%)
# Submitted  : 1778062810
# Exported   : 2026-05-06 22:39:30 UTC
#
# Hints: N/A
# ==========================================================
/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
