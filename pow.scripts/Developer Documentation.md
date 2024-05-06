# Developer Documentation

## Script For Quickie
- `quickiePass` is a script that validates the user. if validated, it redirects to `quickiePow`. otherwise the script exits.
- `quickiePow` is the core script for Quickie. 
    
## Problem Statements
- Temporary Problems [None at the moment]
- Permanent Problems [None at the moment]
- Conceptual Problems [In Review]
    - Slow loading can result undetected elements.
- Technical Problems [In Progress]<br>
    - Microsoft rejects automatic/automated log in just like Google.<br> [Solved]
    - google Log in. 
        Insights:
            Perhaps the reason why it does not work is that because chrome driver is being detected. what if - i open chrome without the use of chromedriver and then automate log in.


## Solutions
   Microsoft rejects automatic/automated log in just like Google.<br>
   -in retrospect, i cloned the files and rerun the program. now it worked. causality unknown, but i suspect the powershell debugger.



## Progress Reports
- Script Terminals hidden [done]
- quickiePow.ps1 log in errors [done]<br>
    - Microsoft 
    - Github
- interoperability between `powershell` and `python` scrtips. i need `SeleniumBase` to bypass google log in but it only works well with python. therefore i intend to use   powershell script for other things and to use it to run the python script with seleniumBase.



## Future Implementations
- Self Extracting Quickkie Installation