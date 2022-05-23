# Multiline lambda Function
[![PyPI Latest Release](https://img.shields.io/pypi/v/multiLineLambda.svg)](https://pypi.org/project/multiLineLambda/)
[![License](https://img.shields.io/pypi/l/multiLineLambda.svg)](https://github.com/NotShrirang/Multiline-lambda-Function/blob/main/LICENSE.md)

Multiline lambda function in python.
Give arguments to lambdafunction() and include multiple lines of code in a single lambda function.
<br>

## PyPI :
```sh
pip install multiLineLambda
```

## Dependencies
- [OS module](https://docs.python.org/3/library/os.html#module-os)

## License
[MIT](LICENSE)

<h2>Syntax :</h2>
General Syntax :

<code>lambdaFunction.lambdafunction("list of string arguments", caller="string argument which gets calls the function.")</code>
<br>
<ul>
<li>First list of arguements should be wrapped in single function.</li>
   eg. <code>lambdaFunction.lambdafunction("def add(x, y) :","...", caller="...")</code>
<li>All the syntax should be same as python. Use "\t" for indentation</li>
<li>Function should have some return method.</li>
   eg. <code>lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="...")</code>
<li>Then pass the function name to caller. (Here, "add")</li>
   eg. <code>lambdaFunction.lambdafunction("def add(x, y) :","\n\treturn(x+y)", caller="add(3, 6)")</code>
       returns -> 18
       <br>
</ul>
