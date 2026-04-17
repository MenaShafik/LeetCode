# ================================================================
# Problem : First Letter Capitalization II
# URL     : https://leetcode.com/problems/first-letter-capitalization-ii/
# Difficulty : Hard
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 50.4%
# Likes           : 32
# Dislikes        : 17
#
# --- My Submission ---
# Language   : postgresql
# Runtime    : 195  (beats 77.34800000000001%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1765199369
#
# --- Hints ---
# N/A
# ================================================================

-- Write your PostgreSQL query statement below
SELECT content_id, content_text AS original_text, REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE( CONCAT(UPPER(LEFT(LOWER(content_text), 1)), SUBSTRING(LOWER(content_text), 2)), ' a', ' A'), ' b', ' B'), ' c', ' C'), ' d', ' D'), ' e', ' E'), ' f', ' F'), ' g', ' G'), ' h', ' H'), ' i', ' I'), ' j', ' J'), ' k', ' K'), ' l', ' L'), ' m', ' M'), ' n', ' N'), ' o', ' O'), ' p', ' P'), ' q', ' Q'), ' r', ' R'), ' s', ' S'), ' t', ' T'), ' u', ' U'), ' v', ' V'), ' w', ' W'), ' x', ' X'), ' y', ' Y'), ' z', ' Z'), '-a', '-A'), '-b', '-B'), '-c', '-C'), '-d', '-D'), '-e', '-E'), '-f', '-F'), '-g', '-G'), '-h', '-H'), '-i', '-I'), '-j', '-J'), '-k', '-K'), '-l', '-L'), '-m', '-M'), '-n', '-N'), '-o', '-O'), '-p', '-P'), '-q', '-Q'), '-r', '-R'), '-s', '-S'), '-t', '-T'), '-u', '-U'), '-v', '-V'), '-w', '-W'), '-x', '-X'), '-y', '-Y'), '-z', '-Z') AS converted_text FROM user_content;
