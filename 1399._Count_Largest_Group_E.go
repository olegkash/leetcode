func countLargestGroup(n int) int {
	max_cnt := 0
	cnt := make(map[int]int)
	var tmp_sum int

	for i := 1; i <= n; i++ {
		tmp_sum = 0
		for ii := i; ii > 0; ii /= 10 {
			tmp_sum += ii % 10
		}
		cnt[tmp_sum]++
		max_cnt = max(max_cnt, cnt[tmp_sum])
	}

	var result int
	for _, value := range cnt {
		if max_cnt == value {
			result++
		}

	}

	return result    
}
