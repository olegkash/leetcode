func buildArray(nums []int) []int {
    N := len(nums)
    var ans []int

    for i:=0; i<N; i++{
        ans = append(ans, nums[nums[i]])
    }

    return ans
}
