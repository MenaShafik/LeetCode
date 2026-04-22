# ==========================================================
# Problem    : Counter
# URL        : https://leetcode.com/problems/counter/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 82.4%
# Likes      : 1632  |  Dislikes: 130
#
# Language   : javascript
# Runtime    : 27  (beats 99.33660000000002%)
# Memory     : 53676000  (beats 50.336500000000036%)
# Submitted  : 1776893078
# Exported   : 2026-04-22 21:45:31 UTC
#
# Hints: In JavaScript, a function can return a closure. A closure is defined as a function and the variables declared around it (it's lexical environment).
#   A count variable can be initialized in the outer function and mutated in the inner function.
# ==========================================================
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    return function() {
        return n++
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
