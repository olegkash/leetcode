func findNumbers(nums []int) int {
    result := 0
    for _, n := range nums{
        if len(strconv.Itoa(n)) % 2 == 0 {
            result++
        }
    }

    return result
}
