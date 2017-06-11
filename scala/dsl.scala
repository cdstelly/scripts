import scala.util.parsing.combinator.JavaTokenParsers

/**
test
f = "file:target.dd" extract files
test = "test.dd" extract files  
f
pdfs = f
pdfs = f | select "*.pdf"
pdfs = f | select "*.pdf", ctime > "01/01/2014"
pdfs = f | select "*.pdf", ctime <= "02/01/2014"
pdfs = f | select "*.pdf", ctime <= "01/01/2014", mtime > "01/02/2015"
*/
 
class FileHandler extends JavaTokenParsers {
	def string  : Parser[Any] = """".*"""".r
	def number  : Parser[Any] = "(0,9)+".r
	def literal : Parser[Any] = "[a-z]+".r

	def operator: Parser[Any] = ">" | "<" | ">=" | "<=" | "=="
	
	def actionVerb  : Parser[Any] = "[a-z]+".r

	def condition : Parser[Any] = ","~literal~operator~string

	def eval    : Parser[Any] = string~literal~literal						// To take care of 'f = "filename" extract files'
	def assign  : Parser[Any] = literal~"="~string | literal~"="~eval | literal~"="~literal
	def action  : Parser[Any] = actionVerb~string~opt(condition)
	def pipeAction : Parser[Any] = "|"~action

	/*
	def block : Parser[Any] = "{"~rep(email | move)~"}"
	def ifClause :Parser[Any] = "if"~"("~expr~")"~block
	def elseIfClause : Parser[Any] = "else"~ifClause
	def elseClause : Parser[Any] = "else"~block
	def ifElse : Parser[Any] = ifClause~opt(rep(elseIfClause))~opt(elseClause)
	*/

	def commandList = rep(assign | literal | action)~opt(pipeAction)
	//def commandList = assign~opt(pipeAction) | literal~opt(pipeAction) | action~(pipeAction)
}
