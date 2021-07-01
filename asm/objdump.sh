objdump -M intel --no-show-raw-insn --no-addresses -d $1

objdump -sj .data $1
