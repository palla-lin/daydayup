
import math
import datetime
s="bbtablud"
def slidewindow(s):
	max_len=0
	cur_win=set()
	left=0
	for i in range(len(s)):
		while s[i] in cur_win :
			cur_win.remove(s[left])
			left=left+1
		cur_win.add(s[i])			
		cur_len=len(cur_win)	
		if cur_len>max_len:
			max_len=cur_len;
	return max_len
ed=slidewindow(s)	
print(ed)