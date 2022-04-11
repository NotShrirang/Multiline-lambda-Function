import os
def lambdafunction(*args, caller):
    for line in args:
        with open('lambdaInternal.py', 'a') as f:
            f.write(line)

    with open('lambdaInternal.py', 'a') as f:
        f.write("\n\ndef main():\n")
        f.write(f"\treturn {caller}")

    import lambdaInternal
    ret = lambdaInternal.main()
    os.remove('lambdaInternal.py')
    return ret

# syntax :
#     print(lambdafunction("def mul(a, b):", "\n\tz = a*b", "\n\treturn z", caller="mul(3, 6)"))    # prints : 18
