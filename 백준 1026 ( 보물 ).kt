fun main(args: Array<String>) {
    val N = readlnOrNull()?.toInt()
    val A = IntArray(N!!)
    val B = IntArray(N!!)
    var S = 0

    val listA = readlnOrNull()?.split(" ")!!
    val listB = readlnOrNull()?.split(" ")!!

    for (i in 0 until N) {
        A[i] = listA[i].toInt()
        B[i] = listB[i].toInt()
    }

    A.sort()
    B.sort()

    for (i in 0 until N) {
        S += A[i] * B[N - i - 1]
    }

    println(S)
}
