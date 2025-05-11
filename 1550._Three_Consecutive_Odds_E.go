func threeConsecutiveOdds(arr []int) bool {
    var count int

    for _, n := range(arr){
        if n % 2 == 1 {
            count++
        } else {
            count = 0
        }

        if count == 3 {
            return true
        }
    }

    return false
}
