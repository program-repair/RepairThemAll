


def getGridTime(timeout, overhead = 0.33):
	timetool = int(timeout)
	timetooloverhead = timetool + (timetool * overhead)
	hr_st = str(int(timetooloverhead  // 60))
	minutes = int(timetooloverhead  % 60)
	mt_st = str(minutes) if minutes >=10 else ("0"+str(minutes))
	timestring = hr_st+":"+mt_st
	return timestring