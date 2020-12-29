
def solution(start: Int, length: Int): Int = {
  val nums = start until (start + length * length)
  nums.grouped(length)
    .zipWithIndex
    .flatMap { case (l, drop) => l.dropRight(drop) }
    .foldLeft(0)(_ ^ _)
}