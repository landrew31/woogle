score = 0;
for (term in my_tags) {
	termInfo = _index['tags'].get(term,_POSITIONS);
	for (pos in termInfo) {
		score = score + 5 /(pow(pos.position, 0.6) + 5);
	}
}
return score;