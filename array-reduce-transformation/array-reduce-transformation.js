# ==========================================================
# Problem    : Array Reduce Transformation
# URL        : https://leetcode.com/problems/array-reduce-transformation/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 85.5%
# Likes      : 780  |  Dislikes: 51
#
# Language   : javascript
# Runtime    : 37  (beats 92.1209%)
# Memory     : 53756000  (beats 76.3618%)
# Submitted  : 1784898670
# Exported   : 2026-07-24 13:18:48 UTC
#
# Hints: Declare a variable "res" and set it it equal to the initial value.
#   Loop over each value in the array and set "res" = fn(res, arr[i]).
# ==========================================================
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let result = init;

    for (let i = 0; i < nums.length; i++) {
        result = fn(result, nums[i]);
    }

    return result;
};
