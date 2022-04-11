# Multiline lambda Function
Multiline lambda function in python. Give arguments to lambdafunction() and include multiple lines in a single lambda function.

<h2>Syntax :</h2>
General Syntax : 
lambdaFunction.lambdafunction("list of string arguments", caller="string argument which gets calls the function.")
1. First list of arguements should be wrapped in single function.
   eg. lambdaFunction.lambdafunction("def add(x, y) :","...", caller="...")
2. All the syntax should be same as python. Use "\t" for indentation.
3. Function should have some return method.
   eg. lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="...")
4. Then pass the function name to caller. (Here, "add")
   eg. lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="add(3, 6)")
       returns -> 18
       when, print(lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="add(3, 6)"))
       prints -> 18.
   
