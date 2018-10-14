html-filtering.py
=================

a python program that removes HTML tags from an input file or url.

usage
-----

`python3 html-filtering.py test.html world`

or

`python3 html-filtering.py https://orf.at EU`

output for test.html
--------------------

```
file detected, reading...
title: Hello, world!
keywords: HTML,CSS,XML,JavaScript
description: Free Web tutorials
filtering html tags...
result:


  
    
    
    
    
    

    
    

    Hello, <<world>>!
  
  
    Hello, <<world>>!

    
    
    
    
    
  



```