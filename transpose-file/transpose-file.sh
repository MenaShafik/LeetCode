# ==========================================================
# Problem    : Transpose File
# URL        : https://leetcode.com/problems/transpose-file/
# Difficulty : Medium
# Category   : Shell
# Tags       : Shell
#
# Acceptance : 31.8%
# Likes      : 164  |  Dislikes: 290
#
# Language   : bash
# Runtime    : 59  (beats 92.83890000000001%)
# Memory     : 4072000  (beats 60.4859%)
# Submitted  : 1779794938
# Exported   : 2026-05-26 11:31:01 UTC
#
# Hints: N/A
# ==========================================================
# Read from the file file.txt and print its transposed content to stdout.
awk '{
  for (i = 1; i <= NF; ++i) {
    if (NR == 1) {
      arr[i] = $i;
    } else {
      arr[i] = arr[i] " " $i;
    }
  }
} END {
  for (i = 1; i <= NF; ++i) {
    print arr[i];
  }
}' file.txt
