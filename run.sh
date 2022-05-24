set -ex
problem=$1
inputNum=$2
go run $problem/run.go < $problem/input$inputNum
