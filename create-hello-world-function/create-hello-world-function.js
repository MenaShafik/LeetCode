# ==========================================================
# Problem    : Create Hello World Function
# URL        : https://leetcode.com/problems/create-hello-world-function/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 81.9%
# Likes      : 1666  |  Dislikes: 229
#
# Language   : javascript
# Runtime    : 29  (beats 98.26530000000001%)
# Memory     : 53752000  (beats 35.117700000000035%)
# Submitted  : 1777318214
# Exported   : 2026-04-27 19:31:18 UTC
#
# Hints: N/A
# ==========================================================
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
    }
};
/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
