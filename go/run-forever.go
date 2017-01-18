//Start doing something, listen forever. 
func main() {
	go startServer() /// depending on implementation, may loop forever inside this fxn 
	meta := make(chan int)
	x := <- meta    /// stay a while, and listen [link](https://www.youtube.com/watch?v=tAVVy_x3Erg)
	fmt.Println(x)  /// go makes you do something with every variable..
}
