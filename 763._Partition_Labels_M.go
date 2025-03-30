func partitionLabels(s string) []int {
    last := map[rune]int{}
    result := []int{}

    for i, c := range s {
        last[c] = i
    }

    var end, size int

    for i, c := range s {
        size++
        end = max(end, last[c])

        if i == end {
            result = append(result, size)
            size = 0
        }
    }

    return result
}
