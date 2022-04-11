# Multiline lambda Function
Multiline lambda function in python. Give arguments to lambdafunction() and include multiple lines in a single lambda function.

<h2>Syntax :</h2>
General Syntax : 
lambdaFunction.lambdafunction("list of string arguments", caller="string argument which gets calls the function.")
<br>
<ul>
<li>First list of arguements should be wrapped in single function.</li>
   eg. lambdaFunction.lambdafunction("def add(x, y) :","...", caller="...")
<li>All the syntax should be same as python. Use "\t" for indentation</li>
<li>Function should have some return method.</li>
   eg. lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="...")
<li>Then pass the function name to caller. (Here, "add")</li>
   eg. lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="add(3, 6)")
       returns -> 18
       when, print(lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="add(3, 6)"))
       prints -> 18.
</ul>
