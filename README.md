# Epitech Workshop - Make your own autocorrect
## *How does an autocorrect works?*

## 1. Introduction

An autocorrect is a tool which, given a mispelled word input, outputs the closest correct word. (Example: tset -> test)

The founder of this feature is Dean Hachamovitch, who worked at Microsoft on the Word project. If this existed since the 90's, it has not evoluted a lot and the magic behind it is simple to understand.

Today, we will implement it together. 

## 2. Where to begin from ?

First, we need a list of all possible words you can use. Basically, a dictionnary.
We will use an english one for convenience (no special characters is used in his alphabet).

Let's use a pre-made one that you can download [here](https://github.com/dwyl/english-words/blob/master/words_alpha.txt)

Use the provided frequency.txt one, if you want to have only the 5000 more common words.

## 3. The algorithm

We basically have two cases : the given word is valid, so we can find it in our dictionnary or we don't find it, meaning it is incorrect.

Next, we generate all possible corrections to apply.

Finally, we return all valid words between generated corrections.

Note that you can also apply this algorithm on all the words of a text to obtain a spellchecker rather than an autocorrect.

## 4. Reproduce the different types of errors

We will keep things simple for this workshop, so we will focus on errors of distance 1, which means only one letter needs to be changed to get the valid word.

So in order to reproduce those errors, we can take the input word, and create all possible corrections by
- adding a letter: ```tset -> atset, btset, ctset, dtset, ...,tsety, tsetz```
- removing a letter:  ```tset -> set, tet, tst, tse```
- replacing a letter: ```tset -> ‘aset, bset, cset, ...,tsey, tsez```
- switching two adjacent letters: ```tset -> stet, ```**test**```, tste```

You can notice that the correct word is present in this list. As reproducing all the errors on the mispelled word error will give you at least one valid word.

## 5. Time to code !

Let's begin with some parsing. Words in our dictionnary are only separated by newlines, then it should not be difficult for you.

You should use a O(1) access data container, like map or dictionnary/set in order to keep your program fast.

Now that we have our database, let's generate the corrections for our given word.

Optimization is key, so we will pre-slice our word only one time rather than for each type of error.

Make a list of the word separated in two at each index
Given the word 'tset', the output of your function should be :
```
[
('', 'tset'),
('t', 'set'),
('te', 'st'),
('tes', 't'),
('test', '')
]
```

It will give you a left and a right part

Now, let's add the first type of correction : removing. Just remove the first letter of each right part (caution crashes on the last one, it is empty !)

The next one is adding a letter, same as above, you can add it to the start of the right part, except you have to iterate through all the letter of the alphabet.

We continue with a slightly more difficult one : replacing.
Do the same as removing, except you add a letter of the alphabet in the middle.

We finish with a more tedious one : swapping.
Just swap the last letter of the left part with the first letter of the right part (same as removing and replacing: don't forget that some of those strings are empty !)

All we have to do is merge all of those corrections and keep only valid words by checking if they are present our database.

And that's it !

## 6. Conclusion & Evolution !

Congratulations, you've made your first autocorrect, now you can enhance it by yourself.

You could make it :
- Harder : Propose the most probable word by adding words frequency checking (you can use the providedfrequency.txt based on the https://www.wordfrequency.info/ website. Words are listed in order of appearance)
- Better : Add more languages
- Faster : Implement it in a compiled language (C, Go...)
- Stronger : Implement deeper distance reseach (2+ type errors)

You can found on this repository a working python implementation of this algorithm, alongside with an example of the first evolution I proposed. Enjoy !
