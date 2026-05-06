# ==========================================================
# Problem    : Debounce
# URL        : https://leetcode.com/problems/debounce/
# Difficulty : Medium
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 91.7%
# Likes      : 484  |  Dislikes: 57
#
# Language   : javascript
# Runtime    : 39  (beats 95.96649999999998%)
# Memory     : 55108000  (beats 7.226799999999992%)
# Submitted  : 1778063618
# Exported   : 2026-05-06 22:39:27 UTC
#
# Hints: You execute code with a delay with "ref = setTimeout(fn, delay)". You can abort the execution of that code with "clearTimeout(ref)"
#   Whenever you call the function, you should abort any existing scheduled code. Then, you should schedule code to be executed after some delay.
# ==========================================================
/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeoutId = null;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn(...args), t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
