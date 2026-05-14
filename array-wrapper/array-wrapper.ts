# ==========================================================
# Problem    : Array Wrapper
# URL        : https://leetcode.com/problems/array-wrapper/
# Difficulty : Easy
# Category   : JavaScript
# Tags       : N/A
#
# Acceptance : 89.1%
# Likes      : 281  |  Dislikes: 63
#
# Language   : typescript
# Runtime    : 43  (beats 71.02050000000001%)
# Memory     : 55704000  (beats 68.57119999999999%)
# Submitted  : 1778751508
# Exported   : 2026-05-14 09:59:03 UTC
#
# Hints: N/A
# ==========================================================
class ArrayWrapper {
    private nums: number[];
    constructor(nums: number[]) {
        this.nums = nums;
    }
    
    valueOf(): number {
        return this.nums.reduce((a, b) => a + b, 0);
    }
    
    toString(): string {
        return `[${this.nums.join(',')}]`;
    }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
