## Design Document
A majority of the this document's sections have been convered in the intial [README] file so I will link to that document where necssary.

### Instructions for running script
To play this game run the following command on the command line inside this directory:
```bash
>>> python main.py
```

### Instructions for running testing
For testing I used the framework PyTest. To run my testing files perform the following commands within this projects directory:
```bash
>>> cd tests/
>>> pytest -v
```

### Rules for the game
The rules of the game have been explained in the [markdown file]. An external explanation can be found [here] as well.

### Brief Explanation of Design Decsisons
The logic behind creating the Accordion Solitarie was not very complicated. There were 3 main considerations one would have to make for this command line game:
1. How to efficiently determine if a move is valid?
2. How to efficiently represent the movemenet of one pile onto another?
3. How to cleanly depict the games state to a user and allow them to indicate what action needs to be performed?

I will address each of these cases and my corresponding design decision.  

**Consideration 1 (C1)**: This check was quite trivial. One would simply need to verify that the suits or the ranks in the cards are equivalent which can be done in constant time. The more important consideration surrounding this was to ensure that the user would be only able to pass cards that were valid into this check. To address this, I decided to create a wrapper function around this validity check that would ensure that both cards were present in the array and that the cards were seperated by either 1 or 3 spots.


**Consideration 2 (C2)**: Initally, this consideration seemed to be quite difficult as I thoughout one would need to display not only the top card of the pile, but also the underlying cards in said pile. But upon further deliberation, this representation would not only be inefficient, but it would also not provide any useful information to the user. As a result, the "merging of piles" operation can be done in constant time by copying the value of the right card into the left cards position and then deleting the right card's position in the array. In python this is a linear time operation with the `del` keyword object. I could reduce the time necessary for this operation through the create of a custom doubly linked list. I ultimately decided against this for 2 reasons. Firstly, the time to develop such a data structure would be quite long and would need to be extensively tested. Secondly, and more importantly, the data structure needs to quickly access elements of the array for this pile operation. Thus, the improvment one would see in this deletion operation (going from linear to constant time) would be rendered useless as accessing the elemnts would now become a linear time operation and this occurs more frequently in the program.

**Consideration 3 (C3)**: I had to go through a few variations of the way the user would interact with the program so that I could optomize for the user's experience. In my final interation, I capped the amount of cards that were displayed per line (4) and only displayed information that was pertinent to the user. This allowed for a cleaner interface for the user and made the game experience less overwhelming. Additionally, I decided to frequently display the board state so that the user would not have to continually scroll up in the command line. Finally, I numbered off the cards in the Tableau allowing for easy identification of cards for the merge pile operation.

Ultimately, the development of this game was quite fun and an interesting challenge!

### Choice of Language, Libraries, Frameworks
**Language**: I chose to use Python 3.5 for development of the command line script. I chose this language as I am most comfortable with it for generic scripting as well as the easy to use builtin libraries this language provides (such as the `random` library). Due to this, the development time for the program was not very long.

**Libraries**: The only libraries I made use of were python's `system` and `random` libraries. I made use of these libraries as they provided a very clean way to implement some integral portions of my program (clean exit of the program and shuffling of the deck respectively).

**Testing Frameworks**: I made use of the PyTest framework for my unit testing. I made this decsion because I am very familiar with the framework and as the code was not too complicated, a simple testing framework seemed like a good choice.

[README]:https://github.com/akiljames83/Accordion-Solitaire#welcome-to-accordion-solitaire
[markdown file]:https://github.com/akiljames83/Accordion-Solitaire#game-rules
[here]:https://www.bvssolitaire.com/rules/accordion.htm