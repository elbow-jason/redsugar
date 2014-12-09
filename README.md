redsugar
========

My little gem of a side project

### Rules:
1. There can be no unassigned strings. NO UNASSIGNED STRINGS.
    +  return "somestring"  #  is invalid
    +  x = "somestring"
    + return x            # is valid

### Types:

+ nil     => unit => ()  (is not actually nil; fuck nil)
+ int     => i64
+ float   => f64
+ bool    => bool
+ string  => String? &str?  (this needs figuring out)


### Processing Source/Lexing:

+ Strings and Regex are extracted first; They are to complex to do otherwise.
