func findWordsContaining(words []string, x byte) []int {
    var result = []int{}

    for i, word := range(words){
        for _, char := range(word) {
            if (char == rune(x)) {
                result = append(result, i)
                break
            }
        }
    }
    return result 
}
