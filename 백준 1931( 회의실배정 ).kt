fun main(args: Array<String>) {
    val coins = arrayOf(0, 0)
    val n = readlnOrNull()

    n?.let {
        if (n.toInt() == 0 || n.toInt() == 1 || n.toInt() == 3){
            println("-1")
        } else {
            coins[0] = n.toInt() / 5
            if ((n.toInt() % 5) % 2 != 0){
                coins[0] -= 1
                coins[1] = (n.toInt() - (coins[0] * 5)) / 2
                println("${coins[0] + coins[1]}")
            }
            else if ((n.toInt() % 5) % 2 == 0){
                coins[1] = (n.toInt() % 5) / 2
                println("${coins[0] + coins[1]}")
            }
        }
    }
}
