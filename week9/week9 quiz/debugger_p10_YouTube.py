def like_or_dislike(events):
	state = ""
	
	for event in events:
		if event == state:
			state = "nothing"
		else:
			state = event
	
	return state

print(like_or_dislike(["dislike","like"]))