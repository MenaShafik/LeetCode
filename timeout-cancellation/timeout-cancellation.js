# ==========================================================
# Problem    : Timeout Cancellation
# URL        : https://leetcode.com/problems/timeout-cancellation/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 89.6%
# Likes      : 324  |  Dislikes: 375
#
# Language   : javascript
# Runtime    : 40  (beats 98.60900000000001%)
# Memory     : 54668000  (beats 18.450000000000017%)
# Submitted  : 1780393491
# Exported   : 2026-06-02 09:46:28 UTC
#
# Hints: N/A
# ==========================================================
/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    const timeoutId = setTimeout(() => fn(...args), t);

    const cancelFn = function() {
        clearTimeout(timeoutId);
    };

    return cancelFn;
};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelTimeMs);
 *           
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */
