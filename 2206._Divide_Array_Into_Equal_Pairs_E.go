func divideArray(nums []int) bool {
    var pair = map[int]bool{}

    for _, num := range nums {
        if _, ok := pair[num]; ok{
            delete(pair, num)
        } else {
            pair[num] = true
        }
    }

    return len(pair) == 0
}
