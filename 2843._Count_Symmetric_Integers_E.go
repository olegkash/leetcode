func countSymmetricIntegers(low int, high int) int {
    var result int

    for i := low; i <= high; i++ {
        if i < 100 && i % 11 == 0 {
            result++
        }
        if i > 1000 {
            left  := i / 1000 + i % 1000 / 100
            right := i % 100 / 10 + i % 10
            if  left == right{
                result++
            }
        }
    }

    return result
}
