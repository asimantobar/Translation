# Variable-Excluding Automatic Translation

A python program with a Gooey GUI to read, translate DOCX files and write PO files all in a few clicks.

Specially designed for documents that includes parameters starting with "ID*_*" or enclosed by @ , excluding them from the translation. Helpful to translate auto-fill templates, not changing any variable names so the parameters can still be easily recognized and applied.


-----



The main steps followed by the code are:
1. Importing all the documents from the indicated path into a big TXT file that contains every character that appears in the documents. 
2. Loading this TXT file and converting to a data frame for easier data processing.
3. Cleaning the initial data frame, deleting repeated phrases and empty or NA values.
4. Identify every word that starts with "ID*_*" or is enclosed by @ (indicating that these are variables) and add to a new data frame. 
5. Assign to every registered variable a randomly generated unique 4-digit code.
6. Replace every variable with it's assigned code in the data frame that contains every unique phrase from the document list.
7. Using the [mtranslate](https://github.com/mouuff/mtranslate) library, translate every phrase from the data frame to the desired language.
8. Referring to the data frame containing the variables and associated codes, replace every code with the original variable name.
9.  Using the [Levenshtein](https://maxbachmann.github.io/Levenshtein/) python library, apply the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to the phrases and create a TXT files that collects the results. 
    * This helps identify phrases that have very little differences in characters. 
    * In this case, it is indicated to identify phrases that have a difference of less than 3 characters.
10. Write a TXT file with the format:
```
    # Comments
    msgid "original word"
    msgstr "translated word"
```
11. Create a copy of this file and change the extension from TXT to PO



-----


In case that the document's variables are not unified under the "ID*_*" prefix, there is a code provided to change the prefixes (id*_*, Tx, @ ) to the desired one. There are two versions of this code, one to be applied to DOCX files and one for TXT files. These can be found as Variable_Unification_DOCX.py and Variable_Unification_TXT.py in the "Desarrollo" folder. 