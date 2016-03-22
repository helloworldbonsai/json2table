# json2table
python,json to html table.
very easy,but useful
>any question concact me..
>gmail: helloworldbonsai@gmail.com
>QQ: 1002432171
>I appreciate you bother.....

## How to use
```python
    #Arrcording to your path,import json2html 
    from json2HtmlTable.json2html import json2html 

    #call convert, it will html string
    json2html.convert(your json)  
```

## Example
### demo1 json contain  array
```python
   a = {"who": "我",
     "how": "love",
     "who": ["papa","mama"]}
```
*then the result*
<table border=1><tr>
                <th colspan="1" rowspan="1" >how</th>
                    
                <td colspan="1" rowspan="1" >love</td>
                    </tr><tr>
                <th colspan="1" rowspan="2" >who</th>
                    
                <td colspan="1" rowspan="1" >papa</td>
                    </tr><tr>
                <td colspan="1" rowspan="1" >mama</td>
                    </tr></table>

