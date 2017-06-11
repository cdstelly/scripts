import java.io.FileReader
import java.io.FileInputStream
 
object dslTest extends FileHandler {
 
  def main(args: Array[String]): Unit = {
    val reader = new FileReader("filein.txt")
    println(parseAll(commandList, reader))
  }
 
}
