//taken from working example with docker containers
package main

import (
    "bufio"
    "flag"
    "fmt"
    "os"
    "strconv"
    "strings"
    "time"

    elastic "gopkg.in/olivere/elastic.v5"
)

var (
    clusterSize    = 4096
    esHost         = flag.String("elasticsearchhost", "http://esswarm_gateway:9200", "URL of ElasticSearch")
    parsedInfoPath = flag.String("ntfsinfo", "ntfs.extract", "Path to the extracted information of the ntfs image")

    allStellyRuns   []StellyRun
    fileInfoMapping map[uint64]FileInfo // allows us to look up fileinfo based on Id of fileinfo

    jobSubmitter elastic.BulkProcessor
)


func init() {
    flag.Parse()

    fileInfoMapping = make(map[uint64]FileInfo)

    jobSubmitter = setupBulkProcessor()
}


type FileInfo struct {
    Id          uint64
    Filenames   []string
    Createtime  time.Time
    Modifytime  time.Time
    Accesstime  time.Time
    Emodifytime time.Time
    Fflags      string
    Flags       string
    Filesize    uint64
    Dataruns    []DataRun
}
type DataRun struct {
    Runid         int
    Clusteroffset uint64
    Numclusters   uint64
}


func submitFileInfoToES(fi FileInfo) {

    resultIndex := elastic.NewBulkIndexRequest().
        Index("scarf").
        Type("file").
        Id(strconv.Itoa(int(fi.Id))).
        Doc(fi)

    jobSubmitter.Add(resultIndex)

    //  fmt.Println("Added to bulk submitter metadata for file ", resultIndex.Id, " to index ", resultIndex.Index, " jobtype ", resultIndex.Type)
}

func submitFileInfoToES(fi FileInfo) {

    resultIndex := elastic.NewBulkIndexRequest().
        Index("scarf").
        Type("file").
        Id(strconv.Itoa(int(fi.Id))).
        Doc(fi)

    jobSubmitter.Add(resultIndex)

    //  fmt.Println("Added to bulk submitter metadata for file ", resultIndex.Id, " to index ", resultIndex.Index, " jobtype ", resultIndex.Type)
}
