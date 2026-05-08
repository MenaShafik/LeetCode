# ==========================================================
# Problem    : Add Two Promises
# URL        : https://leetcode.com/problems/add-two-promises/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 91.7%
# Likes      : 364  |  Dislikes: 33
#
# Language   : javascript
# Runtime    : 46  (beats 87.74009999999998%)
# Memory     : 54744000  (beats 13.810900000000007%)
# Submitted  : 1778245418
# Exported   : 2026-05-08 13:05:17 UTC
#
# Hints: N/A
# ==========================================================
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    let result1 = await promise1;
    let result2 = await promise2;
    return result1 + result2; 
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
