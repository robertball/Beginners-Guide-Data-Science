# Beginners-Guide-Data-Science
Code and data files for "The Beginner's Guide to Data Science" by Robert Ball and Brian Rague

## Errata:
On page 164, Fig. 8.5 refers to text that did not get printed with the book.
Running the code that the caption refers to ('decision_tree.py') generates the following:<br />
<pre>
|--- snowing <= 0.50
|   |--- temperature <= 0.50
|   |   |--- class: 0
|   |--- temperature >  0.50
|   |   |--- temperature <= 1.50
|   |   |   |--- class: 1
|   |   |--- temperature >  1.50
|   |   |   |--- wind <= 1.50
|   |   |   |   |--- class: 0
|   |   |   |--- wind >  1.50
|   |   |   |   |--- class: 1
|--- snowing >  0.50
|   |--- wind <= 1.50
|   |   |--- class: 1
|   |--- wind >  1.50
|   |   |--- class: 0
</pre>


## Chapter 10.9 Update:

The *fbprophet* package is now rebranded as *prophet*. The documentation can be found here: https://facebook.github.io/prophet/docs/quick_start.html
