//remember to implement in gorat
c := make(chan os.Signal, 1)
signal.Notify(c, os.Interrupt)

go func(){
    for sig := range c {
        // sig is a ^C, handle it
    }
}()
