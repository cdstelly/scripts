package main

import (
	log "github.com/Sirupsen/logrus"
	"github.com/mattn/go-colorable"
)

func init() {
	log.SetFormatter(&log.TextFormatter{ForceColors: true})
	log.SetOutput(colorable.NewColorableStdout())
}

func checkError(err error) {
	if err != nil {
		log.Warn("Error!", err)
	}
}
