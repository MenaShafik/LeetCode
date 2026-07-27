# ==========================================================
# Problem    : Chunk Array
# URL        : https://leetcode.com/problems/chunk-array/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 84.5%
# Likes      : 416  |  Dislikes: 14
#
# Language   : javascript
# Runtime    : 37  (beats 93.25280000000002%)
# Memory     : 57284000  (beats 24.571299999999965%)
# Submitted  : 1785141802
# Exported   : 2026-07-27 08:55:26 UTC
#
# Hints: N/A
# ==========================================================
/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let result = [];

    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }

    return result;
};
