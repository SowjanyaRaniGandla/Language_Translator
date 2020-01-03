# Language_Translator
This project will solve the problem of converting any source language to user given translation language.

In order to translate any text,phrase,paragraph to one's own desired language then here your search end.!
Steps to follow:(developed using PyCharm editor)

the code begins with importing Translator of Google API's
Input file is given in order to convert a paragraph of text to another language.
This input file consists of text written in any language.
Firstly user is asked to input the name of file along with extension,if the desired file is in same location of main file then directly input file name can be given as input else,the input file's path is to be given.
Next, user will be asked to input translation language you want to translate to..
The code is written in such a way to convert input languge case to default case.
some languages are given in dictionary to map , any number of languages can be given based on the developer's interest.
Inorder to put any language in dictionary, you need to first search google translate in browser and see the translation language value in the url bar as once you click on it.
https://translate.google.co.in/#view=home&op=translate&sl=auto&tl=en
for example in the above url 'sl' stands for source language and 'tl' stands for translation language,you need to put 'en' in dictionary value and respected key will be its language 'English'.

Then the code is simpler as creation of reference to Translator method is created and then result is printed.
