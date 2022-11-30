#!/usr/bin/env sh

matches_set=( $( grep -l "\<set(" *.py ) )
matches_dict=( $( grep -l "\<dict(" *.py ) )
matches_bstree=( $( grep -l "\<TreeNode" *.py ) )
matches_llist=( $( grep -l "\<ListNode" *.py ) )

echo "matches_set=(${matches_set[@]})"
echo "matches_dict=(${matches_dict[@]})"
echo "matches_bstree=(${matches_bstree[@]})"
echo "matches_llist=(${matches_llist[@]})"

