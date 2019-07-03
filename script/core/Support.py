
def getGridTime(timeout, overhead = 0.33):
	''' computes the timeout of the grid based on the timeout (from the tool) received as parameter.
	Moreover it adds an overhead with is a percentage of the original timeout'''
	timetool = int(timeout)
	timetooloverhead = timetool + (timetool * overhead)
	hr_st = str(int(timetooloverhead  // 60))
	minutes = int(timetooloverhead  % 60)
	mt_st = str(minutes) if minutes >=10 else ("0" + str(minutes))
	timestring = hr_st + ":" + mt_st
	return timestring
