# ================================================================
# Problem : Sleep
# URL     : https://leetcode.com/problems/sleep/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 87.4%
# Likes           : 714
# Dislikes        : 61
#
# --- My Submission ---
# Language   : javascript
# Runtime    : 41  (beats 74.46660000000001%)
# Memory     : 53856000  (beats 29.909700000000004%)
# Submitted  : 1776015939
#
# --- Hints ---
# In Javascript, you can execute code after some delay with the setTimeout(fn, sleepTime) function.
# An async function is defined as function which returns a Promise.
# To create a Promise, you can code new Promise((resolve, reject) => {}). When you want the function to return a value, code resolve(value) inside the callback.
# ================================================================

/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
return new Promise(resolve => setTimeout(resolve, millis));
}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
