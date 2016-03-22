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

## not support
**json like [1,2,3],means json out bordary is array**

## Example
### demo1 json contain  array
```python
case = {"who": "我",
     "how": "love",
     "who": ["papa","mama"]}
```
*then the result*
```html
<table border=1><tr>
                <th colspan="1" rowspan="1" >how</th>
                    
                <td colspan="1" rowspan="1" >love</td>
                    </tr><tr>
                <th colspan="1" rowspan="2" >who</th>
                    
                <td colspan="1" rowspan="1" >papa</td>
                    </tr><tr>
                <td colspan="1" rowspan="1" >mama</td>
                    </tr></table>
```

### demo2 json string
```python
case =''' {"who": "我",
     "how": "love",
     "who": ["papa","mama"]}'''
```
*then the result like demo1*

### demo3 some complex

```python
case = {"country" : [{1:"china",2:"japan",3:"thailand"},
                     ["USA","UK","AUS"],
                     {"food":["china","china","china"],
                      "girl":["japan","japan","japan"],
                      "genius":["usa","usa","usa"],
                      "hunk":["russia","russia","russia"]}],        
        "where":{"earth":{"asia":{"china":{"jiangxi":{"fuzhou":{"linchuan":{"shangdundu":{"east bridge road":"31 number"}}}}}}}},
        }
```
*then the reuslt*
<table border=1><tr>
                <th colspan="1" rowspan="18" >country</th>
                    
                <th colspan="1" rowspan="1" >1</th>
                    
                <td colspan="8" rowspan="1" >china</td>
                    </tr><tr>
                <th colspan="1" rowspan="1" >2</th>
                    
                <td colspan="8" rowspan="1" >japan</td>
                    </tr><tr>
                <th colspan="1" rowspan="1" >3</th>
                    
                <td colspan="8" rowspan="1" >thailand</td>
                    </tr><tr>
                <td colspan="9" rowspan="1" >USA</td>
                    </tr><tr>
                <td colspan="9" rowspan="1" >UK</td>
                    </tr><tr>
                <td colspan="9" rowspan="1" >AUS</td>
                    </tr><tr>
                <th colspan="1" rowspan="3" >food</th>
                    
                <td colspan="8" rowspan="1" >china</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >china</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >china</td>
                    </tr><tr>
                <th colspan="1" rowspan="3" >genius</th>
                    
                <td colspan="8" rowspan="1" >usa</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >usa</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >usa</td>
                    </tr><tr>
                <th colspan="1" rowspan="3" >girl</th>
                    
                <td colspan="8" rowspan="1" >japan</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >japan</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >japan</td>
                    </tr><tr>
                <th colspan="1" rowspan="3" >hunk</th>
                    
                <td colspan="8" rowspan="1" >russia</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >russia</td>
                    </tr><tr>
                <td colspan="8" rowspan="1" >russia</td>
                    </tr><tr>
                <th colspan="1" rowspan="1" >where</th>
                    
                <th colspan="1" rowspan="1" >earth</th>
                    
                <th colspan="1" rowspan="1" >asia</th>
                    
                <th colspan="1" rowspan="1" >china</th>
                    
                <th colspan="1" rowspan="1" >jiangxi</th>
                    
                <th colspan="1" rowspan="1" >fuzhou</th>
                    
                <th colspan="1" rowspan="1" >linchuan</th>
                    
                <th colspan="1" rowspan="1" >shangdundu</th>
                    
                <th colspan="1" rowspan="1" >east bridge road</th>
                    
                <td colspan="1" rowspan="1" >31 number</td>
                    </tr></table>






